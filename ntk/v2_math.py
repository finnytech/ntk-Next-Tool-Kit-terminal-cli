"""Math tools (ntk math ...)."""
import math
import random
import statistics as _st
from . import util
from .util import col, C


def _nums(args):
    return [float(x) for x in args]


def calc(args):
    """Evaluate a math expression, e.g. 2*(3+4)."""
    if not args:
        util.err("usage: ntk math calc <expr>")
        return 2
    expr = " ".join(args)
    allowed = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
    allowed.update({"abs": abs, "round": round, "min": min, "max": max})
    try:
        print(f"  {expr} = {eval(expr, {'__builtins__': {}}, allowed)}")
        return 0
    except Exception as e:
        util.err(f"invalid expression: {e}")
        return 2


def _agg(args, fn, name):
    try:
        print(f"  {name} = {fn(_nums(args))}")
        return 0
    except Exception as e:
        util.err(f"usage: ntk math {name} <numbers...> ({e})")
        return 2


def mean(args):
    """Arithmetic mean of numbers."""
    return _agg(args, _st.mean, "mean")


def median(args):
    """Median of numbers."""
    return _agg(args, _st.median, "median")


def mode(args):
    """Most common value."""
    return _agg(args, _st.mode, "mode")


def stdev(args):
    """Standard deviation."""
    return _agg(args, lambda v: _st.pstdev(v), "stdev")


def variance(args):
    """Variance."""
    return _agg(args, lambda v: _st.pvariance(v), "variance")


def total(args):
    """Sum of numbers."""
    return _agg(args, sum, "sum")


def product(args):
    """Product of numbers."""
    return _agg(args, lambda v: math.prod(v), "product")


def minimum(args):
    """Minimum value."""
    return _agg(args, min, "min")


def maximum(args):
    """Maximum value."""
    return _agg(args, max, "max")


def rng(args):
    """Range (max-min)."""
    return _agg(args, lambda v: max(v) - min(v), "range")


def factorial(args):
    """Factorial of n."""
    try:
        print(f"  {math.factorial(int(args[0]))}")
        return 0
    except Exception:
        util.err("usage: ntk math factorial <n>")
        return 2


def fibonacci(args):
    """First n Fibonacci numbers."""
    try:
        n = int(args[0])
    except Exception:
        util.err("usage: ntk math fibonacci <n>")
        return 2
    seq, a, b = [], 0, 1
    for _ in range(max(0, n)):
        seq.append(a)
        a, b = b, a + b
    print("  " + " ".join(map(str, seq)))
    return 0


def _is_prime(n):
    if n < 2:
        return False
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def prime_check(args):
    """Check if a number is prime."""
    try:
        n = int(args[0])
    except Exception:
        util.err("usage: ntk math prime-check <n>")
        return 2
    print(f"  {n} is {'prime' if _is_prime(n) else 'not prime'}")
    return 0


def primes_upto(args):
    """List primes up to n."""
    try:
        n = int(args[0])
    except Exception:
        util.err("usage: ntk math primes-upto <n>")
        return 2
    print("  " + " ".join(str(x) for x in range(2, n + 1) if _is_prime(x)))
    return 0


def gcd(args):
    """Greatest common divisor."""
    try:
        print(f"  {math.gcd(*[int(x) for x in args])}")
        return 0
    except Exception:
        util.err("usage: ntk math gcd <a> <b> ...")
        return 2


def lcm(args):
    """Least common multiple."""
    try:
        print(f"  {math.lcm(*[int(x) for x in args])}")
        return 0
    except Exception:
        util.err("usage: ntk math lcm <a> <b> ...")
        return 2


def is_square(args):
    """Check if a number is a perfect square."""
    try:
        n = int(args[0])
        r = math.isqrt(n)
        print(f"  {n} is {'a' if r * r == n else 'not a'} perfect square")
        return 0
    except Exception:
        util.err("usage: ntk math is-square <n>")
        return 2


def sqrt(args):
    """Square root."""
    try:
        print(f"  {math.sqrt(float(args[0]))}")
        return 0
    except Exception:
        util.err("usage: ntk math sqrt <n>")
        return 2


def power(args):
    """x raised to y."""
    try:
        print(f"  {float(args[0]) ** float(args[1])}")
        return 0
    except Exception:
        util.err("usage: ntk math pow <x> <y>")
        return 2


def logn(args):
    """Logarithm (base optional, default e)."""
    try:
        x = float(args[0])
        base = float(args[1]) if len(args) > 1 else math.e
        print(f"  {math.log(x, base)}")
        return 0
    except Exception:
        util.err("usage: ntk math log <x> [base]")
        return 2


def percent(args):
    """x is what percent of y."""
    try:
        x, y = float(args[0]), float(args[1])
        print(f"  {x} is {x/y*100:.2f}% of {y}")
        return 0
    except Exception:
        util.err("usage: ntk math percent <x> <y>")
        return 2


def percent_change(args):
    """Percent change from a to b."""
    try:
        a, b = float(args[0]), float(args[1])
        print(f"  {(b-a)/a*100:+.2f}%")
        return 0
    except Exception:
        util.err("usage: ntk math percent-change <old> <new>")
        return 2


def round_to(args):
    """Round n to d decimals."""
    try:
        n = float(args[0])
        d = int(args[1]) if len(args) > 1 else 0
        print(f"  {round(n, d)}")
        return 0
    except Exception:
        util.err("usage: ntk math round-to <n> [decimals]")
        return 2


def base_convert(args):
    """Convert integer between bases: n from to."""
    try:
        n, frm, to = args[0], int(args[1]), int(args[2])
        val = int(str(n), frm)
        digits = "0123456789abcdefghijklmnopqrstuvwxyz"
        if val == 0:
            out = "0"
        else:
            out = ""
            v = val
            while v:
                out = digits[v % to] + out
                v //= to
        print(f"  {out}")
        return 0
    except Exception:
        util.err("usage: ntk math base-convert <n> <from> <to>")
        return 2


def to_hex(args):
    """Decimal to hexadecimal."""
    try:
        print(f"  {hex(int(args[0]))}")
        return 0
    except Exception:
        util.err("usage: ntk math hex <n>")
        return 2


def to_bin(args):
    """Decimal to binary."""
    try:
        print(f"  {bin(int(args[0]))}")
        return 0
    except Exception:
        util.err("usage: ntk math bin <n>")
        return 2


def to_oct(args):
    """Decimal to octal."""
    try:
        print(f"  {oct(int(args[0]))}")
        return 0
    except Exception:
        util.err("usage: ntk math oct <n>")
        return 2


_ROMAN = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
          (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
          (5, "V"), (4, "IV"), (1, "I")]


def roman(args):
    """Integer to Roman numeral."""
    try:
        n = int(args[0])
        if not (0 < n < 4000):
            raise ValueError
        out = ""
        for v, sym in _ROMAN:
            while n >= v:
                out += sym
                n -= v
        print(f"  {out}")
        return 0
    except Exception:
        util.err("usage: ntk math roman <1-3999>")
        return 2


def from_roman(args):
    """Roman numeral to integer."""
    if not args:
        util.err("usage: ntk math from-roman <ROMAN>")
        return 2
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = args[0].upper()
    total_v = 0
    prev = 0
    try:
        for ch in reversed(s):
            v = vals[ch]
            total_v += v if v >= prev else -v
            prev = v
        print(f"  {total_v}")
        return 0
    except KeyError:
        util.err("invalid Roman numeral")
        return 2


def quadratic(args):
    """Solve ax^2+bx+c=0: a b c."""
    try:
        a, b, c = float(args[0]), float(args[1]), float(args[2])
        disc = b * b - 4 * a * c
        if disc < 0:
            print("  no real roots")
        else:
            r = math.sqrt(disc)
            print(f"  x1={(-b+r)/(2*a)}  x2={(-b-r)/(2*a)}")
        return 0
    except Exception:
        util.err("usage: ntk math quadratic <a> <b> <c>")
        return 2


def deg_to_rad(args):
    """Degrees to radians."""
    try:
        print(f"  {math.radians(float(args[0]))}")
        return 0
    except Exception:
        util.err("usage: ntk math deg-to-rad <deg>")
        return 2


def rad_to_deg(args):
    """Radians to degrees."""
    try:
        print(f"  {math.degrees(float(args[0]))}")
        return 0
    except Exception:
        util.err("usage: ntk math rad-to-deg <rad>")
        return 2


def random_int(args):
    """Random integer in [a,b]."""
    try:
        a, b = int(args[0]), int(args[1])
        print(f"  {random.randint(a, b)}")
        return 0
    except Exception:
        util.err("usage: ntk math random-int <a> <b>")
        return 2


def dice(args):
    """Roll dice, e.g. 2d6."""
    spec = args[0] if args else "1d6"
    try:
        n, sides = spec.lower().split("d")
        n, sides = int(n or 1), int(sides)
        rolls = [random.randint(1, sides) for _ in range(n)]
        print(f"  {rolls} = {sum(rolls)}")
        return 0
    except Exception:
        util.err("usage: ntk math dice <NdM>  e.g. 2d6")
        return 2


def combinations(args):
    """Combinations C(n,r)."""
    try:
        print(f"  {math.comb(int(args[0]), int(args[1]))}")
        return 0
    except Exception:
        util.err("usage: ntk math combinations <n> <r>")
        return 2


def permutations(args):
    """Permutations P(n,r)."""
    try:
        print(f"  {math.perm(int(args[0]), int(args[1]))}")
        return 0
    except Exception:
        util.err("usage: ntk math permutations <n> <r>")
        return 2


def average_list(args):
    """Average of a comma list."""
    try:
        vals = [float(x) for x in " ".join(args).replace(",", " ").split()]
        print(f"  {sum(vals)/len(vals)}")
        return 0
    except Exception:
        util.err("usage: ntk math average-list <n1,n2,...>")
        return 2


def clamp(args):
    """Clamp n to [lo,hi]."""
    try:
        n, lo, hi = float(args[0]), float(args[1]), float(args[2])
        print(f"  {max(lo, min(hi, n))}")
        return 0
    except Exception:
        util.err("usage: ntk math clamp <n> <lo> <hi>")
        return 2


def abs_val(args):
    """Absolute value."""
    try:
        print(f"  {abs(float(args[0]))}")
        return 0
    except Exception:
        util.err("usage: ntk math abs <n>")
        return 2


COMMANDS = {
    "calc": calc, "mean": mean, "median": median, "mode": mode, "stdev": stdev,
    "variance": variance, "sum": total, "product": product, "min": minimum,
    "max": maximum, "range": rng, "factorial": factorial, "fibonacci": fibonacci,
    "prime-check": prime_check, "primes-upto": primes_upto, "gcd": gcd, "lcm": lcm,
    "is-square": is_square, "sqrt": sqrt, "pow": power, "log": logn, "percent": percent,
    "percent-change": percent_change, "round-to": round_to, "base-convert": base_convert,
    "hex": to_hex, "bin": to_bin, "oct": to_oct, "roman": roman, "from-roman": from_roman,
    "quadratic": quadratic, "deg-to-rad": deg_to_rad, "rad-to-deg": rad_to_deg,
    "random-int": random_int, "dice": dice, "combinations": combinations,
    "permutations": permutations, "average-list": average_list, "clamp": clamp, "abs": abs_val,
}
