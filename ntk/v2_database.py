"""NTK v2 database tools."""
import os
import time
from . import util

def sqlite_query(args):
    """sqlite-query tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-query <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_tables(args):
    """sqlite-tables tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-tables <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_schema(args):
    """sqlite-schema tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-schema <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_count(args):
    """sqlite-count tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-count <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_dump(args):
    """sqlite-dump tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-dump <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_create(args):
    """sqlite-create tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-create <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_size(args):
    """sqlite-size tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-size <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def csv_to_sqlite(args):
    """csv-to-sqlite tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database csv-to-sqlite <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_to_csv(args):
    """sqlite-to-csv tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-to-csv <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_columns(args):
    """sqlite-columns tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-columns <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_indexes(args):
    """sqlite-indexes tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-indexes <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_vacuum(args):
    """sqlite-vacuum tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-vacuum <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_head(args):
    """sqlite-head tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-head <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def json_to_sqlite(args):
    """json-to-sqlite tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database json-to-sqlite <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_pragma(args):
    """sqlite-pragma tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-pragma <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_integrity(args):
    """sqlite-integrity tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-integrity <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_backup(args):
    """sqlite-backup tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-backup <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sql_format(args):
    """sql-format tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sql-format <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def connection_string_parse(args):
    """connection-string-parse tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database connection-string-parse <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def db_url_parse(args):
    """db-url-parse tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database db-url-parse <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_random_row(args):
    """sqlite-random-row tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-random-row <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_distinct(args):
    """sqlite-distinct tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-distinct <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_min_max(args):
    """sqlite-min-max tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-min-max <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_export_json(args):
    """sqlite-export-json tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-export-json <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def rows_count_all(args):
    """rows-count-all tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database rows-count-all <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_drop(args):
    """sqlite-drop tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-drop <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def redis_ping(args):
    """redis-ping tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database redis-ping <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def pg_url_parse(args):
    """pg-url-parse tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database pg-url-parse <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def mysql_url_parse(args):
    """mysql-url-parse tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database mysql-url-parse <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

def sqlite_info(args):
    """sqlite-info tool."""
    try:
        import sqlite3
        path = args[0] if args else ""
        if not path:
            util.err("usage: ntk database sqlite-info <db>")
            return 2
        if path.endswith((".db", ".sqlite")):
            con = sqlite3.connect(path)
            rows = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            print("\n".join(str(row[0]) for row in rows))
            con.close()
        else:
            print(path)
        return 0
    except Exception as exc:
        util.err(str(exc))
        return 2

COMMANDS = {
    'sqlite-query': sqlite_query,
    'sqlite-tables': sqlite_tables,
    'sqlite-schema': sqlite_schema,
    'sqlite-count': sqlite_count,
    'sqlite-dump': sqlite_dump,
    'sqlite-create': sqlite_create,
    'sqlite-size': sqlite_size,
    'csv-to-sqlite': csv_to_sqlite,
    'sqlite-to-csv': sqlite_to_csv,
    'sqlite-columns': sqlite_columns,
    'sqlite-indexes': sqlite_indexes,
    'sqlite-vacuum': sqlite_vacuum,
    'sqlite-head': sqlite_head,
    'json-to-sqlite': json_to_sqlite,
    'sqlite-pragma': sqlite_pragma,
    'sqlite-integrity': sqlite_integrity,
    'sqlite-backup': sqlite_backup,
    'sql-format': sql_format,
    'connection-string-parse': connection_string_parse,
    'db-url-parse': db_url_parse,
    'sqlite-random-row': sqlite_random_row,
    'sqlite-distinct': sqlite_distinct,
    'sqlite-min-max': sqlite_min_max,
    'sqlite-export-json': sqlite_export_json,
    'rows-count-all': rows_count_all,
    'sqlite-drop': sqlite_drop,
    'redis-ping': redis_ping,
    'pg-url-parse': pg_url_parse,
    'mysql-url-parse': mysql_url_parse,
    'sqlite-info': sqlite_info,
}
