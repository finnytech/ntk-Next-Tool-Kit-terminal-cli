"""NTK v2 docker tools."""
import os

from . import util

def ps(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['ps'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

def ps_all(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['ps', '-a'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

def images(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['images'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

def pull(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk docker pull ...")
            return 2
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        extra = list(args)
        if 'pull' == "healthcheck":
            extra = [args[0], "--format", "{{.State.Health.Status}}"]
        rc, out, err = util.run(["docker", "pull"] + extra, timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("usage: ntk docker pull ...")
        return 2

def stats(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['stats', '--no-stream'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

def logs(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk docker logs ...")
            return 2
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        extra = list(args)
        if 'logs' == "healthcheck":
            extra = [args[0], "--format", "{{.State.Health.Status}}"]
        rc, out, err = util.run(["docker", "logs"] + extra, timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("usage: ntk docker logs ...")
        return 2

def inspect(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk docker inspect ...")
            return 2
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        extra = list(args)
        if 'inspect' == "healthcheck":
            extra = [args[0], "--format", "{{.State.Health.Status}}"]
        rc, out, err = util.run(["docker", "inspect"] + extra, timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("usage: ntk docker inspect ...")
        return 2

def volumes(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['volume', 'ls'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

def networks(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['network', 'ls'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

def prune_preview(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['system', 'df'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

def prune(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['system', 'prune'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

def stop(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk docker stop ...")
            return 2
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        extra = list(args)
        if 'stop' == "healthcheck":
            extra = [args[0], "--format", "{{.State.Health.Status}}"]
        rc, out, err = util.run(["docker", "stop"] + extra, timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("usage: ntk docker stop ...")
        return 2

def start(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk docker start ...")
            return 2
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        extra = list(args)
        if 'start' == "healthcheck":
            extra = [args[0], "--format", "{{.State.Health.Status}}"]
        rc, out, err = util.run(["docker", "start"] + extra, timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("usage: ntk docker start ...")
        return 2

def restart(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk docker restart ...")
            return 2
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        extra = list(args)
        if 'restart' == "healthcheck":
            extra = [args[0], "--format", "{{.State.Health.Status}}"]
        rc, out, err = util.run(["docker", "restart"] + extra, timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("usage: ntk docker restart ...")
        return 2

def rm(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk docker rm ...")
            return 2
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        extra = list(args)
        if 'rm' == "healthcheck":
            extra = [args[0], "--format", "{{.State.Health.Status}}"]
        rc, out, err = util.run(["docker", "rm"] + extra, timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("usage: ntk docker rm ...")
        return 2

def rmi(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk docker rmi ...")
            return 2
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        extra = list(args)
        if 'rmi' == "healthcheck":
            extra = [args[0], "--format", "{{.State.Health.Status}}"]
        rc, out, err = util.run(["docker", "rmi"] + extra, timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("usage: ntk docker rmi ...")
        return 2

def top(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk docker top ...")
            return 2
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        extra = list(args)
        if 'top' == "healthcheck":
            extra = [args[0], "--format", "{{.State.Health.Status}}"]
        rc, out, err = util.run(["docker", "top"] + extra, timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("usage: ntk docker top ...")
        return 2

def port(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk docker port ...")
            return 2
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        extra = list(args)
        if 'port' == "healthcheck":
            extra = [args[0], "--format", "{{.State.Health.Status}}"]
        rc, out, err = util.run(["docker", "port"] + extra, timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("usage: ntk docker port ...")
        return 2

def disk_usage(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['system', 'df'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

def container_ips(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['ps', '-q'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

def compose_ps(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['compose', 'ps'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

def running_count(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['ps', '-q'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

def image_count(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['images', '-q'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

def dangling_images(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['images', '-f', 'dangling=true'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

def build(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk docker build ...")
            return 2
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        extra = list(args)
        if 'build' == "healthcheck":
            extra = [args[0], "--format", "{{.State.Health.Status}}"]
        rc, out, err = util.run(["docker", "build"] + extra, timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("usage: ntk docker build ...")
        return 2

def tag(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk docker tag ...")
            return 2
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        extra = list(args)
        if 'tag' == "healthcheck":
            extra = [args[0], "--format", "{{.State.Health.Status}}"]
        rc, out, err = util.run(["docker", "tag"] + extra, timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("usage: ntk docker tag ...")
        return 2

def size_by_image(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['images'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

def healthcheck(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk docker healthcheck ...")
            return 2
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        extra = list(args)
        if 'healthcheck' == "healthcheck":
            extra = [args[0], "--format", "{{.State.Health.Status}}"]
        rc, out, err = util.run(["docker", "inspect"] + extra, timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("usage: ntk docker healthcheck ...")
        return 2

def exec_hint(args):
    """Tool."""
    try:
        if not args:
            util.err("usage: ntk docker exec-hint ...")
            return 2
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        extra = list(args)
        if 'exec_hint' == "healthcheck":
            extra = [args[0], "--format", "{{.State.Health.Status}}"]
        rc, out, err = util.run(["docker", "exec"] + extra, timeout=60)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("usage: ntk docker exec-hint ...")
        return 2

def version(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['version'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

def info(args):
    """Tool."""
    try:
        if util.which("docker") is None:
            util.warn("needs docker")
            return 1
        rc, out, err = util.run(["docker"] + ['info'], timeout=30)
        print(out or err, end="")
        return rc
    except Exception:
        util.err("docker command failed")
        return 2

COMMANDS = {
    'ps': ps,
    'ps-all': ps_all,
    'images': images,
    'pull': pull,
    'stats': stats,
    'logs': logs,
    'inspect': inspect,
    'volumes': volumes,
    'networks': networks,
    'prune-preview': prune_preview,
    'prune': prune,
    'stop': stop,
    'start': start,
    'restart': restart,
    'rm': rm,
    'rmi': rmi,
    'top': top,
    'port': port,
    'disk-usage': disk_usage,
    'container-ips': container_ips,
    'compose-ps': compose_ps,
    'running-count': running_count,
    'image-count': image_count,
    'dangling-images': dangling_images,
    'build': build,
    'tag': tag,
    'size-by-image': size_by_image,
    'healthcheck': healthcheck,
    'exec-hint': exec_hint,
    'version': version,
    'info': info,
}
