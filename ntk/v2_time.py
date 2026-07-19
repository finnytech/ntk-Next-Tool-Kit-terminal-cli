"""NTK v2 time tools."""
import os
import time
from . import util

def now(args):
    """now tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "now: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time now [value]")
        return 2

def utc_now(args):
    """utc-now tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "utc-now: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time utc-now [value]")
        return 2

def epoch(args):
    """epoch tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "epoch: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time epoch [value]")
        return 2

def epoch_to_date(args):
    """epoch-to-date tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "epoch-to-date: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time epoch-to-date [value]")
        return 2

def date_to_epoch(args):
    """date-to-epoch tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "date-to-epoch: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time date-to-epoch [value]")
        return 2

def timezone(args):
    """timezone tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "timezone: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time timezone [value]")
        return 2

def world_clock(args):
    """world-clock tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "world-clock: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time world-clock [value]")
        return 2

def diff_days(args):
    """diff-days tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "diff-days: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time diff-days [value]")
        return 2

def days_until(args):
    """days-until tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "days-until: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time days-until [value]")
        return 2

def age(args):
    """age tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "age: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time age [value]")
        return 2

def weekday(args):
    """weekday tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "weekday: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time weekday [value]")
        return 2

def week_number(args):
    """week-number tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "week-number: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time week-number [value]")
        return 2

def is_leap(args):
    """is-leap tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "is-leap: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time is-leap [value]")
        return 2

def calendar(args):
    """calendar tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "calendar: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time calendar [value]")
        return 2

def add_days(args):
    """add-days tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "add-days: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time add-days [value]")
        return 2

def iso_now(args):
    """iso-now tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "iso-now: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time iso-now [value]")
        return 2

def parse(args):
    """parse tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "parse: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time parse [value]")
        return 2

def format(args):
    """format tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "format: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time format [value]")
        return 2

def month_name(args):
    """month-name tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "month-name: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time month-name [value]")
        return 2

def quarter(args):
    """quarter tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "quarter: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time quarter [value]")
        return 2

def timestamp_ms(args):
    """timestamp-ms tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "timestamp-ms: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time timestamp-ms [value]")
        return 2

def unix_to_iso(args):
    """unix-to-iso tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "unix-to-iso: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time unix-to-iso [value]")
        return 2

def iso_to_unix(args):
    """iso-to-unix tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "iso-to-unix: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time iso-to-unix [value]")
        return 2

def time_in(args):
    """time-in tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "time-in: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time time-in [value]")
        return 2

def duration_humanize(args):
    """duration-humanize tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "duration-humanize: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time duration-humanize [value]")
        return 2

def business_days(args):
    """business-days tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "business-days: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time business-days [value]")
        return 2

def sleep(args):
    """sleep tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "sleep: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time sleep [value]")
        return 2

def countdown(args):
    """countdown tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "countdown: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time countdown [value]")
        return 2

def timezones_list(args):
    """timezones-list tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "timezones-list: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time timezones-list [value]")
        return 2

def day_of_year(args):
    """day-of-year tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "day-of-year: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time day-of-year [value]")
        return 2

def seconds_until(args):
    """seconds-until tool."""
    try:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        print(now.isoformat() if not args else "seconds-until: " + args[0])
        return 0
    except Exception:
        util.err("usage: ntk time seconds-until [value]")
        return 2

COMMANDS = {
    'now': now,
    'utc-now': utc_now,
    'epoch': epoch,
    'epoch-to-date': epoch_to_date,
    'date-to-epoch': date_to_epoch,
    'timezone': timezone,
    'world-clock': world_clock,
    'diff-days': diff_days,
    'days-until': days_until,
    'age': age,
    'weekday': weekday,
    'week-number': week_number,
    'is-leap': is_leap,
    'calendar': calendar,
    'add-days': add_days,
    'iso-now': iso_now,
    'parse': parse,
    'format': format,
    'month-name': month_name,
    'quarter': quarter,
    'timestamp-ms': timestamp_ms,
    'unix-to-iso': unix_to_iso,
    'iso-to-unix': iso_to_unix,
    'time-in': time_in,
    'duration-humanize': duration_humanize,
    'business-days': business_days,
    'sleep': sleep,
    'countdown': countdown,
    'timezones-list': timezones_list,
    'day-of-year': day_of_year,
    'seconds-until': seconds_until,
}
