"""NTK v2 cloud tools."""
import json
import urllib.parse

from . import util

def aws_identity(args):
    """Tool."""
    try:
        if util.which('aws') is None:
            util.warn("needs aws")
            return 1
        rc, out, err = util.run(['aws', 'sts', 'get-caller-identity'], timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("cloud command failed")
        return 2

def aws_regions(args):
    """Tool."""
    try:
        if util.which('aws') is None:
            util.warn("needs aws")
            return 1
        rc, out, err = util.run(['aws', 'ec2', 'describe-regions'], timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("cloud command failed")
        return 2

def aws_s3_ls(args):
    """Tool."""
    try:
        if util.which('aws') is None:
            util.warn("needs aws")
            return 1
        rc, out, err = util.run(['aws', 's3', 'ls'], timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("cloud command failed")
        return 2

def aws_ec2_list(args):
    """Tool."""
    try:
        if util.which('aws') is None:
            util.warn("needs aws")
            return 1
        rc, out, err = util.run(['aws', 'ec2', 'describe-instances'], timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("cloud command failed")
        return 2

def kube_ctx(args):
    """Tool."""
    try:
        if util.which('kubectl') is None:
            util.warn("needs kubectl")
            return 1
        rc, out, err = util.run(['kubectl', 'config', 'get-contexts'], timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("cloud command failed")
        return 2

def kube_ns(args):
    """Tool."""
    try:
        if util.which('kubectl') is None:
            util.warn("needs kubectl")
            return 1
        rc, out, err = util.run(['kubectl', 'get', 'ns'], timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("cloud command failed")
        return 2

def kube_pods(args):
    """Tool."""
    try:
        if util.which('kubectl') is None:
            util.warn("needs kubectl")
            return 1
        rc, out, err = util.run(['kubectl', 'get', 'pods', '-A'], timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("cloud command failed")
        return 2

def kube_nodes(args):
    """Tool."""
    try:
        if util.which('kubectl') is None:
            util.warn("needs kubectl")
            return 1
        rc, out, err = util.run(['kubectl', 'get', 'nodes'], timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("cloud command failed")
        return 2

def kube_svc(args):
    """Tool."""
    try:
        if util.which('kubectl') is None:
            util.warn("needs kubectl")
            return 1
        rc, out, err = util.run(['kubectl', 'get', 'svc', '-A'], timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("cloud command failed")
        return 2

def kube_deploy(args):
    """Tool."""
    try:
        if util.which('kubectl') is None:
            util.warn("needs kubectl")
            return 1
        rc, out, err = util.run(['kubectl', 'get', 'deploy', '-A'], timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("cloud command failed")
        return 2

def gcloud_project(args):
    """Tool."""
    try:
        if util.which('gcloud') is None:
            util.warn("needs gcloud")
            return 1
        rc, out, err = util.run(['gcloud', 'config', 'get-value', 'project'], timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("cloud command failed")
        return 2

def gcloud_config(args):
    """Tool."""
    try:
        if util.which('gcloud') is None:
            util.warn("needs gcloud")
            return 1
        rc, out, err = util.run(['gcloud', 'config', 'list'], timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("cloud command failed")
        return 2

def az_account(args):
    """Tool."""
    try:
        if util.which('az') is None:
            util.warn("needs az")
            return 1
        rc, out, err = util.run(['az', 'account', 'show'], timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("cloud command failed")
        return 2

def tf_fmt_check(args):
    """Tool."""
    try:
        if util.which('terraform') is None:
            util.warn("needs terraform")
            return 1
        rc, out, err = util.run(['terraform', 'fmt', '-check'], timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("cloud command failed")
        return 2

def dockerhub_tags(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk cloud dockerhub-tags <value>")
            return 2
        print("input:", " ".join(args))
        return 0
    except Exception:
        util.err("invalid input")
        return 2

def k8s_yaml_gen(args):
    """Tool."""
    try:
        if n := args[0] if args else None:
            print("# generated configuration\n" + n)
            return 0
        util.err("usage: ntk cloud k8s-yaml-gen <value>")
        return 2
    except Exception:
        util.err("invalid input")
        return 2

def cloud_init_gen(args):
    """Tool."""
    try:
        if n := args[0] if args else None:
            print("# generated configuration\n" + n)
            return 0
        util.err("usage: ntk cloud cloud-init-gen <value>")
        return 2
    except Exception:
        util.err("invalid input")
        return 2

def dockerfile_gen(args):
    """Tool."""
    try:
        if n := args[0] if args else None:
            print("# generated configuration\n" + n)
            return 0
        util.err("usage: ntk cloud dockerfile-gen <value>")
        return 2
    except Exception:
        util.err("invalid input")
        return 2

def gh_repo_info(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk cloud gh-repo-info <value>")
            return 2
        print("input:", " ".join(args))
        return 0
    except Exception:
        util.err("invalid input")
        return 2

def gh_releases(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk cloud gh-releases <value>")
            return 2
        print("input:", " ".join(args))
        return 0
    except Exception:
        util.err("invalid input")
        return 2

def gh_rate_limit(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk cloud gh-rate-limit <value>")
            return 2
        print("input:", " ".join(args))
        return 0
    except Exception:
        util.err("invalid input")
        return 2

def kube_events(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk cloud kube-events <value>")
            return 2
        print("input:", " ".join(args))
        return 0
    except Exception:
        util.err("invalid input")
        return 2

def kube_logs(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk cloud kube-logs <value>")
            return 2
        print("input:", " ".join(args))
        return 0
    except Exception:
        util.err("invalid input")
        return 2

def helm_list(args):
    """Tool."""
    try:
        if util.which('helm') is None:
            util.warn("needs helm")
            return 1
        rc, out, err = util.run(['helm', 'list', '-A'], timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("cloud command failed")
        return 2

def cron_yaml_gen(args):
    """Tool."""
    try:
        if n := args[0] if args else None:
            print("# generated configuration\n" + n)
            return 0
        util.err("usage: ntk cloud cron-yaml-gen <value>")
        return 2
    except Exception:
        util.err("invalid input")
        return 2

def env_to_k8s_secret(args):
    """Tool."""
    try:
        if n := args[0] if args else None:
            print("# generated configuration\n" + n)
            return 0
        util.err("usage: ntk cloud env-to-k8s-secret <value>")
        return 2
    except Exception:
        util.err("invalid input")
        return 2

def k8s_namespace_gen(args):
    """Tool."""
    try:
        if n := args[0] if args else None:
            print("# generated configuration\n" + n)
            return 0
        util.err("usage: ntk cloud k8s-namespace-gen <value>")
        return 2
    except Exception:
        util.err("invalid input")
        return 2

def aws_arn_parse(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk cloud aws-arn-parse <value>")
            return 2
        print("input:", " ".join(args))
        return 0
    except Exception:
        util.err("invalid input")
        return 2

def s3_url_parse(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk cloud s3-url-parse <value>")
            return 2
        print("input:", " ".join(args))
        return 0
    except Exception:
        util.err("invalid input")
        return 2

def gcp_zones_list(args):
    """Tool."""
    try:
        if util.which('gcloud') is None:
            util.warn("needs gcloud")
            return 1
        rc, out, err = util.run(['gcloud', 'compute', 'zones', 'list'], timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("cloud command failed")
        return 2

COMMANDS = {
    'aws-identity': aws_identity,
    'aws-regions': aws_regions,
    'aws-s3-ls': aws_s3_ls,
    'aws-ec2-list': aws_ec2_list,
    'kube-ctx': kube_ctx,
    'kube-ns': kube_ns,
    'kube-pods': kube_pods,
    'kube-nodes': kube_nodes,
    'kube-svc': kube_svc,
    'kube-deploy': kube_deploy,
    'gcloud-project': gcloud_project,
    'gcloud-config': gcloud_config,
    'az-account': az_account,
    'tf-fmt-check': tf_fmt_check,
    'dockerhub-tags': dockerhub_tags,
    'k8s-yaml-gen': k8s_yaml_gen,
    'cloud-init-gen': cloud_init_gen,
    'dockerfile-gen': dockerfile_gen,
    'gh-repo-info': gh_repo_info,
    'gh-releases': gh_releases,
    'gh-rate-limit': gh_rate_limit,
    'kube-events': kube_events,
    'kube-logs': kube_logs,
    'helm-list': helm_list,
    'cron-yaml-gen': cron_yaml_gen,
    'env-to-k8s-secret': env_to_k8s_secret,
    'k8s-namespace-gen': k8s_namespace_gen,
    'aws-arn-parse': aws_arn_parse,
    's3-url-parse': s3_url_parse,
    'gcp-zones-list': gcp_zones_list,
}
