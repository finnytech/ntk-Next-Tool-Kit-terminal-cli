"""DevOps & cloud management (ntk cloud ...). Wraps aws/gcloud/kubectl/helm/terraform CLIs."""
import os
import json
import urllib.request
from . import util
from .util import col, C, run, which


def _need(cli):
    if not which(cli):
        util.warn(f"{cli} CLI not found on PATH. Install it first.")
        return False
    return True


def aws_s3_ls(args):
    """List an S3 bucket's contents."""
    if not _need("aws"):
        return 1
    target = args[0] if args else ""
    rc, o, e = run(["aws", "s3", "ls"] + ([target] if target else []))
    print(o or e)
    return rc


def aws_s3_sync(args):
    """Sync a local dir with S3."""
    if len(args) < 2:
        util.err("usage: ntk cloud aws-s3-sync <src> <dst>")
        return 2
    if not _need("aws"):
        return 1
    rc, o, e = run(["aws", "s3", "sync", args[0], args[1]])
    print(o or e)
    return rc


def aws_ec2_ls(args):
    """List EC2 instances."""
    if not _need("aws"):
        return 1
    rc, o, e = run(["aws", "ec2", "describe-instances", "--query",
                    "Reservations[].Instances[].[InstanceId,State.Name,InstanceType,PublicIpAddress]",
                    "--output", "table"])
    print(o or e)
    return rc


def gcp_bucket_ls(args):
    """List a Google Cloud Storage bucket."""
    if not _need("gsutil") and not _need("gcloud"):
        return 1
    cli = "gsutil" if which("gsutil") else "gcloud"
    cmd = ["gsutil", "ls"] if cli == "gsutil" else ["gcloud", "storage", "ls"]
    rc, o, e = run(cmd + args)
    print(o or e)
    return rc


def kube_ctx(args):
    """Switch/show kube context."""
    if not _need("kubectl"):
        return 1
    if args:
        rc, o, e = run(["kubectl", "config", "use-context", args[0]])
    else:
        rc, o, e = run(["kubectl", "config", "get-contexts"])
    print(o or e)
    return rc


def kube_ns(args):
    """Switch the default namespace."""
    if not _need("kubectl"):
        return 1
    if not args:
        rc, o, e = run(["kubectl", "get", "namespaces"])
        print(o or e)
        return rc
    rc, o, e = run(["kubectl", "config", "set-context", "--current", "--namespace", args[0]])
    print(o or e or f"namespace -> {args[0]}")
    return rc


def action_lint(args):
    """Validate a GitHub Actions workflow YAML."""
    if not args:
        util.err("usage: ntk cloud action-lint <workflow.yml>")
        return 2
    text = open(args[0], encoding="utf-8").read()
    try:
        import yaml
        data = yaml.safe_load(text)
    except ImportError:
        util.warn("PyYAML not installed; doing a basic structural check")
        if "jobs:" not in text or ("on:" not in text and "on :" not in text):
            util.err("missing required keys 'on' / 'jobs'")
            return 1
        util.ok("basic structure looks OK")
        return 0
    except Exception as e:
        util.err(f"YAML error: {e}")
        return 1
    problems = []
    if "on" not in data:
        problems.append("missing 'on' trigger")
    if "jobs" not in data:
        problems.append("missing 'jobs'")
    else:
        for name, job in (data["jobs"] or {}).items():
            if "runs-on" not in job:
                problems.append(f"job '{name}' missing 'runs-on'")
    if problems:
        for p in problems:
            util.err(p)
        return 1
    util.ok("workflow valid")
    return 0


def docker_push(args):
    """Build and push a docker image in one step."""
    if len(args) < 1:
        util.err("usage: ntk cloud docker-push <image:tag> [context=.]")
        return 2
    if not _need("docker"):
        return 1
    ctx = args[1] if len(args) > 1 else "."
    rc, o, e = run(["docker", "build", "-t", args[0], ctx])
    print(o or e)
    if rc != 0:
        return rc
    rc, o, e = run(["docker", "push", args[0]])
    print(o or e)
    return rc


def env_sync(args):
    """Diff local .env against a target (prints diff)."""
    if not args:
        util.err("usage: ntk cloud env-sync <.env> [other.env]")
        return 2

    def parse(p):
        d = {}
        if os.path.exists(p):
            for line in open(p, encoding="utf-8"):
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    d[k.strip()] = v.strip()
        return d
    a = parse(args[0])
    b = parse(args[1]) if len(args) > 1 else {}
    util.header("Env diff")
    for k in sorted(set(a) | set(b)):
        if k not in b:
            print(col(f"  only in {args[0]}: {k}", C.YELLOW))
        elif k not in a:
            print(col(f"  only in {args[1]}: {k}", C.CYAN))
        elif a[k] != b[k]:
            print(col(f"  differs: {k}", C.RED))
    return 0


def log_stream(args):
    """Stream cloud logs (AWS CloudWatch / GCP)."""
    if which("aws"):
        if not args:
            util.err("usage: ntk cloud log-stream <log-group>")
            return 2
        rc, o, e = run(["aws", "logs", "tail", args[0], "--follow"])
        print(o or e)
        return rc
    util.warn("needs aws CLI (CloudWatch) or gcloud")
    return 1


def helm_ls(args):
    """List installed Helm charts."""
    if not _need("helm"):
        return 1
    rc, o, e = run(["helm", "list", "-A"])
    print(o or e)
    return rc


def tf_lint(args):
    """Validate/format Terraform files."""
    if not _need("terraform"):
        return 1
    rc, o, e = run(["terraform", "fmt", "-check", "-diff"])
    print(o or e)
    rc2, o2, e2 = run(["terraform", "validate"])
    print(o2 or e2)
    return rc or rc2


def cf_purge(args):
    """Purge Cloudflare cache for a zone (needs CF_API_TOKEN)."""
    if not args:
        util.err("usage: ntk cloud cf-purge <zone-id>")
        return 2
    token = os.environ.get("CF_API_TOKEN")
    if not token:
        util.warn("set CF_API_TOKEN environment variable")
        return 1
    zone = args[0]
    body = json.dumps({"purge_everything": True}).encode()
    req = urllib.request.Request(
        f"https://api.cloudflare.com/client/v4/zones/{zone}/purge_cache",
        data=body, method="POST",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            res = json.loads(r.read())
        if res.get("success"):
            util.ok("cache purged")
        else:
            util.err(res.get("errors"))
    except Exception as e:
        util.err(e)
        return 1
    return 0


def vercel_deploy(args):
    """Deploy to Vercel."""
    if not _need("vercel"):
        return 1
    rc, o, e = run(["vercel", "--yes"] + args)
    print(o or e)
    return rc


def netlify_deploy(args):
    """Deploy to Netlify."""
    if not _need("netlify"):
        return 1
    rc, o, e = run(["netlify", "deploy"] + args)
    print(o or e)
    return rc


COMMANDS = {
    "aws-s3-ls": aws_s3_ls, "aws-s3-sync": aws_s3_sync, "aws-ec2-ls": aws_ec2_ls,
    "gcp-bucket-ls": gcp_bucket_ls, "kube-ctx": kube_ctx, "kube-ns": kube_ns,
    "action-lint": action_lint, "docker-push": docker_push, "env-sync": env_sync,
    "log-stream": log_stream, "helm-ls": helm_ls, "tf-lint": tf_lint,
    "cf-purge": cf_purge, "vercel-deploy": vercel_deploy, "netlify-deploy": netlify_deploy,
}
