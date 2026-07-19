# NTK — Command Handbook (Befehlshandbuch)

> Complete reference for **every NTK command** on **Windows 10 / 11** and **Linux**, with call forms, parameters, options and platform notes.
>
> ⚠️ **Beta:** behaviour may change and some tools need external programs or elevated rights. Every command also supports `-h` for live help, e.g. `ntk sys info -h`.

## How to call any command

```bash
ntk <category> <tool> [parameters...]     # space form
ntk-<category>-<tool> [parameters...]     # hyphen form (identical)
ntk <category>                            # list all tools in a category
ntk <category> <tool> -h                  # help for one tool
```

- **Parameters** go right after the command, space-separated. Quote values with spaces: `ntk util calc "2 * (3 + 4)"`.
- **Platform column** shows where a tool works best; most tools are fully cross-platform.
- On Windows use CMD **or** PowerShell (both are on PATH after install).

## Categories

- [`sys` — System & OS](#sys)
- [`net` — Network & HTTP](#net)
- [`file` — Filesystem & Storage](#file)
- [`text` — Text & Data](#text)
- [`crypto` — Cryptography & Hashing](#crypto)
- [`dev` — Developer Workflow](#dev)
- [`auto` — Automation](#auto)
- [`docker` — Docker & Containers](#docker)
- [`db` — Databases](#db)
- [`web` — Web & API](#web)
- [`media` — Media & Assets](#media)
- [`ai` — AI & LLM](#ai)
- [`sec` — Security & Audit](#sec)
- [`cloud` — DevOps & Cloud](#cloud)
- [`util` — Utilities & Fun](#util)

---

## <a id="sys"></a>`sys` — System & OS

_System & OS monitoring/control. 22 tools._

### `ntk sys battery`

Battery status and remaining runtime (laptops).

- **Call forms:** `ntk sys battery …`  ·  `ntk-sys-battery …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk sys cpu`

Detailed per-core CPU usage.

- **Call forms:** `ntk sys cpu …`  ·  `ntk-sys-cpu …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk sys disk`

Disk usage of all mounts.

- **Call forms:** `ntk sys disk …`  ·  `ntk-sys-disk …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk sys env`

Show environment variables (filter: ntk sys env <substr>).

- **Call forms:** `ntk sys env …`  ·  `ntk-sys-env …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk sys hardware`

Detailed hardware specs (mainboard, RAM, GPU).

- **Call forms:** `ntk sys hardware …`  ·  `ntk-sys-hardware …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk sys history`

Searchable shell history with usage stats.

- **Call forms:** `ntk sys history …`  ·  `ntk-sys-history …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** positional args: 1 known (args[0])

### `ntk sys info`

OS, CPU, RAM, kernel and uptime at a glance.

- **Call forms:** `ntk sys info …`  ·  `ntk-sys-info …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk sys kill`

Kill a process by PID or name.

- **Call forms:** `ntk sys kill …`  ·  `ntk-sys-kill …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk sys kill <pid|name>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk sys kill-port`

Kill the process holding a given port.

- **Call forms:** `ntk sys kill-port …`  ·  `ntk-sys-kill-port …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk sys kill-port <port>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk sys log-sys`

Stream the last lines of system logs.

- **Call forms:** `ntk sys log-sys …`  ·  `ntk-sys-log-sys …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** positional args: 1 known (args[0]); flags: --no-pager

### `ntk sys path`

Show the PATH variable line by line, de-duplicated.

- **Call forms:** `ntk sys path …`  ·  `ntk-sys-path …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk sys ps`

List/search processes (filter: ntk sys ps <name>).

- **Call forms:** `ntk sys ps …`  ·  `ntk-sys-ps …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk sys ram`

Current RAM usage (total, free, cache).

- **Call forms:** `ntk sys ram …`  ·  `ntk-sys-ram …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk sys reboot`

Reboot the system (optional delay seconds).

- **Call forms:** `ntk sys reboot …`  ·  `ntk-sys-reboot …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** positional args: 1 known (args[0])

### `ntk sys service-start`

Start a service.

- **Call forms:** `ntk sys service-start …`  ·  `ntk-sys-service-start …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Usage:**
    - `ntk sys service-start <name>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk sys service-stop`

Stop a service.

- **Call forms:** `ntk sys service-stop …`  ·  `ntk-sys-service-stop …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Usage:**
    - `ntk sys service-stop <name>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk sys services`

List system services and status.

- **Call forms:** `ntk sys services …`  ·  `ntk-sys-services …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** positional args: 1 known (args[0]); flags: --no-pager, --type

### `ntk sys shell`

Info about the current shell and version.

- **Call forms:** `ntk sys shell …`  ·  `ntk-sys-shell …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** flags: --version

### `ntk sys shutdown`

Shut down the system (optional delay seconds).

- **Call forms:** `ntk sys shutdown …`  ·  `ntk-sys-shutdown …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** positional args: 1 known (args[0])

### `ntk sys temp`

Read hardware temperatures (CPU/GPU).

- **Call forms:** `ntk sys temp …`  ·  `ntk-sys-temp …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk sys uptime`

System uptime since last boot.

- **Call forms:** `ntk sys uptime …`  ·  `ntk-sys-uptime …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk sys whoami`

Current user, groups and privilege level.

- **Call forms:** `ntk sys whoami …`  ·  `ntk-sys-whoami …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)


## <a id="net"></a>`net` — Network & HTTP

_Network & HTTP tools. 26 tools._

### `ntk net bgp`

Runs `ntk net bgp` (see `-h` for details).

- **Call forms:** `ntk net bgp …`  ·  `ntk-net-bgp …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk net cert-gen`

Runs `ntk net cert-gen` (see `-h` for details).

- **Call forms:** `ntk net cert-gen …`  ·  `ntk-net-cert-gen …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk net cname`

Runs `ntk net cname` (see `-h` for details).

- **Call forms:** `ntk net cname …`  ·  `ntk-net-cname …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk net dns`

Run as: `ntk net dns <name>`

- **Call forms:** `ntk net dns …`  ·  `ntk-net-dns …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk net dns <name>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk net headers`

Run as: `ntk net headers <url>`

- **Call forms:** `ntk net headers …`  ·  `ntk-net-headers …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk net headers <url>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk net http-get`

Runs `ntk net http-get` (see `-h` for details).

- **Call forms:** `ntk net http-get …`  ·  `ntk-net-http-get …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk net http-post`

Runs `ntk net http-post` (see `-h` for details).

- **Call forms:** `ntk net http-post …`  ·  `ntk-net-http-post …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk net http-status`

Runs `ntk net http-status` (see `-h` for details).

- **Call forms:** `ntk net http-status …`  ·  `ntk-net-http-status …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk net interfaces`

Runs `ntk net interfaces` (see `-h` for details).

- **Call forms:** `ntk net interfaces …`  ·  `ntk-net-interfaces …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk net ip`

Show local and public IP addresses.

- **Call forms:** `ntk net ip …`  ·  `ntk-net-ip …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk net mac`

Runs `ntk net mac` (see `-h` for details).

- **Call forms:** `ntk net mac …`  ·  `ntk-net-mac …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk net mx`

Runs `ntk net mx` (see `-h` for details).

- **Call forms:** `ntk net mx …`  ·  `ntk-net-mx …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk net netstat`

Runs `ntk net netstat` (see `-h` for details).

- **Call forms:** `ntk net netstat …`  ·  `ntk-net-netstat …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk net ping`

Run as: `ntk net ping <host> [count]`

- **Call forms:** `ntk net ping …`  ·  `ntk-net-ping …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Usage:**
    - `ntk net ping <host> [count]`
- **Parameters:** positional args: 1 known (args[1])

### `ntk net ports`

Run as: `ntk net ports <host> [port|start-end]`

- **Call forms:** `ntk net ports …`  ·  `ntk-net-ports …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk net ports <host> [port|start-end]`
- **Parameters:** positional args: 1 known (args[1])

### `ntk net speed-ping`

Run as: `ntk net speed-ping <host> [count]`

- **Call forms:** `ntk net speed-ping …`  ·  `ntk-net-speed-ping …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk net speed-ping <host> [count]`
- **Parameters:** positional args: 1 known (args[1])

### `ntk net speedtest`

Measure download speed from a public endpoint.

- **Call forms:** `ntk net speedtest …`  ·  `ntk-net-speedtest …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk net ssh-test`

Run as: `ntk net ssh-test <host> [port]`

- **Call forms:** `ntk net ssh-test …`  ·  `ntk-net-ssh-test …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk net ssh-test <host> [port]`
- **Parameters:** positional args: 1 known (args[1])

### `ntk net ssl`

Run as: `ntk net ssl <host> [port]`

- **Call forms:** `ntk net ssl …`  ·  `ntk-net-ssl …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk net ssl <host> [port]`
- **Parameters:** positional args: 1 known (args[1])

### `ntk net subnet`

Run as: `ntk net subnet <network>`

- **Call forms:** `ntk net subnet …`  ·  `ntk-net-subnet …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk net subnet <network>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk net traceroute`

Run as: `ntk net traceroute <host>`

- **Call forms:** `ntk net traceroute …`  ·  `ntk-net-traceroute …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Usage:**
    - `ntk net traceroute <host>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk net url-parser`

Run as: `ntk net url-parser <url>`

- **Call forms:** `ntk net url-parser …`  ·  `ntk-net-url-parser …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk net url-parser <url>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk net wakeonlan`

Run as: `ntk net wakeonlan <mac> [broadcast]`

- **Call forms:** `ntk net wakeonlan …`  ·  `ntk-net-wakeonlan …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk net wakeonlan <mac> [broadcast]`
- **Parameters:** positional args: 1 known (args[1])

### `ntk net whois`

Run as: `ntk net whois <domain>`

- **Call forms:** `ntk net whois …`  ·  `ntk-net-whois …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Usage:**
    - `ntk net whois <domain>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk net wifi-list`

Runs `ntk net wifi-list` (see `-h` for details).

- **Call forms:** `ntk net wifi-list …`  ·  `ntk-net-wifi-list …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk net wifi-pass`

Run as: `ntk net wifi-pass <ssid>`

- **Call forms:** `ntk net wifi-pass …`  ·  `ntk-net-wifi-pass …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Usage:**
    - `ntk net wifi-pass <ssid>`
- **Parameters:** none (or optional; run with `-h`)


## <a id="file"></a>`file` — Filesystem & Storage

_Filesystem & storage. 22 tools._

### `ntk file chmod`

Run as: `ntk file chmod <mode> <path>`

- **Call forms:** `ntk file chmod …`  ·  `ntk-file-chmod …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file chmod <mode> <path>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk file chown`

Run as: `ntk file chown <user> <path>`

- **Call forms:** `ntk file chown …`  ·  `ntk-file-chown …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Usage:**
    - `ntk file chown <user> <path>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk file clean-temp`

Runs `ntk file clean-temp` (see `-h` for details).

- **Call forms:** `ntk file clean-temp …`  ·  `ntk-file-clean-temp …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file compare`

Run as: `ntk file compare <a> <b>`

- **Call forms:** `ntk file compare …`  ·  `ntk-file-compare …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file compare <a> <b>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk file compress`

Run as: `ntk file compress <source> [archive]`

- **Call forms:** `ntk file compress …`  ·  `ntk-file-compress …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file compress <source> [archive]`
- **Parameters:** positional args: 1 known (args[1])

### `ntk file decompress`

Run as: `ntk file decompress <archive> [dest]`

- **Call forms:** `ntk file decompress …`  ·  `ntk-file-decompress …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file decompress <archive> [dest]`
- **Parameters:** positional args: 1 known (args[1])

### `ntk file disk-health`

Run as: `ntk file disk-health <device>`

- **Call forms:** `ntk file disk-health …`  ·  `ntk-file-disk-health …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file disk-health <device>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk file duplicates`

Run as: `ntk file duplicates <dir>`

- **Call forms:** `ntk file duplicates …`  ·  `ntk-file-duplicates …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file duplicates <dir>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk file empty`

Run as: `ntk file empty <file>`

- **Call forms:** `ntk file empty …`  ·  `ntk-file-empty …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file empty <file>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk file find`

Run as: `ntk file find <dir> [pattern] [grep]`

- **Call forms:** `ntk file find …`  ·  `ntk-file-find …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file find <dir> [pattern] [grep]`
- **Parameters:** positional args: 2 known (args[1], args[2])

### `ntk file lines`

Run as: `ntk file lines <file>`

- **Call forms:** `ntk file lines …`  ·  `ntk-file-lines …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file lines <file>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk file mime`

Run as: `ntk file mime <file>`

- **Call forms:** `ntk file mime …`  ·  `ntk-file-mime …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file mime <file>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk file rename`

Run as: `ntk file rename <source> <dest>`

- **Call forms:** `ntk file rename …`  ·  `ntk-file-rename …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file rename <source> <dest>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk file shred`

Run as: `ntk file shred <file> [passes]`

- **Call forms:** `ntk file shred …`  ·  `ntk-file-shred …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file shred <file> [passes]`
- **Parameters:** positional args: 1 known (args[1])

### `ntk file size`

Run as: `ntk file size <path>`

- **Call forms:** `ntk file size …`  ·  `ntk-file-size …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file size <path>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk file stats`

Run as: `ntk file stats <file>`

- **Call forms:** `ntk file stats …`  ·  `ntk-file-stats …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file stats <file>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk file symlink`

Run as: `ntk file symlink <target> <link>`

- **Call forms:** `ntk file symlink …`  ·  `ntk-file-symlink …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file symlink <target> <link>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk file sync`

Run as: `ntk file sync <source> <dest>`

- **Call forms:** `ntk file sync …`  ·  `ntk-file-sync …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file sync <source> <dest>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk file tail-f`

Run as: `ntk file tail-f <file> [lines]`

- **Call forms:** `ntk file tail-f …`  ·  `ntk-file-tail-f …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file tail-f <file> [lines]`
- **Parameters:** positional args: 1 known (args[1])

### `ntk file temp-dir`

Runs `ntk file temp-dir` (see `-h` for details).

- **Call forms:** `ntk file temp-dir …`  ·  `ntk-file-temp-dir …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file touch`

Run as: `ntk file touch <file>`

- **Call forms:** `ntk file touch …`  ·  `ntk-file-touch …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file touch <file>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk file tree`

Run as: `ntk file tree <dir> [depth]`

- **Call forms:** `ntk file tree …`  ·  `ntk-file-tree …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk file tree <dir> [depth]`
- **Parameters:** positional args: 1 known (args[1])


## <a id="text"></a>`text` — Text & Data

_Text & data processing. 28 tools._

### `ntk text base64-dec`

Runs `ntk text base64-dec` (see `-h` for details).

- **Call forms:** `ntk text base64-dec …`  ·  `ntk-text-base64-dec …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text base64-enc`

Runs `ntk text base64-enc` (see `-h` for details).

- **Call forms:** `ntk text base64-enc …`  ·  `ntk-text-base64-enc …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text binary`

Runs `ntk text binary` (see `-h` for details).

- **Call forms:** `ntk text binary …`  ·  `ntk-text-binary …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text csv-to-json`

Runs `ntk text csv-to-json` (see `-h` for details).

- **Call forms:** `ntk text csv-to-json …`  ·  `ntk-text-csv-to-json …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text diff`

Run as: `ntk text diff <a> <b>`

- **Call forms:** `ntk text diff …`  ·  `ntk-text-diff …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk text diff <a> <b>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk text grep`

Run as: `ntk text grep <pattern> [file]`

- **Call forms:** `ntk text grep …`  ·  `ntk-text-grep …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk text grep <pattern> [file]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk text hex-dump`

Runs `ntk text hex-dump` (see `-h` for details).

- **Call forms:** `ntk text hex-dump …`  ·  `ntk-text-hex-dump …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text html-format`

Runs `ntk text html-format` (see `-h` for details).

- **Call forms:** `ntk text html-format …`  ·  `ntk-text-html-format …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text json-format`

Runs `ntk text json-format` (see `-h` for details).

- **Call forms:** `ntk text json-format …`  ·  `ntk-text-json-format …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text json-minify`

Runs `ntk text json-minify` (see `-h` for details).

- **Call forms:** `ntk text json-minify …`  ·  `ntk-text-json-minify …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text json-to-csv`

Runs `ntk text json-to-csv` (see `-h` for details).

- **Call forms:** `ntk text json-to-csv …`  ·  `ntk-text-json-to-csv …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text json-to-yaml`

Runs `ntk text json-to-yaml` (see `-h` for details).

- **Call forms:** `ntk text json-to-yaml …`  ·  `ntk-text-json-to-yaml …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text lower`

Runs `ntk text lower` (see `-h` for details).

- **Call forms:** `ntk text lower …`  ·  `ntk-text-lower …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text md-preview`

Runs `ntk text md-preview` (see `-h` for details).

- **Call forms:** `ntk text md-preview …`  ·  `ntk-text-md-preview …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text morse`

Runs `ntk text morse` (see `-h` for details).

- **Call forms:** `ntk text morse …`  ·  `ntk-text-morse …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text regex`

Run as: `ntk text regex <pattern> <text>`

- **Call forms:** `ntk text regex …`  ·  `ntk-text-regex …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk text regex <pattern> <text>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk text replace`

Run as: `ntk text replace <old> <new> <text|file>`

- **Call forms:** `ntk text replace …`  ·  `ntk-text-replace …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk text replace <old> <new> <text|file>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk text slugify`

Runs `ntk text slugify` (see `-h` for details).

- **Call forms:** `ntk text slugify …`  ·  `ntk-text-slugify …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text sort`

Runs `ntk text sort` (see `-h` for details).

- **Call forms:** `ntk text sort …`  ·  `ntk-text-sort …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text strip-html`

Runs `ntk text strip-html` (see `-h` for details).

- **Call forms:** `ntk text strip-html …`  ·  `ntk-text-strip-html …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text titlecase`

Runs `ntk text titlecase` (see `-h` for details).

- **Call forms:** `ntk text titlecase …`  ·  `ntk-text-titlecase …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text unique`

Runs `ntk text unique` (see `-h` for details).

- **Call forms:** `ntk text unique …`  ·  `ntk-text-unique …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text upper`

Runs `ntk text upper` (see `-h` for details).

- **Call forms:** `ntk text upper …`  ·  `ntk-text-upper …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text url-dec`

Runs `ntk text url-dec` (see `-h` for details).

- **Call forms:** `ntk text url-dec …`  ·  `ntk-text-url-dec …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text url-enc`

Runs `ntk text url-enc` (see `-h` for details).

- **Call forms:** `ntk text url-enc …`  ·  `ntk-text-url-enc …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text wc`

Runs `ntk text wc` (see `-h` for details).

- **Call forms:** `ntk text wc …`  ·  `ntk-text-wc …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text xml-format`

Runs `ntk text xml-format` (see `-h` for details).

- **Call forms:** `ntk text xml-format …`  ·  `ntk-text-xml-format …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text yaml-to-json`

Runs `ntk text yaml-to-json` (see `-h` for details).

- **Call forms:** `ntk text yaml-to-json …`  ·  `ntk-text-yaml-to-json …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="crypto"></a>`crypto` — Cryptography & Hashing

_Cryptography & security. 21 tools._

### `ntk crypto bcrypt`

Hash a password with bcrypt.

- **Call forms:** `ntk crypto bcrypt …`  ·  `ntk-crypto-bcrypt …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk crypto bcrypt <password>`
- **Parameters:** accepts a variable list of args

### `ntk crypto cipher-list`

List available hashlib ciphers.

- **Call forms:** `ntk crypto cipher-list …`  ·  `ntk-crypto-cipher-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto decrypt`

Decrypt Fernet ciphertext.

- **Call forms:** `ntk crypto decrypt …`  ·  `ntk-crypto-decrypt …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk crypto decrypt <key> <token>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk crypto encrypt`

Encrypt text with Fernet.

- **Call forms:** `ntk crypto encrypt …`  ·  `ntk-crypto-encrypt …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk crypto encrypt <key> <text>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk crypto file-checksum`

Checksum a file.

- **Call forms:** `ntk crypto file-checksum …`  ·  `ntk-crypto-file-checksum …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk crypto file-checksum <file> [algorithm]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk crypto hash-check`

Check text against a hash.

- **Call forms:** `ntk crypto hash-check …`  ·  `ntk-crypto-hash-check …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk crypto hash-check <algorithm> <hash> <text>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk crypto jwt-decode`

Decode JWT header and payload without verifying.

- **Call forms:** `ntk crypto jwt-decode …`  ·  `ntk-crypto-jwt-decode …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk crypto jwt-decode <token>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk crypto leet`

Convert text to leetspeak.

- **Call forms:** `ntk crypto leet …`  ·  `ntk-crypto-leet …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto md5`

MD5 hash text.

- **Call forms:** `ntk crypto md5 …`  ·  `ntk-crypto-md5 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto password`

Generate a cryptographically random password.

- **Call forms:** `ntk crypto password …`  ·  `ntk-crypto-password …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk crypto pgp-decrypt`

Decrypt GPG input or file.

- **Call forms:** `ntk crypto pgp-decrypt …`  ·  `ntk-crypto-pgp-decrypt …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto pgp-encrypt`

Encrypt a file using GPG.

- **Call forms:** `ntk crypto pgp-encrypt …`  ·  `ntk-crypto-pgp-encrypt …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto random-bytes`

Generate random bytes as hexadecimal.

- **Call forms:** `ntk crypto random-bytes …`  ·  `ntk-crypto-random-bytes …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk crypto random-bytes [count]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk crypto rot13`

Apply ROT13 to text.

- **Call forms:** `ntk crypto rot13 …`  ·  `ntk-crypto-rot13 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto rsa-gen`

Generate an RSA private key with OpenSSL.

- **Call forms:** `ntk crypto rsa-gen …`  ·  `ntk-crypto-rsa-gen …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk crypto secret-mask`

Mask likely secrets in text.

- **Call forms:** `ntk crypto secret-mask …`  ·  `ntk-crypto-secret-mask …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto sha1`

SHA-1 hash text.

- **Call forms:** `ntk crypto sha1 …`  ·  `ntk-crypto-sha1 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto sha256`

SHA-256 hash text.

- **Call forms:** `ntk crypto sha256 …`  ·  `ntk-crypto-sha256 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto sha512`

SHA-512 hash text.

- **Call forms:** `ntk crypto sha512 …`  ·  `ntk-crypto-sha512 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto totp`

Generate or verify an RFC 6238 TOTP.

- **Call forms:** `ntk crypto totp …`  ·  `ntk-crypto-totp …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk crypto totp <base32-secret> [code]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk crypto uuid`

Generate a UUID.

- **Call forms:** `ntk crypto uuid …`  ·  `ntk-crypto-uuid …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="dev"></a>`dev` — Developer Workflow

_Developer workflow & IDE utils. 25 tools._

### `ntk dev api-serve`

Serve a JSON file as an API.

- **Call forms:** `ntk dev api-serve …`  ·  `ntk-dev-api-serve …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev changelog`

Create a changelog entry from git commits.

- **Call forms:** `ntk dev changelog …`  ·  `ntk-dev-changelog …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** flags: --pretty

### `ntk dev color`

Convert HEX, RGB and HSL colors.

- **Call forms:** `ntk dev color …`  ·  `ntk-dev-color …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk dev color <#rgb|r,g,b|h,s%,l%>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk dev cron-parse`

Explain a five-field cron expression.

- **Call forms:** `ntk dev cron-parse …`  ·  `ntk-dev-cron-parse …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk dev cron-parse`
- **Parameters:** positional args: 1 known (args[0])

### `ntk dev dependency-check`

Check Python imports listed in requirements.

- **Call forms:** `ntk dev dependency-check …`  ·  `ntk-dev-dependency-check …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk dev git-clean`

Show untracked files and build artifacts.

- **Call forms:** `ntk dev git-clean …`  ·  `ntk-dev-git-clean …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** flags: --short, --untracked-files

### `ntk dev git-stats`

Show git history statistics.

- **Call forms:** `ntk dev git-stats …`  ·  `ntk-dev-git-stats …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0]); flags: --oneline, --stat

### `ntk dev gitignore-gen`

Fetch or print a language gitignore.

- **Call forms:** `ntk dev gitignore-gen …`  ·  `ntk-dev-gitignore-gen …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk dev gitignore-gen <language>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk dev image-convert`

Convert an image format with Pillow.

- **Call forms:** `ntk dev image-convert …`  ·  `ntk-dev-image-convert …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev image-resize`

Resize an image with Pillow.

- **Call forms:** `ntk dev image-resize …`  ·  `ntk-dev-image-resize …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev license-gen`

Generate a short open-source license.

- **Call forms:** `ntk dev license-gen …`  ·  `ntk-dev-license-gen …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk dev lorem`

Generate lorem ipsum text.

- **Call forms:** `ntk dev lorem …`  ·  `ntk-dev-lorem …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk dev markdown-pdf`

Convert Markdown to PDF when supported.

- **Call forms:** `ntk dev markdown-pdf …`  ·  `ntk-dev-markdown-pdf …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk dev markdown-pdf <file> [output]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk dev math`

Safely evaluate arithmetic.

- **Call forms:** `ntk dev math …`  ·  `ntk-dev-math …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk dev math <expression>`
- **Parameters:** accepts a variable list of args

### `ntk dev minify`

Naively minify text or JSON whitespace.

- **Call forms:** `ntk dev minify …`  ·  `ntk-dev-minify …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev mock-db`

Generate fake JSON database records.

- **Call forms:** `ntk dev mock-db …`  ·  `ntk-dev-mock-db …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk dev mock-user`

Generate a fake user record.

- **Call forms:** `ntk dev mock-user …`  ·  `ntk-dev-mock-user …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev port-scan`

Scan TCP ports on a host.

- **Call forms:** `ntk dev port-scan …`  ·  `ntk-dev-port-scan …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk dev port-scan <host> [start-end]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk dev readme-gen`

Generate a README template.

- **Call forms:** `ntk dev readme-gen …`  ·  `ntk-dev-readme-gen …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk dev semver`

Parse, compare or bump semantic versions.

- **Call forms:** `ntk dev semver …`  ·  `ntk-dev-semver …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk dev semver <version> [bump]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk dev static-serve`

Serve static files over HTTP.

- **Call forms:** `ntk dev static-serve …`  ·  `ntk-dev-static-serve …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev svg-minify`

Minify an SVG file.

- **Call forms:** `ntk dev svg-minify …`  ·  `ntk-dev-svg-minify …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev time`

Measure a command's runtime.

- **Call forms:** `ntk dev time …`  ·  `ntk-dev-time …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk dev time <command> [args]`
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev timestamp`

Print a Unix timestamp or convert one.

- **Call forms:** `ntk dev timestamp …`  ·  `ntk-dev-timestamp …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk dev todo`

Scan source files for TODO and FIXME.

- **Call forms:** `ntk dev todo …`  ·  `ntk-dev-todo …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])


## <a id="auto"></a>`auto` — Automation

_Automation & helpers. 15 tools._

### `ntk auto alias`

Show or explain a shell alias.

- **Call forms:** `ntk auto alias …`  ·  `ntk-auto-alias …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk auto alias <name> [command]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk auto backup`

Zip a folder with a timestamp.

- **Call forms:** `ntk auto backup …`  ·  `ntk-auto-backup …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk auto backup <folder> [output.zip]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk auto calculator`

Calculate percentages and simple interest.

- **Call forms:** `ntk auto calculator …`  ·  `ntk-auto-calculator …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk auto calculator <percent|interest> values...`
- **Parameters:** positional args: 1 known (args[0])

### `ntk auto clip-copy`

Copy text to the system clipboard.

- **Call forms:** `ntk auto clip-copy …`  ·  `ntk-auto-clip-copy …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** accepts a variable list of args; flags: --clipboard, --input

### `ntk auto clip-paste`

Print text from the system clipboard.

- **Call forms:** `ntk auto clip-paste …`  ·  `ntk-auto-clip-paste …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** flags: --clipboard, --output

### `ntk auto currency`

Fetch current exchange rates.

- **Call forms:** `ntk auto currency …`  ·  `ntk-auto-currency …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk auto currency <from> <to> [amount]`
- **Parameters:** positional args: 3 known (args[0], args[1], args[2])

### `ntk auto macro`

Run a sequence of shell commands.

- **Call forms:** `ntk auto macro …`  ·  `ntk-auto-macro …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk auto macro <command> [; command...]`
- **Parameters:** accepts a variable list of args

### `ntk auto notify`

Send a desktop notification or print it.

- **Call forms:** `ntk auto notify …`  ·  `ntk-auto-notify …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** accepts a variable list of args

### `ntk auto open`

Open a URL or file with the default application.

- **Call forms:** `ntk auto open …`  ·  `ntk-auto-open …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Usage:**
    - `ntk auto open <url-or-path>`
- **Parameters:** accepts a variable list of args

### `ntk auto reminder`

Wait minutes then print a reminder.

- **Call forms:** `ntk auto reminder …`  ·  `ntk-auto-reminder …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk auto reminder <minutes> <message>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk auto search-web`

Open a web search for terms.

- **Call forms:** `ntk auto search-web …`  ·  `ntk-auto-search-web …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk auto search-web <query>`
- **Parameters:** accepts a variable list of args

### `ntk auto todo-list`

Add, list or complete local todos.

- **Call forms:** `ntk auto todo-list …`  ·  `ntk-auto-todo-list …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk auto todo-list [add text|done number|list]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk auto update`

Show the current NTK update note.

- **Call forms:** `ntk auto update …`  ·  `ntk-auto-update …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk auto watch`

Run a command repeatedly every N seconds.

- **Call forms:** `ntk auto watch …`  ·  `ntk-auto-watch …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk auto watch <seconds> <command> [args]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk auto weather`

Fetch compact weather for a location.

- **Call forms:** `ntk auto weather …`  ·  `ntk-auto-weather …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk auto weather <location>`
- **Parameters:** accepts a variable list of args


## <a id="docker"></a>`docker` — Docker & Containers

_Docker & containers. 21 tools._

### `ntk docker clean`

Prune stopped containers, unused nets & dangling images.

- **Call forms:** `ntk docker clean …`  ·  `ntk-docker-clean …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker compose-down`

docker compose down.

- **Call forms:** `ntk docker compose-down …`  ·  `ntk-docker-compose-down …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker compose-up`

docker compose up -d.

- **Call forms:** `ntk docker compose-up …`  ·  `ntk-docker-compose-up …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker copy-from`

Copy from a container to host (container:src dest).

- **Call forms:** `ntk docker copy-from …`  ·  `ntk-docker-copy-from …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker copy-from <container:src> <dest>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk docker copy-to`

Copy host file into a container (src container:dest).

- **Call forms:** `ntk docker copy-to …`  ·  `ntk-docker-copy-to …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker copy-to <src> <container:dest>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk docker dockerfile-gen`

Generate an optimized Dockerfile (node/python/go).

- **Call forms:** `ntk docker dockerfile-gen …`  ·  `ntk-docker-dockerfile-gen …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0]); flags: --from, --no-cache-dir, --omit

### `ntk docker exec`

Open a shell inside a container.

- **Call forms:** `ntk docker exec …`  ·  `ntk-docker-exec …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker exec <container> [cmd]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk docker health`

Show health status of containers.

- **Call forms:** `ntk docker health …`  ·  `ntk-docker-health …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** flags: --format

### `ntk docker image-history`

Show layers of a local image.

- **Call forms:** `ntk docker image-history …`  ·  `ntk-docker-image-history …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker image-history <image>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk docker image-prune`

Remove dangling images.

- **Call forms:** `ntk docker image-prune …`  ·  `ntk-docker-image-prune …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker inspect-env`

Show environment variables inside a container.

- **Call forms:** `ntk docker inspect-env …`  ·  `ntk-docker-inspect-env …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker inspect-env <container>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk docker ip`

Internal IP of a running container.

- **Call forms:** `ntk docker ip …`  ·  `ntk-docker-ip …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker ip <container>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk docker k8s-pods`

List pods in the current kube context.

- **Call forms:** `ntk docker k8s-pods …`  ·  `ntk-docker-k8s-pods …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker logs`

Stream a container's logs (name/id).

- **Call forms:** `ntk docker logs …`  ·  `ntk-docker-logs …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker logs <container> [--tail N]`
- **Parameters:** flags: --tail

### `ntk docker network-list`

List docker networks.

- **Call forms:** `ntk docker network-list …`  ·  `ntk-docker-network-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker ports`

Show port mappings of all containers.

- **Call forms:** `ntk docker ports …`  ·  `ntk-docker-ports …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** flags: --format

### `ntk docker ps`

List running containers with stats.

- **Call forms:** `ntk docker ps …`  ·  `ntk-docker-ps …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** flags: --format

### `ntk docker registry-login`

Test login to a docker registry.

- **Call forms:** `ntk docker registry-login …`  ·  `ntk-docker-registry-login …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker registry-login <registry>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk docker stats`

Live resource usage of running containers.

- **Call forms:** `ntk docker stats …`  ·  `ntk-docker-stats …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** flags: --no-stream

### `ntk docker stop-all`

Stop all running containers.

- **Call forms:** `ntk docker stop-all …`  ·  `ntk-docker-stop-all …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker volume-size`

Show disk usage of docker volumes.

- **Call forms:** `ntk docker volume-size …`  ·  `ntk-docker-volume-size …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="db"></a>`db` — Databases

_Database tools. 20 tools._

### `ntk db backup-cron`

Generate a cron job + script for DB backups.

- **Call forms:** `ntk db backup-cron …`  ·  `ntk-db-backup-cron …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk db csv-import`

Import a CSV file into a sqlite table.

- **Call forms:** `ntk db csv-import …`  ·  `ntk-db-csv-import …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk db csv-import <file.db> <table> <data.csv>`
- **Parameters:** positional args: 3 known (args[0], args[1], args[2])

### `ntk db diff`

Compare schemas of two sqlite databases.

- **Call forms:** `ntk db diff …`  ·  `ntk-db-diff …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk db diff <a.db> <b.db>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk db dump`

Export sqlite structure + data as SQL.

- **Call forms:** `ntk db dump …`  ·  `ntk-db-dump …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk db dump <file> [out.sql]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk db fake-fill`

Insert N fake rows into a sqlite table.

- **Call forms:** `ntk db fake-fill …`  ·  `ntk-db-fake-fill …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk db fake-fill <file> <table> <count>`
- **Parameters:** positional args: 3 known (args[0], args[1], args[2])

### `ntk db import`

Import a .sql file into a sqlite db.

- **Call forms:** `ntk db import …`  ·  `ntk-db-import …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk db import <file.db> <script.sql>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk db json-export`

Export a sqlite table to JSON.

- **Call forms:** `ntk db json-export …`  ·  `ntk-db-json-export …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk db json-export <file.db> <table> [out.json]`
- **Parameters:** positional args: 3 known (args[0], args[1], args[2])

### `ntk db migrations`

Create a timestamped migration template.

- **Call forms:** `ntk db migrations …`  ·  `ntk-db-migrations …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk db mongo-stats`

MongoDB server status (wraps mongosh).

- **Call forms:** `ntk db mongo-stats …`  ·  `ntk-db-mongo-stats …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** flags: --eval, --quiet

### `ntk db pg-activity`

Show active PostgreSQL queries (wraps psql).

- **Call forms:** `ntk db pg-activity …`  ·  `ntk-db-pg-activity …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk db ping`

Test connection to a DB (sqlite native; others via CLI).

- **Call forms:** `ntk db ping …`  ·  `ntk-db-ping …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk db ping <sqlite-file | mysql|postgres|redis|mongo host>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk db query-time`

Measure a query's execution time (+EXPLAIN).

- **Call forms:** `ntk db query-time …`  ·  `ntk-db-query-time …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk db query-time <file>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk db redis-cli`

Simple redis client (wraps redis-cli).

- **Call forms:** `ntk db redis-cli …`  ·  `ntk-db-redis-cli …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk db redis-monitor`

Stream live redis commands (wraps redis-cli monitor).

- **Call forms:** `ntk db redis-monitor …`  ·  `ntk-db-redis-monitor …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk db schema`

Show schema of a table (or whole db).

- **Call forms:** `ntk db schema …`  ·  `ntk-db-schema …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk db schema <file> [table]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk db size`

Show row counts / size per table.

- **Call forms:** `ntk db size …`  ·  `ntk-db-size …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk db size <file>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk db sqlite-query`

Run SQL on a .db/.sqlite file (file 'SQL').

- **Call forms:** `ntk db sqlite-query …`  ·  `ntk-db-sqlite-query …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk db sqlite-query <file>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk db tables`

List tables of a sqlite db.

- **Call forms:** `ntk db tables …`  ·  `ntk-db-tables …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk db tables <file>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk db truncate`

Empty all tables of a dev sqlite db.

- **Call forms:** `ntk db truncate …`  ·  `ntk-db-truncate …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk db truncate <file>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk db tunnel`

Open an SSH tunnel for a DB connection.

- **Call forms:** `ntk db tunnel …`  ·  `ntk-db-tunnel …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk db tunnel <user@host> <localport:dbhost:dbport>`
- **Parameters:** positional args: 2 known (args[0], args[1])


## <a id="web"></a>`web` — Web & API

_Advanced web & API tools. 20 tools._

### `ntk web bench`

Load-test a URL (N requests, req/s).

- **Call forms:** `ntk web bench …`  ·  `ntk-web-bench …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web bench <url> [count=20]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk web broken-links`

Find broken links (404s) on a page.

- **Call forms:** `ntk web broken-links …`  ·  `ntk-web-broken-links …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web broken-links <url>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk web cookie-chk`

Show cookies and check HttpOnly/Secure flags.

- **Call forms:** `ntk web cookie-chk …`  ·  `ntk-web-cookie-chk …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web cookie-chk <url>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk web cors-test`

Check if a server allows cross-origin requests.

- **Call forms:** `ntk web cors-test …`  ·  `ntk-web-cors-test …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web cors-test <url>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk web css-unused`

Find CSS classes not referenced in HTML files.

- **Call forms:** `ntk web css-unused …`  ·  `ntk-web-css-unused …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web css-unused <style.css> <page.html> [more.html]`
- **Parameters:** positional args: 1 known (args[0]); accepts a variable list of args

### `ntk web dns-propagation`

Check DNS across public resolvers.

- **Call forms:** `ntk web dns-propagation …`  ·  `ntk-web-dns-propagation …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web dns-propagation <domain>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk web graphql`

Run a GraphQL query against an endpoint.

- **Call forms:** `ntk web graphql …`  ·  `ntk-web-graphql …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web graphql <url>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk web headers`

Analyze HTTP security headers (CSP/HSTS/etc.).

- **Call forms:** `ntk web headers …`  ·  `ntk-web-headers …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web headers <url>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk web http2-chk`

Check if a site supports HTTP/2 (via curl).

- **Call forms:** `ntk web http2-chk …`  ·  `ntk-web-http2-chk …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web http2-chk <url>`
- **Parameters:** positional args: 1 known (args[0]); flags: --http2

### `ntk web ip-geo`

Geolocate an IP (country, ISP).

- **Call forms:** `ntk web ip-geo …`  ·  `ntk-web-ip-geo …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk web mail-dns`

Validate MX / SPF / DMARC records.

- **Call forms:** `ntk web mail-dns …`  ·  `ntk-web-mail-dns …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web mail-dns <domain>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk web minify-html`

Minify HTML (input file or string).

- **Call forms:** `ntk web minify-html …`  ·  `ntk-web-minify-html …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web minify-html <file|html>`
- **Parameters:** positional args: 1 known (args[0]); accepts a variable list of args

### `ntk web pagespeed`

Basic page performance metrics.

- **Call forms:** `ntk web pagespeed …`  ·  `ntk-web-pagespeed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web pagespeed <url>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk web robots`

Fetch and show robots.txt.

- **Call forms:** `ntk web robots …`  ·  `ntk-web-robots …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web robots <url>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk web sitemap`

List URLs from a sitemap.xml.

- **Call forms:** `ntk web sitemap …`  ·  `ntk-web-sitemap …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web sitemap <url>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk web sse-client`

Receive Server-Sent Events from an endpoint.

- **Call forms:** `ntk web sse-client …`  ·  `ntk-web-sse-client …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web sse-client <url>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk web url-shorten`

Shorten a URL via is.gd.

- **Call forms:** `ntk web url-shorten …`  ·  `ntk-web-url-shorten …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web url-shorten <url>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk web user-agent`

Print a random User-Agent string.

- **Call forms:** `ntk web user-agent …`  ·  `ntk-web-user-agent …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web whois-expiry`

Check a domain's expiry date.

- **Call forms:** `ntk web whois-expiry …`  ·  `ntk-web-whois-expiry …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web whois-expiry <domain>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk web ws-client`

Minimal WebSocket check (best-effort).

- **Call forms:** `ntk web ws-client …`  ·  `ntk-web-ws-client …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk web ws-client <ws-url>`
- **Parameters:** positional args: 2 known (args[0], args[1])


## <a id="media"></a>`media` — Media & Assets

_Media & asset tools. 20 tools._

### `ntk media ascii-art`

Turn an image into colored ASCII art.

- **Call forms:** `ntk media ascii-art …`  ·  `ntk-media-ascii-art …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media ascii-art <image> [width]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk media audio-convert`

Convert audio format (by output extension).

- **Call forms:** `ntk media audio-convert …`  ·  `ntk-media-audio-convert …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media audio-convert <in> <out.ext>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk media audio-extract`

Extract audio from a video (mp3/aac).

- **Call forms:** `ntk media audio-extract …`  ·  `ntk-media-audio-extract …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media audio-extract <video> [out.mp3]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk media compress-video`

Compress a video (keep quality).

- **Call forms:** `ntk media compress-video …`  ·  `ntk-media-compress-video …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media compress-video <video> [out] [crf=28]`
- **Parameters:** positional args: 3 known (args[0], args[1], args[2])

### `ntk media exif-read`

Read EXIF metadata from an image.

- **Call forms:** `ntk media exif-read …`  ·  `ntk-media-exif-read …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media exif-read <image>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk media exif-strip`

Remove all EXIF data from an image.

- **Call forms:** `ntk media exif-strip …`  ·  `ntk-media-exif-strip …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media exif-strip <image> [out]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk media gif-gen`

Create a GIF from a video or image sequence.

- **Call forms:** `ntk media gif-gen …`  ·  `ntk-media-gif-gen …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media gif-gen <video|glob> [out.gif]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk media icon-gen`

Generate app/web icons (favicon sizes).

- **Call forms:** `ntk media icon-gen …`  ·  `ntk-media-icon-gen …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media icon-gen <image>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk media img-color`

Show dominant HEX colors in an image.

- **Call forms:** `ntk media img-color …`  ·  `ntk-media-img-color …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media img-color <image>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk media img-convert`

Convert image format (by output extension).

- **Call forms:** `ntk media img-convert …`  ·  `ntk-media-img-convert …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media img-convert <in> <out.ext>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk media img-resize`

Resize an image (WIDTHxHEIGHT).

- **Call forms:** `ntk media img-resize …`  ·  `ntk-media-img-resize …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media img-resize <image> <WxH> [out]`
- **Parameters:** positional args: 3 known (args[0], args[1], args[2])

### `ntk media ocr`

Read text from an image (OCR).

- **Call forms:** `ntk media ocr …`  ·  `ntk-media-ocr …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media ocr <image>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk media pdf-merge`

Merge multiple PDFs into one.

- **Call forms:** `ntk media pdf-merge …`  ·  `ntk-media-pdf-merge …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media pdf-merge <out.pdf> <in1.pdf> <in2.pdf> ...`
- **Parameters:** positional args: 1 known (args[0]); accepts a variable list of args

### `ntk media pdf-pages`

Count the pages of a PDF.

- **Call forms:** `ntk media pdf-pages …`  ·  `ntk-media-pdf-pages …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media pdf-pages <in.pdf>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk media pdf-split`

Split a PDF into single pages.

- **Call forms:** `ntk media pdf-split …`  ·  `ntk-media-pdf-split …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media pdf-split <in.pdf>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk media qrcode`

Create a QR code from text/URL.

- **Call forms:** `ntk media qrcode …`  ·  `ntk-media-qrcode …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media qrcode <text> [out.png]`
- **Parameters:** accepts a variable list of args

### `ntk media qrcode-read`

Decode a QR code from an image.

- **Call forms:** `ntk media qrcode-read …`  ·  `ntk-media-qrcode-read …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media qrcode-read <image>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk media video-mute`

Remove the audio track from a video.

- **Call forms:** `ntk media video-mute …`  ·  `ntk-media-video-mute …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media video-mute <video> [out]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk media watermark`

Add a text watermark to an image.

- **Call forms:** `ntk media watermark …`  ·  `ntk-media-watermark …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media watermark <image>`
- **Parameters:** positional args: 3 known (args[0], args[1], args[2])

### `ntk media waveform`

ASCII waveform of an audio file.

- **Call forms:** `ntk media waveform …`  ·  `ntk-media-waveform …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk media waveform <audio>`
- **Parameters:** positional args: 1 known (args[0])


## <a id="ai"></a>`ai` — AI & LLM

_AI & LLM integrations. 15 tools._

### `ntk ai code-explain`

Explain a code block in simple words.

- **Call forms:** `ntk ai code-explain …`  ·  `ntk-ai-code-explain …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk ai code-explain <file|code>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk ai commit-msg`

Generate a commit message from staged diff.

- **Call forms:** `ntk ai commit-msg …`  ·  `ntk-ai-commit-msg …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** flags: --cached

### `ntk ai embedding`

Semantic-ish similarity between two texts (offline cosine).

- **Call forms:** `ntk ai embedding …`  ·  `ntk-ai-embedding …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk ai embedding`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk ai fix-bugs`

Analyze code for bugs and suggest fixes.

- **Call forms:** `ntk ai fix-bugs …`  ·  `ntk-ai-fix-bugs …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk ai fix-bugs <file>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk ai json-schema`

Generate a JSON Schema from a JSON object.

- **Call forms:** `ntk ai json-schema …`  ·  `ntk-ai-json-schema …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk ai json-schema <file.json|json>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk ai prompt-opt`

Analyze a prompt and suggest improvements.

- **Call forms:** `ntk ai prompt-opt …`  ·  `ntk-ai-prompt-opt …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk ai prompt-opt <text|file>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk ai refactor`

Suggest refactors for structure/performance.

- **Call forms:** `ntk ai refactor …`  ·  `ntk-ai-refactor …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk ai refactor <file>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk ai regex-gen`

Generate a regex from a description (heuristic + LLM).

- **Call forms:** `ntk ai regex-gen …`  ·  `ntk-ai-regex-gen …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk ai regex-gen <description>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk ai shell-helper`

Translate natural language into a shell command.

- **Call forms:** `ntk ai shell-helper …`  ·  `ntk-ai-shell-helper …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Usage:**
    - `ntk ai shell-helper <what you want>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk ai sql-gen`

Write SQL from a natural-language request.

- **Call forms:** `ntk ai sql-gen …`  ·  `ntk-ai-sql-gen …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk ai sql-gen <request>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk ai summarize`

Summarize long text or a code file.

- **Call forms:** `ntk ai summarize …`  ·  `ntk-ai-summarize …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk ai summarize <text|file>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk ai test-gen`

Generate unit tests for code.

- **Call forms:** `ntk ai test-gen …`  ·  `ntk-ai-test-gen …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk ai test-gen <file>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk ai tokens`

Estimate token count of text (GPT/Claude approx).

- **Call forms:** `ntk ai tokens …`  ·  `ntk-ai-tokens …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk ai tokens <text|file>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk ai transcribe`

Transcribe audio to text (needs whisper/API).

- **Call forms:** `ntk ai transcribe …`  ·  `ntk-ai-transcribe …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk ai transcribe <audio>`
- **Parameters:** positional args: 1 known (args[0]); flags: --model, --ntk

### `ntk ai translate`

Translate text into another language (lang first).

- **Call forms:** `ntk ai translate …`  ·  `ntk-ai-translate …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk ai translate <lang> <text|file>`
- **Parameters:** positional args: 1 known (args[0])


## <a id="sec"></a>`sec` — Security & Audit

_System security & audit. 20 tools._

### `ntk sec anti-virus`

Quick local scan of a file (uses OS AV if available).

- **Call forms:** `ntk sec anti-virus …`  ·  `ntk-sec-anti-virus …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Usage:**
    - `ntk sec anti-virus <file>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk sec dir-brute`

Discover common web paths (authorized testing only).

- **Call forms:** `ntk sec dir-brute …`  ·  `ntk-sec-dir-brute …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk sec dir-brute <base-url>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk sec dnssec`

Validate DNSSEC signature of a domain.

- **Call forms:** `ntk sec dnssec …`  ·  `ntk-sec-dnssec …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk sec dnssec <domain>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk sec entropy`

Measure Shannon entropy of a string.

- **Call forms:** `ntk sec entropy …`  ·  `ntk-sec-entropy …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk sec entropy <string>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk sec file-integrity`

Baseline/verify file hashes (init <dir> | check <dir>).

- **Call forms:** `ntk sec file-integrity …`  ·  `ntk-sec-file-integrity …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk sec file-integrity <init|check> <dir>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk sec firewall`

Show firewall status and rules.

- **Call forms:** `ntk sec firewall …`  ·  `ntk-sec-firewall …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk sec hash-identify`

Identify a hash algorithm by shape.

- **Call forms:** `ntk sec hash-identify …`  ·  `ntk-sec-hash-identify …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk sec hash-identify <hash>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk sec key-scan`

Scan files for API keys / secrets.

- **Call forms:** `ntk sec key-scan …`  ·  `ntk-sec-key-scan …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk sec nmap`

Simplified port/network scan (uses nmap if present).

- **Call forms:** `ntk sec nmap …`  ·  `ntk-sec-nmap …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk sec nmap <host> [ports]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk sec pass-audit`

Check a password against HaveIBeenPwned (k-anonymity).

- **Call forms:** `ntk sec pass-audit …`  ·  `ntk-sec-pass-audit …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk sec pass-audit <password>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk sec ports-vuln`

Flag risky open ports on a host.

- **Call forms:** `ntk sec ports-vuln …`  ·  `ntk-sec-ports-vuln …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk sec sandbox-run`

Run a command with reduced privileges/timeout.

- **Call forms:** `ntk sec sandbox-run …`  ·  `ntk-sec-sandbox-run …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk sec sandbox-run <command...>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk sec secret-store`

Encrypted local credential store (set/get/list).

- **Call forms:** `ntk sec secret-store …`  ·  `ntk-sec-secret-store …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk sec secret-store <set|get|list> [name] [value]`
    - `...set <name> <value>`
- **Parameters:** positional args: 3 known (args[0], args[1], args[2]); accepts a variable list of args

### `ntk sec sqli-test`

Basic SQL-injection probe (authorized testing only).

- **Call forms:** `ntk sec sqli-test …`  ·  `ntk-sec-sqli-test …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk sec sqli-test <url-with-param>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk sec ssh-audit`

Check SSH server config for weak settings.

- **Call forms:** `ntk sec ssh-audit …`  ·  `ntk-sec-ssh-audit …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk sec ssl-ciphers`

List SSL/TLS ciphers a server supports.

- **Call forms:** `ntk sec ssl-ciphers …`  ·  `ntk-sec-ssl-ciphers …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk sec ssl-ciphers <host[:port]>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk sec subdomains`

Find public subdomains via crt.sh (OSINT).

- **Call forms:** `ntk sec subdomains …`  ·  `ntk-sec-subdomains …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk sec subdomains <domain>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk sec user-audit`

Audit system users and login info.

- **Call forms:** `ntk sec user-audit …`  ·  `ntk-sec-user-audit …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk sec vuln-scan`

Scan dependencies for known CVEs.

- **Call forms:** `ntk sec vuln-scan …`  ·  `ntk-sec-vuln-scan …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk sec xss-test`

Basic reflected-XSS probe (authorized testing only).

- **Call forms:** `ntk sec xss-test …`  ·  `ntk-sec-xss-test …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk sec xss-test <url-with-param>`
- **Parameters:** positional args: 1 known (args[0])


## <a id="cloud"></a>`cloud` — DevOps & Cloud

_DevOps & cloud management. 15 tools._

### `ntk cloud action-lint`

Validate a GitHub Actions workflow YAML.

- **Call forms:** `ntk cloud action-lint …`  ·  `ntk-cloud-action-lint …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud action-lint <workflow.yml>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk cloud aws-ec2-ls`

List EC2 instances.

- **Call forms:** `ntk cloud aws-ec2-ls …`  ·  `ntk-cloud-aws-ec2-ls …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** flags: --output, --query

### `ntk cloud aws-s3-ls`

List an S3 bucket's contents.

- **Call forms:** `ntk cloud aws-s3-ls …`  ·  `ntk-cloud-aws-s3-ls …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk cloud aws-s3-sync`

Sync a local dir with S3.

- **Call forms:** `ntk cloud aws-s3-sync …`  ·  `ntk-cloud-aws-s3-sync …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud aws-s3-sync <src> <dst>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk cloud cf-purge`

Purge Cloudflare cache for a zone (needs CF_API_TOKEN).

- **Call forms:** `ntk cloud cf-purge …`  ·  `ntk-cloud-cf-purge …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud cf-purge <zone-id>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk cloud docker-push`

Build and push a docker image in one step.

- **Call forms:** `ntk cloud docker-push …`  ·  `ntk-cloud-docker-push …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud docker-push <image:tag> [context=.]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk cloud env-sync`

Diff local .env against a target (prints diff).

- **Call forms:** `ntk cloud env-sync …`  ·  `ntk-cloud-env-sync …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud env-sync <.env> [other.env]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk cloud gcp-bucket-ls`

List a Google Cloud Storage bucket.

- **Call forms:** `ntk cloud gcp-bucket-ls …`  ·  `ntk-cloud-gcp-bucket-ls …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud helm-ls`

List installed Helm charts.

- **Call forms:** `ntk cloud helm-ls …`  ·  `ntk-cloud-helm-ls …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud kube-ctx`

Switch/show kube context.

- **Call forms:** `ntk cloud kube-ctx …`  ·  `ntk-cloud-kube-ctx …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk cloud kube-ns`

Switch the default namespace.

- **Call forms:** `ntk cloud kube-ns …`  ·  `ntk-cloud-kube-ns …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0]); flags: --current, --namespace

### `ntk cloud log-stream`

Stream cloud logs (AWS CloudWatch / GCP).

- **Call forms:** `ntk cloud log-stream …`  ·  `ntk-cloud-log-stream …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud log-stream <log-group>`
- **Parameters:** positional args: 1 known (args[0]); flags: --follow

### `ntk cloud netlify-deploy`

Deploy to Netlify.

- **Call forms:** `ntk cloud netlify-deploy …`  ·  `ntk-cloud-netlify-deploy …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud tf-lint`

Validate/format Terraform files.

- **Call forms:** `ntk cloud tf-lint …`  ·  `ntk-cloud-tf-lint …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud vercel-deploy`

Deploy to Vercel.

- **Call forms:** `ntk cloud vercel-deploy …`  ·  `ntk-cloud-vercel-deploy …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** flags: --yes


## <a id="util"></a>`util` — Utilities & Fun

_General utilities & terminal games. 20 tools._

### `ntk util biorhythm`

Biorhythm from birthday (YYYY-MM-DD).

- **Call forms:** `ntk util biorhythm …`  ·  `ntk-util-biorhythm …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk util biorhythm 1990-05-17`
- **Parameters:** positional args: 1 known (args[0])

### `ntk util calc`

Terminal calculator for math formulas.

- **Call forms:** `ntk util calc …`  ·  `ntk-util-calc …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk util calc`
- **Parameters:** accepts a variable list of args

### `ntk util calendar`

Show a month calendar.

- **Call forms:** `ntk util calendar …`  ·  `ntk-util-calendar …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk util clipboard-history`

List clipboard history (current clipboard).

- **Call forms:** `ntk util clipboard-history …`  ·  `ntk-util-clipboard-history …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk util diff-days`

Days between two dates (YYYY-MM-DD YYYY-MM-DD).

- **Call forms:** `ntk util diff-days …`  ·  `ntk-util-diff-days …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk util diff-days 2024-01-01 2024-12-31`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk util game-snake`

Play Snake in the terminal.

- **Call forms:** `ntk util game-snake …`  ·  `ntk-util-game-snake …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk util game-tetris`

Retro Tetris in the console.

- **Call forms:** `ntk util game-tetris …`  ·  `ntk-util-game-tetris …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk util keyboard-test`

Show terminal keycodes for pressed keys (Ctrl+C to exit).

- **Call forms:** `ntk util keyboard-test …`  ·  `ntk-util-keyboard-test …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk util morse-beep`

Play morse code as beeps (falls back to text).

- **Call forms:** `ntk util morse-beep …`  ·  `ntk-util-morse-beep …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** accepts a variable list of args

### `ntk util notes`

Terminal notebook (add/list/clear).

- **Call forms:** `ntk util notes …`  ·  `ntk-util-notes …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0]); accepts a variable list of args

### `ntk util percent`

Percentage helper (of/change/tip).

- **Call forms:** `ntk util percent …`  ·  `ntk-util-percent …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk util percent of 20 80 | change 100 120 | tip 50 15`
- **Parameters:** positional args: 3 known (args[0], args[1], args[2])

### `ntk util pomodoro`

Pomodoro timer (work break cycles).

- **Call forms:** `ntk util pomodoro …`  ·  `ntk-util-pomodoro …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk util qrcode-wifi`

Make a WiFi-join QR code (SSID PASSWORD [WPA]).

- **Call forms:** `ntk util qrcode-wifi …`  ·  `ntk-util-qrcode-wifi …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk util qrcode-wifi <SSID> <PASSWORD> [WPA|WEP|nopass]`
- **Parameters:** positional args: 3 known (args[0], args[1], args[2])

### `ntk util quote`

Random programmer quote/joke.

- **Call forms:** `ntk util quote …`  ·  `ntk-util-quote …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk util speak`

Text-to-speech via system voice.

- **Call forms:** `ntk util speak …`  ·  `ntk-util-speak …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** accepts a variable list of args

### `ntk util sys-benchmark`

Quick CPU + disk benchmark with a score.

- **Call forms:** `ntk util sys-benchmark …`  ·  `ntk-util-sys-benchmark …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk util tarot`

Draw a random tarot card.

- **Call forms:** `ntk util tarot …`  ·  `ntk-util-tarot …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk util timer`

Simple stopwatch (Ctrl+C to stop, Enter for lap). Countdown: ntk util timer 30

- **Call forms:** `ntk util timer …`  ·  `ntk-util-timer …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk util timer [seconds]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk util timezone`

Show current time in global timezones.

- **Call forms:** `ntk util timezone …`  ·  `ntk-util-timezone …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** accepts a variable list of args

### `ntk util unit`

Convert units (c2f, km2mi, b2gb, ...).

- **Call forms:** `ntk util unit …`  ·  `ntk-util-unit …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk util unit <conv> <value>   e.g. c2f 100`
- **Parameters:** positional args: 2 known (args[0], args[1])



---

**Grand total: 310 commands across 15 categories.**

Every command is also documented live: `ntk <category> <tool> -h`.
