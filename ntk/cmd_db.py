"""Database tools (ntk db ...). SQLite is native; others wrap their CLIs."""
import os
import json
import time
import sqlite3
import random
from . import util
from .util import col, C, run, which


def _open_sqlite(path):
    if not os.path.exists(path):
        util.err(f"file not found: {path}")
        return None
    return sqlite3.connect(path)


def ping(args):
    """Test connection to a DB (sqlite native; others via CLI)."""
    if not args:
        util.err("usage: ntk db ping <sqlite-file | mysql|postgres|redis|mongo host>")
        return 2
    target = args[0]
    if target.endswith((".db", ".sqlite", ".sqlite3")) or os.path.exists(target):
        try:
            con = sqlite3.connect(target)
            con.execute("SELECT 1")
            con.close()
            util.ok(f"SQLite reachable: {target}")
            return 0
        except Exception as e:
            util.err(e)
            return 1
    kind = target.lower()
    cli = {"mysql": "mysql", "postgres": "psql", "redis": "redis-cli", "mongo": "mongosh"}.get(kind)
    if cli and which(cli):
        util.info(f"try: {cli} " + " ".join(args[1:]))
        return 0
    util.warn(f"no native support; install the {kind} client CLI")
    return 1


def redis_cli(args):
    """Simple redis client (wraps redis-cli)."""
    if not which("redis-cli"):
        util.warn("redis-cli not found")
        return 1
    rc, o, e = run(["redis-cli"] + args)
    print(o or e)
    return rc


def sqlite_query(args):
    """Run SQL on a .db/.sqlite file (file 'SQL')."""
    if len(args) < 2:
        util.err('usage: ntk db sqlite-query <file> "SELECT * FROM t"')
        return 2
    con = _open_sqlite(args[0])
    if not con:
        return 1
    try:
        cur = con.execute(" ".join(args[1:]))
        if cur.description:
            cols = [d[0] for d in cur.description]
            rows = cur.fetchall()
            util.table(rows, headers=cols)
        else:
            con.commit()
            util.ok(f"{cur.rowcount} row(s) affected")
    except Exception as e:
        util.err(e)
        return 1
    finally:
        con.close()
    return 0


def dump(args):
    """Export sqlite structure + data as SQL."""
    if not args:
        util.err("usage: ntk db dump <file> [out.sql]")
        return 2
    con = _open_sqlite(args[0])
    if not con:
        return 1
    lines = list(con.iterdump())
    con.close()
    if len(args) > 1:
        open(args[1], "w", encoding="utf-8").write("\n".join(lines))
        util.ok(f"dumped -> {args[1]}")
    else:
        print("\n".join(lines))
    return 0


def import_(args):
    """Import a .sql file into a sqlite db."""
    if len(args) < 2:
        util.err("usage: ntk db import <file.db> <script.sql>")
        return 2
    con = sqlite3.connect(args[0])
    try:
        con.executescript(open(args[1], encoding="utf-8").read())
        con.commit()
        util.ok("imported")
    except Exception as e:
        util.err(e)
        return 1
    finally:
        con.close()
    return 0


def tables(args):
    """List tables of a sqlite db."""
    if not args:
        util.err("usage: ntk db tables <file>")
        return 2
    con = _open_sqlite(args[0])
    if not con:
        return 1
    rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    con.close()
    util.table(rows, headers=["Table"])
    return 0


def schema(args):
    """Show schema of a table (or whole db)."""
    if not args:
        util.err("usage: ntk db schema <file> [table]")
        return 2
    con = _open_sqlite(args[0])
    if not con:
        return 1
    if len(args) > 1:
        rows = con.execute("SELECT sql FROM sqlite_master WHERE name=?", (args[1],)).fetchall()
    else:
        rows = con.execute("SELECT sql FROM sqlite_master WHERE sql NOT NULL").fetchall()
    con.close()
    for (sql,) in rows:
        print(sql + ";\n")
    return 0


def size(args):
    """Show row counts / size per table."""
    if not args:
        util.err("usage: ntk db size <file>")
        return 2
    con = _open_sqlite(args[0])
    if not con:
        return 1
    tabs = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    rows = []
    for (t,) in tabs:
        try:
            n = con.execute(f"SELECT COUNT(*) FROM '{t}'").fetchone()[0]
            rows.append((t, n))
        except Exception:
            rows.append((t, "?"))
    con.close()
    util.table(rows, headers=["Table", "Rows"])
    util.kv("File size", util.human_bytes(os.path.getsize(args[0])))
    return 0


def query_time(args):
    """Measure a query's execution time (+EXPLAIN)."""
    if len(args) < 2:
        util.err('usage: ntk db query-time <file> "SQL"')
        return 2
    con = _open_sqlite(args[0])
    if not con:
        return 1
    sql = " ".join(args[1:])
    try:
        t0 = time.time()
        con.execute(sql).fetchall()
        dt = (time.time() - t0) * 1000
        util.kv("Time", f"{dt:.2f} ms")
        util.info("EXPLAIN QUERY PLAN:")
        for row in con.execute("EXPLAIN QUERY PLAN " + sql):
            print("  " + " ".join(str(c) for c in row))
    except Exception as e:
        util.err(e)
        return 1
    finally:
        con.close()
    return 0


def tunnel(args):
    """Open an SSH tunnel for a DB connection."""
    if len(args) < 2:
        util.err("usage: ntk db tunnel <user@host> <localport:dbhost:dbport>")
        return 2
    if not which("ssh"):
        util.warn("ssh not found")
        return 1
    util.info(f"opening tunnel (Ctrl+C to close): ssh -N -L {args[1]} {args[0]}")
    rc, o, e = run(["ssh", "-N", "-L", args[1], args[0]])
    print(o or e)
    return rc


_FIRST = ["alex", "sam", "jordan", "casey", "riley", "morgan", "taylor", "jamie"]
_LAST = ["smith", "jones", "lee", "brown", "wilson", "taylor", "davis", "muller"]


def fake_fill(args):
    """Insert N fake rows into a sqlite table."""
    if len(args) < 3:
        util.err("usage: ntk db fake-fill <file> <table> <count>")
        return 2
    con = sqlite3.connect(args[0])
    table, n = args[1], int(args[2])
    try:
        cols = [r[1] for r in con.execute(f"PRAGMA table_info('{table}')").fetchall()]
        if not cols:
            util.err("table not found or empty schema")
            return 1
        for i in range(n):
            vals = []
            for c in cols:
                cl = c.lower()
                if "id" == cl:
                    vals.append(None)
                elif "email" in cl:
                    vals.append(f"{random.choice(_FIRST)}@example.com")
                elif "name" in cl:
                    vals.append(f"{random.choice(_FIRST)} {random.choice(_LAST)}")
                elif "age" in cl or "count" in cl or "num" in cl:
                    vals.append(random.randint(1, 99))
                else:
                    vals.append(f"val{i}")
            ph = ",".join("?" * len(cols))
            con.execute(f"INSERT INTO '{table}' VALUES ({ph})", vals)
        con.commit()
        util.ok(f"inserted {n} rows into {table}")
    except Exception as e:
        util.err(e)
        return 1
    finally:
        con.close()
    return 0


def diff(args):
    """Compare schemas of two sqlite databases."""
    if len(args) < 2:
        util.err("usage: ntk db diff <a.db> <b.db>")
        return 2

    def schema_set(p):
        con = sqlite3.connect(p)
        s = set(r[0] for r in con.execute(
            "SELECT sql FROM sqlite_master WHERE sql NOT NULL").fetchall())
        con.close()
        return s
    a, b = schema_set(args[0]), schema_set(args[1])
    for s in a - b:
        print(col("- " + (s or "")[:80], C.RED))
    for s in b - a:
        print(col("+ " + (s or "")[:80], C.GREEN))
    if a == b:
        util.ok("schemas identical")
    return 0


def migrations(args):
    """Create a timestamped migration template."""
    name = args[0] if args else "migration"
    ts = time.strftime("%Y%m%d%H%M%S")
    fn = f"{ts}_{name}.sql"
    open(fn, "w", encoding="utf-8").write(
        f"-- Migration: {name}\n-- Created: {time.ctime()}\n\n-- Up\n\n\n-- Down\n\n")
    util.ok(f"created {fn}")
    return 0


def mongo_stats(args):
    """MongoDB server status (wraps mongosh)."""
    if not which("mongosh"):
        util.warn("mongosh not found")
        return 1
    rc, o, e = run(["mongosh", "--quiet", "--eval", "JSON.stringify(db.serverStatus())"] + args)
    print(o or e)
    return rc


def pg_activity(args):
    """Show active PostgreSQL queries (wraps psql)."""
    if not which("psql"):
        util.warn("psql not found")
        return 1
    rc, o, e = run(["psql"] + args + ["-c",
                   "SELECT pid, state, query FROM pg_stat_activity;"])
    print(o or e)
    return rc


def redis_monitor(args):
    """Stream live redis commands (wraps redis-cli monitor)."""
    if not which("redis-cli"):
        util.warn("redis-cli not found")
        return 1
    rc, o, e = run(["redis-cli", "monitor"])
    print(o or e)
    return rc


def csv_import(args):
    """Import a CSV file into a sqlite table."""
    if len(args) < 3:
        util.err("usage: ntk db csv-import <file.db> <table> <data.csv>")
        return 2
    import csv
    con = sqlite3.connect(args[0])
    with open(args[2], newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        cols = ",".join(f'"{h}"' for h in header)
        con.execute(f'CREATE TABLE IF NOT EXISTS "{args[1]}" ({",".join(h+" TEXT" for h in header)})')
        ph = ",".join("?" * len(header))
        rows = list(reader)
        con.executemany(f'INSERT INTO "{args[1]}" ({cols}) VALUES ({ph})', rows)
    con.commit()
    con.close()
    util.ok(f"imported {len(rows)} rows into {args[1]}")
    return 0


def json_export(args):
    """Export a sqlite table to JSON."""
    if len(args) < 2:
        util.err("usage: ntk db json-export <file.db> <table> [out.json]")
        return 2
    con = _open_sqlite(args[0])
    if not con:
        return 1
    cur = con.execute(f'SELECT * FROM "{args[1]}"')
    cols = [d[0] for d in cur.description]
    data = [dict(zip(cols, row)) for row in cur.fetchall()]
    con.close()
    out = json.dumps(data, indent=2, default=str)
    if len(args) > 2:
        open(args[2], "w", encoding="utf-8").write(out)
        util.ok(f"exported -> {args[2]}")
    else:
        print(out)
    return 0


def backup_cron(args):
    """Generate a cron job + script for DB backups."""
    dbfile = args[0] if args else "app.db"
    print(f"""#!/bin/sh
# ntk db backup script
STAMP=$(date +%Y%m%d-%H%M%S)
cp "{dbfile}" "backup-$STAMP-{os.path.basename(dbfile)}"
find . -name 'backup-*' -mtime +7 -delete

# crontab (daily 02:00):
# 0 2 * * * /path/to/this/script.sh
""")
    return 0


def truncate(args):
    """Empty all tables of a dev sqlite db."""
    if not args:
        util.err("usage: ntk db truncate <file>")
        return 2
    con = sqlite3.connect(args[0])
    tabs = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    for (t,) in tabs:
        con.execute(f'DELETE FROM "{t}"')
    con.commit()
    con.close()
    util.ok(f"truncated {len(tabs)} table(s)")
    return 0


COMMANDS = {
    "ping": ping, "redis-cli": redis_cli, "sqlite-query": sqlite_query,
    "dump": dump, "import": import_, "tables": tables, "schema": schema,
    "size": size, "query-time": query_time, "tunnel": tunnel, "fake-fill": fake_fill,
    "diff": diff, "migrations": migrations, "mongo-stats": mongo_stats,
    "pg-activity": pg_activity, "redis-monitor": redis_monitor,
    "csv-import": csv_import, "json-export": json_export, "backup-cron": backup_cron,
    "truncate": truncate,
}
