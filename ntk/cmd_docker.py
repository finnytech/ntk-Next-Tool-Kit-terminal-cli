"""Docker & container tools (ntk docker ...). Thin, safe wrappers over docker/kubectl."""
from . import util
from .util import col, C, run, which


def _need_docker():
    if not which("docker"):
        util.warn("docker not found on PATH. Install Docker Desktop / engine.")
        return False
    return True


def _d(args_list):
    rc, o, e = run(["docker"] + args_list)
    if o:
        print(o.rstrip())
    if e and rc != 0:
        print(col(e.rstrip(), C.YELLOW))
    return rc


def ps(args):
    """List running containers with stats."""
    if not _need_docker():
        return 1
    return _d(["ps", "--format",
               "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"])


def clean(args):
    """Prune stopped containers, unused nets & dangling images."""
    if not _need_docker():
        return 1
    return _d(["system", "prune", "-f"])


def logs(args):
    """Stream a container's logs (name/id)."""
    if not args:
        util.err("usage: ntk docker logs <container> [--tail N]")
        return 2
    if not _need_docker():
        return 1
    return _d(["logs", "--tail", "200", "-f"] + args)


def stats(args):
    """Live resource usage of running containers."""
    if not _need_docker():
        return 1
    return _d(["stats", "--no-stream"])


def ip(args):
    """Internal IP of a running container."""
    if not args:
        util.err("usage: ntk docker ip <container>")
        return 2
    if not _need_docker():
        return 1
    return _d(["inspect", "-f",
               "{{range .NetworkSettings.Networks}}{{.IPAddress}} {{end}}", args[0]])


def exec_(args):
    """Open a shell inside a container."""
    if not args:
        util.err("usage: ntk docker exec <container> [cmd]")
        return 2
    if not _need_docker():
        return 1
    cmd = args[1:] if len(args) > 1 else ["/bin/sh"]
    rc, o, e = run(["docker", "exec", "-it", args[0]] + cmd)
    print(o or e)
    return rc


def ports(args):
    """Show port mappings of all containers."""
    if not _need_docker():
        return 1
    return _d(["ps", "--format", "table {{.Names}}\t{{.Ports}}"])


def stop_all(args):
    """Stop all running containers."""
    if not _need_docker():
        return 1
    rc, o, e = run(["docker", "ps", "-q"])
    ids = o.split()
    if not ids:
        util.info("no running containers")
        return 0
    return _d(["stop"] + ids)


def volume_size(args):
    """Show disk usage of docker volumes."""
    if not _need_docker():
        return 1
    return _d(["system", "df", "-v"])


def inspect_env(args):
    """Show environment variables inside a container."""
    if not args:
        util.err("usage: ntk docker inspect-env <container>")
        return 2
    if not _need_docker():
        return 1
    return _d(["inspect", "-f", "{{range .Config.Env}}{{println .}}{{end}}", args[0]])


def compose_up(args):
    """docker compose up -d."""
    if not _need_docker():
        return 1
    rc, o, e = run(["docker", "compose", "up", "-d"] + args)
    print(o or e)
    return rc


def compose_down(args):
    """docker compose down."""
    if not _need_docker():
        return 1
    rc, o, e = run(["docker", "compose", "down"] + args)
    print(o or e)
    return rc


def image_history(args):
    """Show layers of a local image."""
    if not args:
        util.err("usage: ntk docker image-history <image>")
        return 2
    if not _need_docker():
        return 1
    return _d(["history", args[0]])


def image_prune(args):
    """Remove dangling images."""
    if not _need_docker():
        return 1
    return _d(["image", "prune", "-f"])


def network_list(args):
    """List docker networks."""
    if not _need_docker():
        return 1
    return _d(["network", "ls"])


def copy_to(args):
    """Copy host file into a container (src container:dest)."""
    if len(args) < 2:
        util.err("usage: ntk docker copy-to <src> <container:dest>")
        return 2
    if not _need_docker():
        return 1
    return _d(["cp", args[0], args[1]])


def copy_from(args):
    """Copy from a container to host (container:src dest)."""
    if len(args) < 2:
        util.err("usage: ntk docker copy-from <container:src> <dest>")
        return 2
    if not _need_docker():
        return 1
    return _d(["cp", args[0], args[1]])


def health(args):
    """Show health status of containers."""
    if not _need_docker():
        return 1
    return _d(["ps", "--format", "table {{.Names}}\t{{.Status}}"])


def dockerfile_gen(args):
    """Generate an optimized Dockerfile (node/python/go)."""
    lang = (args[0].lower() if args else "python")
    templates = {
        "python": """FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
""",
        "node": """FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
EXPOSE 3000
CMD ["node", "index.js"]
""",
        "go": """FROM golang:1.22 AS build
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o /app ./...

FROM gcr.io/distroless/static
COPY --from=build /app /app
ENTRYPOINT ["/app"]
""",
    }
    if lang not in templates:
        util.err(f"supported: {', '.join(templates)}")
        return 2
    print(templates[lang])
    return 0


def registry_login(args):
    """Test login to a docker registry."""
    if not args:
        util.err("usage: ntk docker registry-login <registry>")
        return 2
    if not _need_docker():
        return 1
    rc, o, e = run(["docker", "login", args[0]])
    print(o or e)
    return rc


def k8s_pods(args):
    """List pods in the current kube context."""
    if not which("kubectl"):
        util.warn("kubectl not found on PATH")
        return 1
    rc, o, e = run(["kubectl", "get", "pods", "-A"])
    print(o or e)
    return rc


COMMANDS = {
    "ps": ps, "clean": clean, "logs": logs, "stats": stats, "ip": ip,
    "exec": exec_, "ports": ports, "stop-all": stop_all, "volume-size": volume_size,
    "inspect-env": inspect_env, "compose-up": compose_up, "compose-down": compose_down,
    "image-history": image_history, "image-prune": image_prune,
    "network-list": network_list, "copy-to": copy_to, "copy-from": copy_from,
    "health": health, "dockerfile-gen": dockerfile_gen,
    "registry-login": registry_login, "k8s-pods": k8s_pods,
}
