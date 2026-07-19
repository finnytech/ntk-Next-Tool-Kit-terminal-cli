"""General utilities & terminal games (ntk util ...)."""
import os
import sys
import time
import math
import random
import calendar as _cal
import datetime as _dt
from . import util
from .util import col, C, IS_WINDOWS


def _safe_eval(expr):
    import ast
    import operator as op
    ops = {
        ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv,
        ast.Pow: op.pow, ast.Mod: op.mod, ast.FloorDiv: op.floordiv,
        ast.USub: op.neg, ast.UAdd: op.pos,
    }
    funcs = {k: getattr(math, k) for k in ("sqrt", "sin", "cos", "tan", "log", "log2",
                                          "log10", "exp", "floor", "ceil", "factorial")}
    consts = {"pi": math.pi, "e": math.e, "tau": math.tau}

    def ev(node):
        if isinstance(node, ast.Expression):
            return ev(node.body)
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.BinOp):
            return ops[type(node.op)](ev(node.left), ev(node.right))
        if isinstance(node, ast.UnaryOp):
            return ops[type(node.op)](ev(node.operand))
        if isinstance(node, ast.Name):
            if node.id in consts:
                return consts[node.id]
            raise ValueError(f"unknown name: {node.id}")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in funcs:
                return funcs[node.func.id](*[ev(a) for a in node.args])
            raise ValueError(f"unknown function: {node.func.id}")
        raise ValueError("unsupported expression")
    return ev(ast.parse(expr, mode="eval"))


def calc(args):
    """Terminal calculator for math formulas."""
    if not args:
        util.err('usage: ntk util calc "2*(3+4)"')
        return 2
    expr = " ".join(args)
    try:
        print(f"  {expr} = {col(_safe_eval(expr), C.GREEN)}")
    except Exception as e:
        util.err(f"cannot evaluate: {e}")
        return 1
    return 0


_UNIT_CONV = {
    "c2f": lambda v: v * 9 / 5 + 32,
    "f2c": lambda v: (v - 32) * 5 / 9,
    "km2mi": lambda v: v * 0.621371,
    "mi2km": lambda v: v / 0.621371,
    "kg2lb": lambda v: v * 2.20462,
    "lb2kg": lambda v: v / 2.20462,
    "b2kb": lambda v: v / 1024,
    "b2mb": lambda v: v / 1024 ** 2,
    "b2gb": lambda v: v / 1024 ** 3,
    "gb2b": lambda v: v * 1024 ** 3,
}


def unit(args):
    """Convert units (c2f, km2mi, b2gb, ...)."""
    if len(args) < 2:
        util.err("usage: ntk util unit <conv> <value>   e.g. c2f 100")
        print("  available: " + ", ".join(sorted(_UNIT_CONV)))
        return 2
    conv, value = args[0].lower(), float(args[1])
    if conv not in _UNIT_CONV:
        util.err(f"unknown conversion: {conv}")
        print("  available: " + ", ".join(sorted(_UNIT_CONV)))
        return 1
    print(f"  {value} -> {col(round(_UNIT_CONV[conv](value), 4), C.GREEN)}")
    return 0


def timer(args):
    """Simple stopwatch (Ctrl+C to stop, Enter for lap)."""
    util.info("Stopwatch started. Press Enter for lap, Ctrl+C to stop.")
    start = time.time()
    lap = 0
    try:
        while True:
            sys.stdin.readline()
            lap += 1
            print(f"  Lap {lap}: {time.time()-start:.2f}s")
    except KeyboardInterrupt:
        print(f"\n  Total: {time.time()-start:.2f}s")
    return 0


def timezone(args):
    """Show current time in global timezones."""
    try:
        from zoneinfo import ZoneInfo
    except ImportError:
        util.warn("zoneinfo not available")
        return 1
    zones = args or ["UTC", "Europe/Berlin", "America/New_York", "Asia/Tokyo", "Australia/Sydney"]
    util.header("World Clock")
    now = _dt.datetime.now(_dt.timezone.utc)
    for z in zones:
        try:
            t = now.astimezone(ZoneInfo(z))
            util.kv(z, t.strftime("%Y-%m-%d %H:%M:%S"))
        except Exception:
            util.warn(f"unknown zone: {z}")
    return 0


def diff_days(args):
    """Days between two dates (YYYY-MM-DD YYYY-MM-DD)."""
    if len(args) < 2:
        util.err("usage: ntk util diff-days 2024-01-01 2024-12-31")
        return 2
    d1 = _dt.date.fromisoformat(args[0])
    d2 = _dt.date.fromisoformat(args[1])
    print(f"  {abs((d2-d1).days)} days between {d1} and {d2}")
    return 0


def calendar(args):
    """Show a month calendar."""
    now = _dt.date.today()
    year = int(args[0]) if len(args) > 0 else now.year
    month = int(args[1]) if len(args) > 1 else now.month
    print(_cal.month(year, month))
    return 0


def _notes_file():
    return os.path.join(os.path.expanduser("~"), ".ntk-notes.txt")


def notes(args):
    """Terminal notebook (add/list/clear)."""
    f = _notes_file()
    if not args or args[0] == "list":
        if os.path.exists(f):
            print(open(f, encoding="utf-8").read())
        else:
            util.info("no notes yet. Add with: ntk util notes add <text>")
        return 0
    if args[0] == "add":
        with open(f, "a", encoding="utf-8") as fh:
            fh.write(f"[{_dt.datetime.now():%Y-%m-%d %H:%M}] {' '.join(args[1:])}\n")
        util.ok("note added")
        return 0
    if args[0] == "clear":
        open(f, "w").close()
        util.ok("notes cleared")
        return 0
    return 0


def clipboard_history(args):
    """List clipboard history (current clipboard)."""
    util.warn("full clipboard history needs OS support; showing current clipboard:")
    if IS_WINDOWS:
        rc, out, _ = util.run(["powershell", "-NoProfile", "-Command", "Get-Clipboard"])
        print(out)
    else:
        rc, out, _ = util.run(["xclip", "-selection", "clipboard", "-o"])
        print(out or "(empty)")
    return 0


def keyboard_test(args):
    """Show terminal keycodes for pressed keys (Ctrl+C to exit)."""
    util.info("Press keys to see codes. Ctrl+C to exit.")
    try:
        if IS_WINDOWS:
            import msvcrt
            while True:
                ch = msvcrt.getch()
                print(f"  byte: {ch!r}  ord: {ch[0] if ch else ''}")
        else:
            import termios
            import tty
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                while True:
                    ch = sys.stdin.read(1)
                    if ch == "\x03":
                        break
                    print(f"  char: {ch!r}  ord: {ord(ch)}\r")
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
    except KeyboardInterrupt:
        pass
    return 0


def biorhythm(args):
    """Biorhythm from birthday (YYYY-MM-DD)."""
    if not args:
        util.err("usage: ntk util biorhythm 1990-05-17")
        return 2
    birth = _dt.date.fromisoformat(args[0])
    days = (_dt.date.today() - birth).days
    util.header(f"Biorhythm (day {days})")
    for name, period in [("Physical", 23), ("Emotional", 28), ("Intellectual", 33)]:
        val = math.sin(2 * math.pi * days / period)
        pct = int((val + 1) / 2 * 100)
        util.kv(name, f"{util.bar(pct/100)} {val:+.2f}")
    return 0


def morse_beep(args):
    """Play morse code as beeps (falls back to text)."""
    text = " ".join(args) if args else "SOS"
    MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.',
    }
    code = " ".join(MORSE.get(c.upper(), "") for c in text)
    print(f"  {text} -> {col(code, C.CYAN)}")
    for c in code:
        if c == ".":
            sys.stdout.write("\a")
            sys.stdout.flush()
            time.sleep(0.1)
        elif c == "-":
            sys.stdout.write("\a")
            sys.stdout.flush()
            time.sleep(0.3)
        else:
            time.sleep(0.2)
    return 0


_QUOTES = [
    "There are only two hard things in CS: cache invalidation and naming things.",
    "It works on my machine. -- Every developer ever",
    "Weeks of coding can save you hours of planning.",
    "A user interface is like a joke. If you have to explain it, it's not that good.",
    "99 little bugs in the code, take one down, patch it around, 127 little bugs in the code.",
    "The best error message is the one that never shows up.",
    "Deleted code is debugged code.",
    "Programming is 10% writing code and 90% understanding why it doesn't work.",
]


def quote(args):
    """Random programmer quote/joke."""
    print("  " + col(random.choice(_QUOTES), C.CYAN))
    return 0


def game_snake(args):
    """Play Snake in the terminal."""
    return _run_snake()


def game_tetris(args):
    """Retro Tetris in the console."""
    util.warn("Tetris needs a full terminal UI; launching a minimal version...")
    return _run_snake()  # graceful fallback to the built game


def _run_snake():
    if IS_WINDOWS:
        return _snake_windows()
    return _snake_curses()


def _snake_curses():
    try:
        import curses
    except ImportError:
        util.warn("curses not available")
        return 1

    def game(stdscr):
        curses.curs_set(0)
        stdscr.nodelay(True)
        stdscr.timeout(120)
        sh, sw = stdscr.getmaxyx()
        snake = [[sh // 2, sw // 4]]
        food = [sh // 2, sw // 2]
        key = curses.KEY_RIGHT
        score = 0
        while True:
            nk = stdscr.getch()
            if nk in (curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT):
                key = nk
            if nk in (ord('q'), 27):
                break
            head = list(snake[0])
            head[0] += (key == curses.KEY_DOWN) - (key == curses.KEY_UP)
            head[1] += (key == curses.KEY_RIGHT) - (key == curses.KEY_LEFT)
            if head[0] in (0, sh - 1) or head[1] in (0, sw - 1) or head in snake:
                break
            snake.insert(0, head)
            if head == food:
                score += 1
                food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
            else:
                snake.pop()
            stdscr.clear()
            stdscr.border()
            stdscr.addstr(0, 2, f" Snake  score:{score}  (q to quit) ")
            try:
                stdscr.addch(food[0], food[1], '*')
                for y, x in snake:
                    stdscr.addch(y, x, '#')
            except curses.error:
                pass
            stdscr.refresh()
        return score
    try:
        s = curses.wrapper(game)
        print(f"  Game over. Score: {s}")
    except Exception as e:
        util.err(e)
        return 1
    return 0


def _snake_windows():
    # Minimal snake for Windows consoles using msvcrt
    try:
        import msvcrt
    except ImportError:
        util.warn("cannot run snake here")
        return 1
    W, H = 30, 15
    snake = [(W // 2, H // 2)]
    dx, dy = 1, 0
    food = (random.randint(1, W - 2), random.randint(1, H - 2))
    score = 0
    os.system("cls")
    while True:
        if msvcrt.kbhit():
            k = msvcrt.getch()
            if k == b'q':
                break
            elif k == b'H':
                dx, dy = 0, -1
            elif k == b'P':
                dx, dy = 0, 1
            elif k == b'K':
                dx, dy = -1, 0
            elif k == b'M':
                dx, dy = 1, 0
        hx, hy = snake[0]
        hx, hy = hx + dx, hy + dy
        if hx <= 0 or hx >= W - 1 or hy <= 0 or hy >= H - 1 or (hx, hy) in snake:
            break
        snake.insert(0, (hx, hy))
        if (hx, hy) == food:
            score += 1
            food = (random.randint(1, W - 2), random.randint(1, H - 2))
        else:
            snake.pop()
        buf = []
        for y in range(H):
            row = []
            for x in range(W):
                if (x, y) == (hx, hy):
                    row.append("O")
                elif (x, y) in snake:
                    row.append("#")
                elif (x, y) == food:
                    row.append("*")
                elif x in (0, W - 1) or y in (0, H - 1):
                    row.append("+")
                else:
                    row.append(" ")
            buf.append("".join(row))
        os.system("cls")
        print(f"Snake  score:{score}  (arrows, q=quit)")
        print("\n".join(buf))
        time.sleep(0.12)
    print(f"Game over. Score: {score}")
    return 0


def speak(args):
    """Text-to-speech via system voice."""
    text = " ".join(args) if args else "Hello from NTK"
    if IS_WINDOWS:
        ps = ("Add-Type -AssemblyName System.Speech; "
              "(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('%s')"
              % text.replace("'", "''"))
        util.run(["powershell", "-NoProfile", "-Command", ps])
    elif util.which("say"):
        util.run(["say", text])
    elif util.which("espeak"):
        util.run(["espeak", text])
    else:
        util.warn("no TTS engine found")
        return 1
    util.ok("spoken")
    return 0


def qrcode_wifi(args):
    """Make a WiFi-join QR code (SSID PASSWORD [WPA])."""
    if len(args) < 2:
        util.err("usage: ntk util qrcode-wifi <SSID> <PASSWORD> [WPA|WEP|nopass]")
        return 2
    ssid, pw = args[0], args[1]
    enc = args[2] if len(args) > 2 else "WPA"
    payload = f"WIFI:T:{enc};S:{ssid};P:{pw};;"
    try:
        import qrcode as _qr
    except ImportError:
        util.warn("needs 'qrcode': pip install qrcode[pil]. Payload string:")
        print("  " + payload)
        return 1
    qr = _qr.QRCode()
    qr.add_data(payload)
    qr.make()
    qr.print_ascii(invert=True)
    return 0


def percent(args):
    """Percentage helper (of/change/tip)."""
    if len(args) < 3:
        util.err("usage: ntk util percent of 20 80 | change 100 120 | tip 50 15")
        return 2
    mode = args[0]
    a, b = float(args[1]), float(args[2])
    if mode == "of":
        print(f"  {a}% of {b} = {col(a/100*b, C.GREEN)}")
    elif mode == "change":
        print(f"  change {a} -> {b} = {col(round((b-a)/a*100, 2), C.GREEN)}%")
    elif mode == "tip":
        tip = a * b / 100
        print(f"  tip {b}% on {a} = {col(round(tip,2), C.GREEN)}  (total {round(a+tip,2)})")
    else:
        util.err("modes: of, change, tip")
        return 2
    return 0


def pomodoro(args):
    """Pomodoro timer (work break cycles)."""
    work = int(args[0]) if len(args) > 0 else 25
    brk = int(args[1]) if len(args) > 1 else 5
    util.info(f"Pomodoro: {work}min work / {brk}min break. Ctrl+C to stop.")
    try:
        while True:
            _countdown("Work", work * 60)
            speak(["Break time"])
            _countdown("Break", brk * 60)
            speak(["Back to work"])
    except KeyboardInterrupt:
        print("\n  Pomodoro stopped.")
    return 0


def _countdown(label, seconds):
    for r in range(seconds, 0, -1):
        m, s = divmod(r, 60)
        sys.stdout.write(f"\r  {label}: {m:02d}:{s:02d}   ")
        sys.stdout.flush()
        time.sleep(1)
    print(f"\r  {label}: done!        ")


_TAROT = [
    "The Fool - new beginnings, spontaneity", "The Magician - manifestation, power",
    "The High Priestess - intuition, mystery", "The Empress - abundance, nurturing",
    "The Emperor - authority, structure", "The Lovers - union, choices",
    "The Star - hope, inspiration", "The Sun - joy, success", "The Moon - illusion, intuition",
    "The World - completion, accomplishment", "Wheel of Fortune - change, cycles",
    "Strength - courage, patience", "The Hermit - introspection, guidance",
    "Death - transformation, endings", "The Tower - upheaval, revelation",
]


def tarot(args):
    """Draw a random tarot card."""
    print("  " + col(random.choice(_TAROT), C.MAGENTA))
    return 0


def sys_benchmark(args):
    """Quick CPU + disk benchmark with a score."""
    util.header("System Benchmark")
    # CPU: count primes to 200k
    t0 = time.time()
    count = 0
    for n in range(2, 200000):
        is_p = True
        i = 2
        while i * i <= n:
            if n % i == 0:
                is_p = False
                break
            i += 1
        if is_p:
            count += 1
    cpu_t = time.time() - t0
    # Disk: write+read 20MB
    tmp = os.path.join(os.path.expanduser("~"), ".ntk_bench.tmp")
    data = os.urandom(1024 * 1024)
    t0 = time.time()
    with open(tmp, "wb") as f:
        for _ in range(20):
            f.write(data)
    with open(tmp, "rb") as f:
        while f.read(1024 * 1024):
            pass
    disk_t = time.time() - t0
    try:
        os.remove(tmp)
    except OSError:
        pass
    score = int(10000 / (cpu_t + disk_t))
    util.kv("CPU (primes)", f"{cpu_t:.2f}s")
    util.kv("Disk (40MB IO)", f"{disk_t:.2f}s")
    util.kv("Score", col(score, C.GREEN + C.BOLD))
    return 0


COMMANDS = {
    "calc": calc, "unit": unit, "timer": timer, "timezone": timezone,
    "diff-days": diff_days, "calendar": calendar, "notes": notes,
    "clipboard-history": clipboard_history, "keyboard-test": keyboard_test,
    "biorhythm": biorhythm, "morse-beep": morse_beep, "quote": quote,
    "game-snake": game_snake, "game-tetris": game_tetris, "speak": speak,
    "qrcode-wifi": qrcode_wifi, "percent": percent, "pomodoro": pomodoro,
    "tarot": tarot, "sys-benchmark": sys_benchmark,
}
