# NTK v2.0 Build Plan — 1000 tools, 33 universal categories

## Target
- **33 universal categories**, ~30 tools each = **~990**, plus we round up to **1000** total.
- Standalone exe (Win10/11) + Linux, installer, updater, **uninstaller**, **management web-app**.

## Categories (module = ntk/v2_<cat>.py, exposes COMMANDS dict)
Each must have AT LEAST 30 working tools (performance can have a few more to reach 1000).

1.  system       — OS/system info, boot, users, env, uptime
2.  performance  — RAM free, disk clean, cpu/gpu optimize (SAFE, see below)
3.  network      — ping, dns, ports, interfaces, http, whois, ssl
4.  file         — files & folders ops
5.  text         — text processing, case, wrap, count, replace
6.  data         — json/csv/yaml/xml/toml convert & query
7.  crypto       — hashing, hmac, encrypt/decrypt, base64, jwt
8.  security     — audit, scan, password strength, hash id, entropy
9.  dev          — dev workflow, scaffolding, lorem, semver, regex
10. git          — git status/log/branch/clean/stats wrappers
11. web          — http client, headers, bench, download, api probe
12. media        — image/audio/video info & simple ops
13. docker       — container/image/volume management
14. cloud        — aws/azure/gcp/kubectl wrappers + generators
15. database     — sqlite/query/csv-import/schema/dump
16. math         — calc, stats, matrix, prime, convert-base
17. time         — date, tz, timer, countdown, cron parse, age
18. convert      — units (length/mass/temp/data/speed) + formats
19. generate     — password, uuid, lorem, qr, name, color, token
20. monitor      — live cpu/mem/net/disk watchers
21. benchmark    — cpu/disk/mem/net speed tests
22. disk         — usage, dupes, big files, tree, mounts
23. process      — list/kill/priority/tree/port-owner
24. search       — find files/text/regex across dirs
25. archive      — zip/tar/gz create/extract/list, backup
26. image        — resize/convert/crop/exif/optimize
27. audio        — info/convert/trim (ffmpeg-backed, graceful)
28. code         — count lines, format, lint hints, complexity
29. api          — REST client, mock, json-schema, openapi peek
30. os           — services, registry(win)/systemd, scheduled tasks, env-set
31. hardware     — cpu/gpu/ram/disk/sensors/battery details
32. productivity — notes, todo, calc, clipboard, stopwatch, fun
33. admin        — users, permissions, firewall, hosts-file, tasks

## performance category — MUST be safe by default
- ram-free       : trim working sets / empty standby list. Windows: EmptyWorkingSet on
                   non-critical procs via ctypes psapi; DO NOT touch system/critical procs.
                   Linux: drop_caches only with sudo, else advise. Never kill user apps.
- clean-disk     : delete ONLY temp/cache: %TEMP%, C:\Windows\Temp, browser caches,
                   recycle bin (with confirm), thumbnail cache. Show freed bytes.
                   ALWAYS ask confirmation unless --yes. Never touch Documents/user files.
- cpu-optimize   : lower priority of heavy background procs, report top CPU hogs, suggest.
- gpu-optimize   : report GPU status/driver/power mode; on Win use nvidia-smi/wmic if present.
- boost          : safe combo of ram-free + clean-disk(dry) + report. --yes to apply.
- startup-clean  : list & (optionally) disable startup items (report-first).
- services-trim  : list trimmable non-essential services (report-first, never auto-stop critical).
- temp-clean, cache-clean, dns-flush, network-reset(report), power-plan,
  bloat-scan, mem-report, cpu-throttle-check, thermals, ... (>=30 total; may exceed to hit 1000)

## Conventions (SAME as CONVENTIONS.md)
- `def toolname(args): """One-line help.""" ... return 0`
- COMMANDS = {"tool-name": toolname, ...}  (hyphenated CLI names ok)
- stdlib-first; optional deps (psutil, requests, PIL) in try/except -> util.warn + return 1
- Cross-platform; use util.IS_WINDOWS to branch. Never sys.exit(). Return int.
- Destructive ops: require confirmation or --yes flag. SAFE by default.
- Use util.header/kv/table/ok/err/warn/info/bar/human_bytes/run/which.

## Deliverables
- ntk/v2_*.py (33 modules)
- router updated to 33 categories (+ legacy aliases mapping old names)
- management app: installer/ntk_manage.py (localhost server + open browser)
- uninstaller: installer/ntk_uninstall.py + `ntk uninstall` command
- regenerated COMMANDS.md handbook, README update, v2.0 release
