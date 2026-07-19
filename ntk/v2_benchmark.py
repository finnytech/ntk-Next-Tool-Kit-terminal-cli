"""NTK v2 benchmark tools."""
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
        util.err("usage: ntk benchmark cpu [value]")
        return 2

def memory(args):
    """memory tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("memory:", value)
        else:
            print("memory: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark memory [value]")
        return 2

def disk_write(args):
    """disk-write tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("disk-write:", value)
        else:
            print("disk-write: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark disk-write [value]")
        return 2

def disk_read(args):
    """disk-read tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("disk-read:", value)
        else:
            print("disk-read: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark disk-read [value]")
        return 2

def hash_speed(args):
    """hash-speed tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("hash-speed:", value)
        else:
            print("hash-speed: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark hash-speed [value]")
        return 2

def json_parse_speed(args):
    """json-parse-speed tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("json-parse-speed:", value)
        else:
            print("json-parse-speed: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark json-parse-speed [value]")
        return 2

def sort_speed(args):
    """sort-speed tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("sort-speed:", value)
        else:
            print("sort-speed: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark sort-speed [value]")
        return 2

def prime_speed(args):
    """prime-speed tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("prime-speed:", value)
        else:
            print("prime-speed: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark prime-speed [value]")
        return 2

def int_ops(args):
    """int-ops tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("int-ops:", value)
        else:
            print("int-ops: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark int-ops [value]")
        return 2

def float_ops(args):
    """float-ops tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("float-ops:", value)
        else:
            print("float-ops: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark float-ops [value]")
        return 2

def string_ops(args):
    """string-ops tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("string-ops:", value)
        else:
            print("string-ops: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark string-ops [value]")
        return 2

def list_ops(args):
    """list-ops tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("list-ops:", value)
        else:
            print("list-ops: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark list-ops [value]")
        return 2

def dict_ops(args):
    """dict-ops tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("dict-ops:", value)
        else:
            print("dict-ops: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark dict-ops [value]")
        return 2

def regex_speed(args):
    """regex-speed tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("regex-speed:", value)
        else:
            print("regex-speed: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark regex-speed [value]")
        return 2

def fib_bench(args):
    """fib-bench tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("fib-bench:", value)
        else:
            print("fib-bench: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark fib-bench [value]")
        return 2

def random_speed(args):
    """random-speed tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("random-speed:", value)
        else:
            print("random-speed: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark random-speed [value]")
        return 2

def sqlite_insert_speed(args):
    """sqlite-insert-speed tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("sqlite-insert-speed:", value)
        else:
            print("sqlite-insert-speed: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark sqlite-insert-speed [value]")
        return 2

def base64_speed(args):
    """base64-speed tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("base64-speed:", value)
        else:
            print("base64-speed: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark base64-speed [value]")
        return 2

def loop_bench(args):
    """loop-bench tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("loop-bench:", value)
        else:
            print("loop-bench: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark loop-bench [value]")
        return 2

def checksum_speed(args):
    """checksum-speed tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("checksum-speed:", value)
        else:
            print("checksum-speed: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark checksum-speed [value]")
        return 2

def http_speed(args):
    """http-speed tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("http-speed:", value)
        else:
            print("http-speed: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark http-speed [value]")
        return 2

def dns_speed(args):
    """dns-speed tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("dns-speed:", value)
        else:
            print("dns-speed: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark dns-speed [value]")
        return 2

def sort_vs_sorted(args):
    """sort-vs-sorted tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("sort-vs-sorted:", value)
        else:
            print("sort-vs-sorted: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark sort-vs-sorted [value]")
        return 2

def comprehension_speed(args):
    """comprehension-speed tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("comprehension-speed:", value)
        else:
            print("comprehension-speed: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark comprehension-speed [value]")
        return 2

def set_ops(args):
    """set-ops tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("set-ops:", value)
        else:
            print("set-ops: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark set-ops [value]")
        return 2

def startup_self(args):
    """startup-self tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("startup-self:", value)
        else:
            print("startup-self: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark startup-self [value]")
        return 2

def encode_speed(args):
    """encode-speed tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("encode-speed:", value)
        else:
            print("encode-speed: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark encode-speed [value]")
        return 2

def pi_calc(args):
    """pi-calc tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("pi-calc:", value)
        else:
            print("pi-calc: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark pi-calc [value]")
        return 2

def matrix_bench(args):
    """matrix-bench tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("matrix-bench:", value)
        else:
            print("matrix-bench: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark matrix-bench [value]")
        return 2

def allocate_bench(args):
    """allocate-bench tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("allocate-bench:", value)
        else:
            print("allocate-bench: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark allocate-bench [value]")
        return 2

def concat_speed(args):
    """concat-speed tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("concat-speed:", value)
        else:
            print("concat-speed: available")
        return 0
    except Exception:
        util.err("usage: ntk benchmark concat-speed [value]")
        return 2

COMMANDS = {
    'cpu': cpu,
    'memory': memory,
    'disk-write': disk_write,
    'disk-read': disk_read,
    'hash-speed': hash_speed,
    'json-parse-speed': json_parse_speed,
    'sort-speed': sort_speed,
    'prime-speed': prime_speed,
    'int-ops': int_ops,
    'float-ops': float_ops,
    'string-ops': string_ops,
    'list-ops': list_ops,
    'dict-ops': dict_ops,
    'regex-speed': regex_speed,
    'fib-bench': fib_bench,
    'random-speed': random_speed,
    'sqlite-insert-speed': sqlite_insert_speed,
    'base64-speed': base64_speed,
    'loop-bench': loop_bench,
    'checksum-speed': checksum_speed,
    'http-speed': http_speed,
    'dns-speed': dns_speed,
    'sort-vs-sorted': sort_vs_sorted,
    'comprehension-speed': comprehension_speed,
    'set-ops': set_ops,
    'startup-self': startup_self,
    'encode-speed': encode_speed,
    'pi-calc': pi_calc,
    'matrix-bench': matrix_bench,
    'allocate-bench': allocate_bench,
    'concat-speed': concat_speed,
}
