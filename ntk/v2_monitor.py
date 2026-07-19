"""NTK v2 monitor tools."""
import os
import time
from . import util

def cpu(args):
    """cpu tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("cpu:", value)
        else:
            print("cpu: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor cpu [value]")
        return 2

def cpu_per_core(args):
    """cpu-per-core tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("cpu-per-core:", value)
        else:
            print("cpu-per-core: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor cpu-per-core [value]")
        return 2

def mem(args):
    """mem tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("mem:", value)
        else:
            print("mem: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor mem [value]")
        return 2

def disk_io(args):
    """disk-io tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("disk-io:", value)
        else:
            print("disk-io: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor disk-io [value]")
        return 2

def net_io(args):
    """net-io tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("net-io:", value)
        else:
            print("net-io: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor net-io [value]")
        return 2

def processes(args):
    """processes tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("processes:", value)
        else:
            print("processes: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor processes [value]")
        return 2

def top_mem(args):
    """top-mem tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("top-mem:", value)
        else:
            print("top-mem: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor top-mem [value]")
        return 2

def load(args):
    """load tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("load:", value)
        else:
            print("load: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor load [value]")
        return 2

def temps(args):
    """temps tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("temps:", value)
        else:
            print("temps: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor temps [value]")
        return 2

def battery(args):
    """battery tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("battery:", value)
        else:
            print("battery: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor battery [value]")
        return 2

def uptime(args):
    """uptime tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("uptime:", value)
        else:
            print("uptime: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor uptime [value]")
        return 2

def disk_usage(args):
    """disk-usage tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("disk-usage:", value)
        else:
            print("disk-usage: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor disk-usage [value]")
        return 2

def connections_count(args):
    """connections-count tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("connections-count:", value)
        else:
            print("connections-count: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor connections-count [value]")
        return 2

def threads(args):
    """threads tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("threads:", value)
        else:
            print("threads: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor threads [value]")
        return 2

def swap(args):
    """swap tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("swap:", value)
        else:
            print("swap: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor swap [value]")
        return 2

def gpu(args):
    """gpu tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("gpu:", value)
        else:
            print("gpu: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor gpu [value]")
        return 2

def watch_cpu(args):
    """watch-cpu tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("watch-cpu:", value)
        else:
            print("watch-cpu: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor watch-cpu [value]")
        return 2

def watch_mem(args):
    """watch-mem tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("watch-mem:", value)
        else:
            print("watch-mem: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor watch-mem [value]")
        return 2

def net_speed(args):
    """net-speed tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("net-speed:", value)
        else:
            print("net-speed: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor net-speed [value]")
        return 2

def users_logged(args):
    """users-logged tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("users-logged:", value)
        else:
            print("users-logged: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor users-logged [value]")
        return 2

def boot_time(args):
    """boot-time tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("boot-time:", value)
        else:
            print("boot-time: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor boot-time [value]")
        return 2

def process_count(args):
    """process-count tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("process-count:", value)
        else:
            print("process-count: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor process-count [value]")
        return 2

def cpu_freq(args):
    """cpu-freq tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("cpu-freq:", value)
        else:
            print("cpu-freq: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor cpu-freq [value]")
        return 2

def per_disk_usage(args):
    """per-disk-usage tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("per-disk-usage:", value)
        else:
            print("per-disk-usage: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor per-disk-usage [value]")
        return 2

def listening_ports(args):
    """listening-ports tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("listening-ports:", value)
        else:
            print("listening-ports: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor listening-ports [value]")
        return 2

def memory_percent(args):
    """memory-percent tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("memory-percent:", value)
        else:
            print("memory-percent: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor memory-percent [value]")
        return 2

def disk_percent(args):
    """disk-percent tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("disk-percent:", value)
        else:
            print("disk-percent: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor disk-percent [value]")
        return 2

def top_cpu(args):
    """top-cpu tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("top-cpu:", value)
        else:
            print("top-cpu: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor top-cpu [value]")
        return 2

def io_counters(args):
    """io-counters tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("io-counters:", value)
        else:
            print("io-counters: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor io-counters [value]")
        return 2

def net_counters(args):
    """net-counters tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("net-counters:", value)
        else:
            print("net-counters: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor net-counters [value]")
        return 2

def cpu_times(args):
    """cpu-times tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("cpu-times:", value)
        else:
            print("cpu-times: available")
        return 0
    except Exception:
        util.err("usage: ntk monitor cpu-times [value]")
        return 2

COMMANDS = {
    'cpu': cpu,
    'cpu-per-core': cpu_per_core,
    'mem': mem,
    'disk-io': disk_io,
    'net-io': net_io,
    'processes': processes,
    'top-mem': top_mem,
    'load': load,
    'temps': temps,
    'battery': battery,
    'uptime': uptime,
    'disk-usage': disk_usage,
    'connections-count': connections_count,
    'threads': threads,
    'swap': swap,
    'gpu': gpu,
    'watch-cpu': watch_cpu,
    'watch-mem': watch_mem,
    'net-speed': net_speed,
    'users-logged': users_logged,
    'boot-time': boot_time,
    'process-count': process_count,
    'cpu-freq': cpu_freq,
    'per-disk-usage': per_disk_usage,
    'listening-ports': listening_ports,
    'memory-percent': memory_percent,
    'disk-percent': disk_percent,
    'top-cpu': top_cpu,
    'io-counters': io_counters,
    'net-counters': net_counters,
    'cpu-times': cpu_times,
}
