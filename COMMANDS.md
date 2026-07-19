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

- [`system` — System & OS info/control](#system)
- [`performance` — Speed up: free RAM, clean disk, CPU/GPU optimize](#performance)
- [`network` — Network, DNS, ports & connectivity](#network)
- [`file` — Files & folders](#file)
- [`text` — Text processing](#text)
- [`data` — JSON/CSV/YAML/XML convert & query](#data)
- [`crypto` — Hashing & encryption](#crypto)
- [`security` — Security audit & scanning](#security)
- [`dev` — Developer workflow](#dev)
- [`git` — Git helpers](#git)
- [`web` — Web, HTTP & API](#web)
- [`media` — Media info & simple ops](#media)
- [`docker` — Docker & containers](#docker)
- [`cloud` — Cloud & DevOps](#cloud)
- [`database` — Database tools](#database)
- [`math` — Math, stats & number tools](#math)
- [`time` — Date, time, timers & zones](#time)
- [`convert` — Units & format conversion](#convert)
- [`generate` — Generators (passwords, UUID, QR, ...)](#generate)
- [`monitor` — Live system monitors](#monitor)
- [`benchmark` — Speed benchmarks](#benchmark)
- [`disk` — Disk & storage analysis](#disk)
- [`process` — Process management](#process)
- [`search` — Search files, text & web](#search)
- [`archive` — Archives & backups](#archive)
- [`image` — Image editing](#image)
- [`audio` — Audio tools](#audio)
- [`code` — Code analysis & formatting](#code)
- [`api` — API testing & clients](#api)
- [`os` — OS settings, services & tasks](#os)
- [`hardware` — Hardware & sensors](#hardware)
- [`productivity` — Notes, todo, calc & fun](#productivity)
- [`admin` — Admin: users, firewall, tasks](#admin)

---

## <a id="system"></a>`system` — System & OS info/control

_System & OS info/control. 30 tools._

### `ntk system arch`

Show machine architecture.

- **Call forms:** `ntk system arch …`  ·  `ntk-system-arch …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system boot-time`

Show approximate boot time.

- **Call forms:** `ntk system boot-time …`  ·  `ntk-system-boot-time …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk system cpu-count`

Show logical CPU count.

- **Call forms:** `ntk system cpu-count …`  ·  `ntk-system-cpu-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system disk-usage`

Show disk usage for a path.

- **Call forms:** `ntk system disk-usage …`  ·  `ntk-system-disk-usage …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk system env`

Show environment variables.

- **Call forms:** `ntk system env …`  ·  `ntk-system-env …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system hostname`

Show host name.

- **Call forms:** `ntk system hostname …`  ·  `ntk-system-hostname …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system hostname-set`

Set hostname with --yes confirmation.

- **Call forms:** `ntk system hostname-set …`  ·  `ntk-system-hostname-set …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk system hostname-set NAME --yes`
- **Parameters:** positional args: 1 known (args[0]); accepts a variable list of args; flags: --yes

### `ntk system is-admin`

Report administrator privilege.

- **Call forms:** `ntk system is-admin …`  ·  `ntk-system-is-admin …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system kernel`

Show kernel release.

- **Call forms:** `ntk system kernel …`  ·  `ntk-system-kernel …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system load`

Show CPU load averages.

- **Call forms:** `ntk system load …`  ·  `ntk-system-load …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system locale`

Show locale settings.

- **Call forms:** `ntk system locale …`  ·  `ntk-system-locale …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system lock`

Lock current workstation.

- **Call forms:** `ntk system lock …`  ·  `ntk-system-lock …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk system logical-cores`

Show logical CPU cores.

- **Call forms:** `ntk system logical-cores …`  ·  `ntk-system-logical-cores …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system logoff`

Log off current session.

- **Call forms:** `ntk system logoff …`  ·  `ntk-system-logoff …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system motd`

Show message of the day.

- **Call forms:** `ntk system motd …`  ·  `ntk-system-motd …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system ntk-version`

Show NTK version.

- **Call forms:** `ntk system ntk-version …`  ·  `ntk-system-ntk-version …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system os-info`

Show operating system information.

- **Call forms:** `ntk system os-info …`  ·  `ntk-system-os-info …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system path-list`

List PATH entries.

- **Call forms:** `ntk system path-list …`  ·  `ntk-system-path-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system physical-cores`

Show physical CPU cores.

- **Call forms:** `ntk system physical-cores …`  ·  `ntk-system-physical-cores …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system python-version`

Show Python version.

- **Call forms:** `ntk system python-version …`  ·  `ntk-system-python-version …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system reboot`

Reboot system with explicit confirmation.

- **Call forms:** `ntk system reboot …`  ·  `ntk-system-reboot …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** accepts a variable list of args; flags: --yes

### `ntk system session-info`

Show session environment.

- **Call forms:** `ntk system session-info …`  ·  `ntk-system-session-info …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system shell`

Show configured shell.

- **Call forms:** `ntk system shell …`  ·  `ntk-system-shell …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk system shutdown`

Shutdown system with explicit confirmation.

- **Call forms:** `ntk system shutdown …`  ·  `ntk-system-shutdown …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system swap`

Show swap usage.

- **Call forms:** `ntk system swap …`  ·  `ntk-system-swap …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system timezone`

Show timezone.

- **Call forms:** `ntk system timezone …`  ·  `ntk-system-timezone …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system uptime`

Show system uptime.

- **Call forms:** `ntk system uptime …`  ·  `ntk-system-uptime …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk system users`

List logged-in users.

- **Call forms:** `ntk system users …`  ·  `ntk-system-users …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system virtualization-detect`

Detect virtualization hints.

- **Call forms:** `ntk system virtualization-detect …`  ·  `ntk-system-virtualization-detect …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk system whoami`

Show current user.

- **Call forms:** `ntk system whoami …`  ·  `ntk-system-whoami …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="performance"></a>`performance` — Speed up: free RAM, clean disk, CPU/GPU optimize

_Speed up: free RAM, clean disk, CPU/GPU optimize. 32 tools._

### `ntk performance battery`

Show battery percentage and time remaining.

- **Call forms:** `ntk performance battery …`  ·  `ntk-performance-battery …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance bloat-scan`

Scan for large caches, logs and temp taking up space.

- **Call forms:** `ntk performance bloat-scan …`  ·  `ntk-performance-bloat-scan …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance boost`

Safe all-in-one: report + free RAM + preview disk cleanup. --yes applies.

- **Call forms:** `ntk performance boost …`  ·  `ntk-performance-boost …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** accepts a variable list of args; flags: --yes

### `ntk performance cache-clean`

Clear common app/browser caches (safe).

- **Call forms:** `ntk performance cache-clean …`  ·  `ntk-performance-cache-clean …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** accepts a variable list of args; flags: --yes

### `ntk performance clean-disk`

Clean ONLY temp/cache (safe). Personal files untouched. Use --yes to apply.

- **Call forms:** `ntk performance clean-disk …`  ·  `ntk-performance-clean-disk …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** accepts a variable list of args; flags: --yes

### `ntk performance cpu-info`

Show CPU model, cores and current load.

- **Call forms:** `ntk performance cpu-info …`  ·  `ntk-performance-cpu-info …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance cpu-optimize`

Report CPU hogs and lower priority of heavy background tasks (safe).

- **Call forms:** `ntk performance cpu-optimize …`  ·  `ntk-performance-cpu-optimize …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** accepts a variable list of args; flags: --yes

### `ntk performance cpu-throttle-check`

Check whether the CPU is being thermally/power throttled.

- **Call forms:** `ntk performance cpu-throttle-check …`  ·  `ntk-performance-cpu-throttle-check …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance disk-usage`

Show disk usage summary for all drives.

- **Call forms:** `ntk performance disk-usage …`  ·  `ntk-performance-disk-usage …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance dns-flush`

Flush the DNS resolver cache.

- **Call forms:** `ntk performance dns-flush …`  ·  `ntk-performance-dns-flush …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** flags: --flush-caches

### `ntk performance gpu-info`

Show GPU model, driver, memory and power mode.

- **Call forms:** `ntk performance gpu-info …`  ·  `ntk-performance-gpu-info …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** flags: --format, --query-gpu

### `ntk performance gpu-optimize`

Report GPU status and power/optimization hints.

- **Call forms:** `ntk performance gpu-optimize …`  ·  `ntk-performance-gpu-optimize …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance gpu-processes`

List processes using the GPU (nvidia only).

- **Call forms:** `ntk performance gpu-processes …`  ·  `ntk-performance-gpu-processes …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** flags: --format, --query-compute-apps

### `ntk performance health`

Overall performance health score (RAM/CPU/disk).

- **Call forms:** `ntk performance health …`  ·  `ntk-performance-health …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance io-report`

Show disk I/O counters.

- **Call forms:** `ntk performance io-report …`  ·  `ntk-performance-io-report …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance mem-report`

Detailed memory usage report.

- **Call forms:** `ntk performance mem-report …`  ·  `ntk-performance-mem-report …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance net-report`

Show network I/O counters per interface.

- **Call forms:** `ntk performance net-report …`  ·  `ntk-performance-net-report …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance network-boost`

Report network tweaks and flush DNS (safe).

- **Call forms:** `ntk performance network-boost …`  ·  `ntk-performance-network-boost …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance power-plan`

Show or set the OS power plan (high-performance/balanced).

- **Call forms:** `ntk performance power-plan …`  ·  `ntk-performance-power-plan …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** positional args: 1 known (args[0])

### `ntk performance prefetch-clean`

Clean Windows Prefetch (safe; rebuilt automatically).

- **Call forms:** `ntk performance prefetch-clean …`  ·  `ntk-performance-prefetch-clean …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** accepts a variable list of args; flags: --yes

### `ntk performance process-count`

Count running processes and threads.

- **Call forms:** `ntk performance process-count …`  ·  `ntk-performance-process-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance quick-scan`

Fast overview: health + top RAM + top CPU.

- **Call forms:** `ntk performance quick-scan …`  ·  `ntk-performance-quick-scan …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance ram-free`

Free RAM by trimming working sets/caches (SAFE: no apps closed).

- **Call forms:** `ntk performance ram-free …`  ·  `ntk-performance-ram-free …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** accepts a variable list of args; flags: --yes

### `ntk performance recycle-clean`

Empty the Recycle Bin / Trash (asks first).

- **Call forms:** `ntk performance recycle-clean …`  ·  `ntk-performance-recycle-clean …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** flags: --yes

### `ntk performance services-list`

List running services (to spot trimmable ones).

- **Call forms:** `ntk performance services-list …`  ·  `ntk-performance-services-list …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** flags: --no-legend, --no-pager, --state, --type

### `ntk performance standby-clear`

Clear the standby memory list (Windows, needs admin).

- **Call forms:** `ntk performance standby-clear …`  ·  `ntk-performance-standby-clear …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** accepts a variable list of args; flags: --yes

### `ntk performance startup-list`

List programs that run at startup (report-first).

- **Call forms:** `ntk performance startup-list …`  ·  `ntk-performance-startup-list …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance swap-report`

Show swap/pagefile usage.

- **Call forms:** `ntk performance swap-report …`  ·  `ntk-performance-swap-report …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance temp-clean`

Clear temporary files only (alias of clean-disk, temp dirs).

- **Call forms:** `ntk performance temp-clean …`  ·  `ntk-performance-temp-clean …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance thermals`

Show temperature sensors if available.

- **Call forms:** `ntk performance thermals …`  ·  `ntk-performance-thermals …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk performance top-memory`

Show top memory-consuming processes.

- **Call forms:** `ntk performance top-memory …`  ·  `ntk-performance-top-memory …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk performance uptime`

Show system uptime and boot time.

- **Call forms:** `ntk performance uptime …`  ·  `ntk-performance-uptime …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="network"></a>`network` — Network, DNS, ports & connectivity

_Network, DNS, ports & connectivity. 31 tools._

### `ntk network arp`

Runs `ntk network arp` (see `-h` for details).

- **Call forms:** `ntk network arp …`  ·  `ntk-network-arp …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network cert-expiry`

Runs `ntk network cert-expiry` (see `-h` for details).

- **Call forms:** `ntk network cert-expiry …`  ·  `ntk-network-cert-expiry …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network dns-cache`

Runs `ntk network dns-cache` (see `-h` for details).

- **Call forms:** `ntk network dns-cache …`  ·  `ntk-network-dns-cache …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network dns-lookup`

Runs `ntk network dns-lookup` (see `-h` for details).

- **Call forms:** `ntk network dns-lookup …`  ·  `ntk-network-dns-lookup …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network download`

Runs `ntk network download` (see `-h` for details).

- **Call forms:** `ntk network download …`  ·  `ntk-network-download …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network gateway`

Runs `ntk network gateway` (see `-h` for details).

- **Call forms:** `ntk network gateway …`  ·  `ntk-network-gateway …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network headers`

Runs `ntk network headers` (see `-h` for details).

- **Call forms:** `ntk network headers …`  ·  `ntk-network-headers …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network host-up`

Runs `ntk network host-up` (see `-h` for details).

- **Call forms:** `ntk network host-up …`  ·  `ntk-network-host-up …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network http-get`

Runs `ntk network http-get` (see `-h` for details).

- **Call forms:** `ntk network http-get …`  ·  `ntk-network-http-get …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network http-post`

Runs `ntk network http-post` (see `-h` for details).

- **Call forms:** `ntk network http-post …`  ·  `ntk-network-http-post …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network http-status`

Runs `ntk network http-status` (see `-h` for details).

- **Call forms:** `ntk network http-status …`  ·  `ntk-network-http-status …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network interfaces`

Runs `ntk network interfaces` (see `-h` for details).

- **Call forms:** `ntk network interfaces …`  ·  `ntk-network-interfaces …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network ip-geo`

Runs `ntk network ip-geo` (see `-h` for details).

- **Call forms:** `ntk network ip-geo …`  ·  `ntk-network-ip-geo …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network is-online`

Runs `ntk network is-online` (see `-h` for details).

- **Call forms:** `ntk network is-online …`  ·  `ntk-network-is-online …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network local-ip`

Runs `ntk network local-ip` (see `-h` for details).

- **Call forms:** `ntk network local-ip …`  ·  `ntk-network-local-ip …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network mac`

Runs `ntk network mac` (see `-h` for details).

- **Call forms:** `ntk network mac …`  ·  `ntk-network-mac …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network mx`

Runs `ntk network mx` (see `-h` for details).

- **Call forms:** `ntk network mx …`  ·  `ntk-network-mx …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network my-ip`

Runs `ntk network my-ip` (see `-h` for details).

- **Call forms:** `ntk network my-ip …`  ·  `ntk-network-my-ip …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network netstat`

Runs `ntk network netstat` (see `-h` for details).

- **Call forms:** `ntk network netstat …`  ·  `ntk-network-netstat …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network ns`

Runs `ntk network ns` (see `-h` for details).

- **Call forms:** `ntk network ns …`  ·  `ntk-network-ns …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network ping`

Runs `ntk network ping` (see `-h` for details).

- **Call forms:** `ntk network ping …`  ·  `ntk-network-ping …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network ports-scan`

Runs `ntk network ports-scan` (see `-h` for details).

- **Call forms:** `ntk network ports-scan …`  ·  `ntk-network-ports-scan …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network reverse-dns`

Runs `ntk network reverse-dns` (see `-h` for details).

- **Call forms:** `ntk network reverse-dns …`  ·  `ntk-network-reverse-dns …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network speed-ping`

Runs `ntk network speed-ping` (see `-h` for details).

- **Call forms:** `ntk network speed-ping …`  ·  `ntk-network-speed-ping …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network ssl-info`

Runs `ntk network ssl-info` (see `-h` for details).

- **Call forms:** `ntk network ssl-info …`  ·  `ntk-network-ssl-info …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network subnet-calc`

Runs `ntk network subnet-calc` (see `-h` for details).

- **Call forms:** `ntk network subnet-calc …`  ·  `ntk-network-subnet-calc …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network traceroute`

Runs `ntk network traceroute` (see `-h` for details).

- **Call forms:** `ntk network traceroute …`  ·  `ntk-network-traceroute …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network txt`

Runs `ntk network txt` (see `-h` for details).

- **Call forms:** `ntk network txt …`  ·  `ntk-network-txt …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network url-parse`

Runs `ntk network url-parse` (see `-h` for details).

- **Call forms:** `ntk network url-parse …`  ·  `ntk-network-url-parse …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network whois`

Runs `ntk network whois` (see `-h` for details).

- **Call forms:** `ntk network whois …`  ·  `ntk-network-whois …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk network wifi-list`

Runs `ntk network wifi-list` (see `-h` for details).

- **Call forms:** `ntk network wifi-list …`  ·  `ntk-network-wifi-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="file"></a>`file` — Files & folders

_Files & folders. 31 tools._

### `ntk file bigfiles`

Run the bigfiles tool.

- **Call forms:** `ntk file bigfiles …`  ·  `ntk-file-bigfiles …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file by-ext`

Run the by ext tool.

- **Call forms:** `ntk file by-ext …`  ·  `ntk-file-by-ext …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file checksum`

Run the checksum tool.

- **Call forms:** `ntk file checksum …`  ·  `ntk-file-checksum …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file clean-empty`

Run the clean empty tool.

- **Call forms:** `ntk file clean-empty …`  ·  `ntk-file-clean-empty …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file compare`

Run the compare tool.

- **Call forms:** `ntk file compare …`  ·  `ntk-file-compare …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file copy`

Run the copy tool.

- **Call forms:** `ntk file copy …`  ·  `ntk-file-copy …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file count-lines`

Run the count lines tool.

- **Call forms:** `ntk file count-lines …`  ·  `ntk-file-count-lines …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file dupes`

Run the dupes tool.

- **Call forms:** `ntk file dupes …`  ·  `ntk-file-dupes …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file empty-dirs`

Run the empty dirs tool.

- **Call forms:** `ntk file empty-dirs …`  ·  `ntk-file-empty-dirs …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file encoding-detect`

Run the encoding detect tool.

- **Call forms:** `ntk file encoding-detect …`  ·  `ntk-file-encoding-detect …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file ext-change`

Run the ext change tool.

- **Call forms:** `ntk file ext-change …`  ·  `ntk-file-ext-change …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file find`

Run the find tool.

- **Call forms:** `ntk file find …`  ·  `ntk-file-find …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file hash`

Run the hash tool.

- **Call forms:** `ntk file hash …`  ·  `ntk-file-hash …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file head`

Run the head tool.

- **Call forms:** `ntk file head …`  ·  `ntk-file-head …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file join`

Run the join tool.

- **Call forms:** `ntk file join …`  ·  `ntk-file-join …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** accepts a variable list of args

### `ntk file list`

Run the list tool.

- **Call forms:** `ntk file list …`  ·  `ntk-file-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file mime`

Run the mime tool.

- **Call forms:** `ntk file mime …`  ·  `ntk-file-mime …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file mkdir-p`

Run the mkdir p tool.

- **Call forms:** `ntk file mkdir-p …`  ·  `ntk-file-mkdir-p …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file move`

Run the move tool.

- **Call forms:** `ntk file move …`  ·  `ntk-file-move …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file newest`

Run the newest tool.

- **Call forms:** `ntk file newest …`  ·  `ntk-file-newest …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file oldest`

Run the oldest tool.

- **Call forms:** `ntk file oldest …`  ·  `ntk-file-oldest …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file permissions`

Run the permissions tool.

- **Call forms:** `ntk file permissions …`  ·  `ntk-file-permissions …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file rename-batch`

Run the rename batch tool.

- **Call forms:** `ntk file rename-batch …`  ·  `ntk-file-rename-batch …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file size`

Run the size tool.

- **Call forms:** `ntk file size …`  ·  `ntk-file-size …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file split`

Run the split tool.

- **Call forms:** `ntk file split …`  ·  `ntk-file-split …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file stats`

Run the stats tool.

- **Call forms:** `ntk file stats …`  ·  `ntk-file-stats …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file tail`

Run the tail tool.

- **Call forms:** `ntk file tail …`  ·  `ntk-file-tail …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file touch`

Run the touch tool.

- **Call forms:** `ntk file touch …`  ·  `ntk-file-touch …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file tree`

Run the tree tool.

- **Call forms:** `ntk file tree …`  ·  `ntk-file-tree …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file watch-changes`

Run the watch changes tool.

- **Call forms:** `ntk file watch-changes …`  ·  `ntk-file-watch-changes …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk file wc`

Run the wc tool.

- **Call forms:** `ntk file wc …`  ·  `ntk-file-wc …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="text"></a>`text` — Text processing

_Text processing. 30 tools._

### `ntk text ascii-table`

Run the ascii table tool.

- **Call forms:** `ntk text ascii-table …`  ·  `ntk-text-ascii-table …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text camel`

Run the camel tool.

- **Call forms:** `ntk text camel …`  ·  `ntk-text-camel …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text capitalize`

Run the capitalize tool.

- **Call forms:** `ntk text capitalize …`  ·  `ntk-text-capitalize …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text count`

Run the count tool.

- **Call forms:** `ntk text count …`  ·  `ntk-text-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text dedent`

Run the dedent tool.

- **Call forms:** `ntk text dedent …`  ·  `ntk-text-dedent …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text grep`

Run the grep tool.

- **Call forms:** `ntk text grep …`  ·  `ntk-text-grep …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text head-lines`

Run the head lines tool.

- **Call forms:** `ntk text head-lines …`  ·  `ntk-text-head-lines …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text indent`

Run the indent tool.

- **Call forms:** `ntk text indent …`  ·  `ntk-text-indent …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text kebab`

Run the kebab tool.

- **Call forms:** `ntk text kebab …`  ·  `ntk-text-kebab …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text leet`

Run the leet tool.

- **Call forms:** `ntk text leet …`  ·  `ntk-text-leet …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text lower`

Run the lower tool.

- **Call forms:** `ntk text lower …`  ·  `ntk-text-lower …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text nato`

Run the nato tool.

- **Call forms:** `ntk text nato …`  ·  `ntk-text-nato …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text number-lines`

Run the number lines tool.

- **Call forms:** `ntk text number-lines …`  ·  `ntk-text-number-lines …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text remove-blank`

Run the remove blank tool.

- **Call forms:** `ntk text remove-blank …`  ·  `ntk-text-remove-blank …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text replace`

Run the replace tool.

- **Call forms:** `ntk text replace …`  ·  `ntk-text-replace …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text reverse`

Run the reverse tool.

- **Call forms:** `ntk text reverse …`  ·  `ntk-text-reverse …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text rot13`

Run the rot13 tool.

- **Call forms:** `ntk text rot13 …`  ·  `ntk-text-rot13 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text shuffle-lines`

Run the shuffle lines tool.

- **Call forms:** `ntk text shuffle-lines …`  ·  `ntk-text-shuffle-lines …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text slugify`

Run the slugify tool.

- **Call forms:** `ntk text slugify …`  ·  `ntk-text-slugify …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text snake`

Run the snake tool.

- **Call forms:** `ntk text snake …`  ·  `ntk-text-snake …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text sort-lines`

Run the sort lines tool.

- **Call forms:** `ntk text sort-lines …`  ·  `ntk-text-sort-lines …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text strip-ansi`

Run the strip ansi tool.

- **Call forms:** `ntk text strip-ansi …`  ·  `ntk-text-strip-ansi …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text tabs-to-spaces`

Run the tabs to spaces tool.

- **Call forms:** `ntk text tabs-to-spaces …`  ·  `ntk-text-tabs-to-spaces …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text tail-lines`

Run the tail lines tool.

- **Call forms:** `ntk text tail-lines …`  ·  `ntk-text-tail-lines …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text title`

Run the title tool.

- **Call forms:** `ntk text title …`  ·  `ntk-text-title …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text trim`

Run the trim tool.

- **Call forms:** `ntk text trim …`  ·  `ntk-text-trim …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text unique-lines`

Run the unique lines tool.

- **Call forms:** `ntk text unique-lines …`  ·  `ntk-text-unique-lines …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text upper`

Run the upper tool.

- **Call forms:** `ntk text upper …`  ·  `ntk-text-upper …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text wordfreq`

Run the wordfreq tool.

- **Call forms:** `ntk text wordfreq …`  ·  `ntk-text-wordfreq …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk text wrap`

Run the wrap tool.

- **Call forms:** `ntk text wrap …`  ·  `ntk-text-wrap …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="data"></a>`data` — JSON/CSV/YAML/XML convert & query

_JSON/CSV/YAML/XML convert & query. 31 tools._

### `ntk data base64-json`

Run the base64 json tool.

- **Call forms:** `ntk data base64-json …`  ·  `ntk-data-base64-json …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data csv-cols`

Run the csv cols tool.

- **Call forms:** `ntk data csv-cols …`  ·  `ntk-data-csv-cols …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data csv-dedupe`

Run the csv dedupe tool.

- **Call forms:** `ntk data csv-dedupe …`  ·  `ntk-data-csv-dedupe …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data csv-filter`

Run the csv filter tool.

- **Call forms:** `ntk data csv-filter …`  ·  `ntk-data-csv-filter …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data csv-head`

Run the csv head tool.

- **Call forms:** `ntk data csv-head …`  ·  `ntk-data-csv-head …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data csv-sort`

Run the csv sort tool.

- **Call forms:** `ntk data csv-sort …`  ·  `ntk-data-csv-sort …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data csv-stats`

Run the csv stats tool.

- **Call forms:** `ntk data csv-stats …`  ·  `ntk-data-csv-stats …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data csv-to-json`

Run the csv to json tool.

- **Call forms:** `ntk data csv-to-json …`  ·  `ntk-data-csv-to-json …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data csv-to-md`

Run the csv to md tool.

- **Call forms:** `ntk data csv-to-md …`  ·  `ntk-data-csv-to-md …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data data-stats`

Run the data stats tool.

- **Call forms:** `ntk data data-stats …`  ·  `ntk-data-data-stats …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data env-to-json`

Run the env to json tool.

- **Call forms:** `ntk data env-to-json …`  ·  `ntk-data-env-to-json …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data flatten-json`

Run the flatten json tool.

- **Call forms:** `ntk data flatten-json …`  ·  `ntk-data-flatten-json …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data json-count`

Run the json count tool.

- **Call forms:** `ntk data json-count …`  ·  `ntk-data-json-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data json-diff`

Run the json diff tool.

- **Call forms:** `ntk data json-diff …`  ·  `ntk-data-json-diff …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data json-format`

Run the json format tool.

- **Call forms:** `ntk data json-format …`  ·  `ntk-data-json-format …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data json-get`

Run the json get tool.

- **Call forms:** `ntk data json-get …`  ·  `ntk-data-json-get …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data json-keys`

Run the json keys tool.

- **Call forms:** `ntk data json-keys …`  ·  `ntk-data-json-keys …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data json-lines`

Run the json lines tool.

- **Call forms:** `ntk data json-lines …`  ·  `ntk-data-json-lines …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data json-merge`

Run the json merge tool.

- **Call forms:** `ntk data json-merge …`  ·  `ntk-data-json-merge …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data json-minify`

Run the json minify tool.

- **Call forms:** `ntk data json-minify …`  ·  `ntk-data-json-minify …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data json-schema-infer`

Run the json schema infer tool.

- **Call forms:** `ntk data json-schema-infer …`  ·  `ntk-data-json-schema-infer …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data json-sort-keys`

Run the json sort keys tool.

- **Call forms:** `ntk data json-sort-keys …`  ·  `ntk-data-json-sort-keys …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data json-to-csv`

Run the json to csv tool.

- **Call forms:** `ntk data json-to-csv …`  ·  `ntk-data-json-to-csv …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data json-to-yaml`

Run the json to yaml tool.

- **Call forms:** `ntk data json-to-yaml …`  ·  `ntk-data-json-to-yaml …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data json-validate`

Run the json validate tool.

- **Call forms:** `ntk data json-validate …`  ·  `ntk-data-json-validate …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data ndjson-to-json`

Run the ndjson to json tool.

- **Call forms:** `ntk data ndjson-to-json …`  ·  `ntk-data-ndjson-to-json …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data pretty`

Run the pretty tool.

- **Call forms:** `ntk data pretty …`  ·  `ntk-data-pretty …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data toml-to-json`

Run the toml to json tool.

- **Call forms:** `ntk data toml-to-json …`  ·  `ntk-data-toml-to-json …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data url-to-json`

Run the url to json tool.

- **Call forms:** `ntk data url-to-json …`  ·  `ntk-data-url-to-json …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data xml-to-json`

Run the xml to json tool.

- **Call forms:** `ntk data xml-to-json …`  ·  `ntk-data-xml-to-json …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk data yaml-to-json`

Run the yaml to json tool.

- **Call forms:** `ntk data yaml-to-json …`  ·  `ntk-data-yaml-to-json …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="crypto"></a>`crypto` — Hashing & encryption

_Hashing & encryption. 30 tools._

### `ntk crypto base32`

Run the base32 tool.

- **Call forms:** `ntk crypto base32 …`  ·  `ntk-crypto-base32 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto base64-dec`

Run the base64 dec tool.

- **Call forms:** `ntk crypto base64-dec …`  ·  `ntk-crypto-base64-dec …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto base64-enc`

Run the base64 enc tool.

- **Call forms:** `ntk crypto base64-enc …`  ·  `ntk-crypto-base64-enc …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto blake2`

Run the blake2 tool.

- **Call forms:** `ntk crypto blake2 …`  ·  `ntk-crypto-blake2 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto caesar`

Run the caesar tool.

- **Call forms:** `ntk crypto caesar …`  ·  `ntk-crypto-caesar …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto checksum-file`

Run the checksum file tool.

- **Call forms:** `ntk crypto checksum-file …`  ·  `ntk-crypto-checksum-file …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto crc32`

Run the crc32 tool.

- **Call forms:** `ntk crypto crc32 …`  ·  `ntk-crypto-crc32 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto entropy`

Run the entropy tool.

- **Call forms:** `ntk crypto entropy …`  ·  `ntk-crypto-entropy …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto fernet-gen`

Run the fernet gen tool.

- **Call forms:** `ntk crypto fernet-gen …`  ·  `ntk-crypto-fernet-gen …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto file-hash`

Run the file hash tool.

- **Call forms:** `ntk crypto file-hash …`  ·  `ntk-crypto-file-hash …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto hash-file-tree`

Run the hash file tree tool.

- **Call forms:** `ntk crypto hash-file-tree …`  ·  `ntk-crypto-hash-file-tree …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto hex-dec`

Run the hex dec tool.

- **Call forms:** `ntk crypto hex-dec …`  ·  `ntk-crypto-hex-dec …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto hex-enc`

Run the hex enc tool.

- **Call forms:** `ntk crypto hex-enc …`  ·  `ntk-crypto-hex-enc …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto hmac-sha256`

Run the hmac sha256 tool.

- **Call forms:** `ntk crypto hmac-sha256 …`  ·  `ntk-crypto-hmac-sha256 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto md5`

Run the md5 tool.

- **Call forms:** `ntk crypto md5 …`  ·  `ntk-crypto-md5 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto morse-dec`

Run the morse dec tool.

- **Call forms:** `ntk crypto morse-dec …`  ·  `ntk-crypto-morse-dec …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto morse-enc`

Run the morse enc tool.

- **Call forms:** `ntk crypto morse-enc …`  ·  `ntk-crypto-morse-enc …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto password-hash`

Run the password hash tool.

- **Call forms:** `ntk crypto password-hash …`  ·  `ntk-crypto-password-hash …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto random-bytes`

Run the random bytes tool.

- **Call forms:** `ntk crypto random-bytes …`  ·  `ntk-crypto-random-bytes …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto rot13`

Run the rot13 tool.

- **Call forms:** `ntk crypto rot13 …`  ·  `ntk-crypto-rot13 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto sha1`

Run the sha1 tool.

- **Call forms:** `ntk crypto sha1 …`  ·  `ntk-crypto-sha1 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto sha256`

Run the sha256 tool.

- **Call forms:** `ntk crypto sha256 …`  ·  `ntk-crypto-sha256 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto sha3-256`

Run the sha3 256 tool.

- **Call forms:** `ntk crypto sha3-256 …`  ·  `ntk-crypto-sha3-256 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto sha512`

Run the sha512 tool.

- **Call forms:** `ntk crypto sha512 …`  ·  `ntk-crypto-sha512 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto uuid`

Run the uuid tool.

- **Call forms:** `ntk crypto uuid …`  ·  `ntk-crypto-uuid …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto uuid5`

Run the uuid5 tool.

- **Call forms:** `ntk crypto uuid5 …`  ·  `ntk-crypto-uuid5 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto verify-hash`

Run the verify hash tool.

- **Call forms:** `ntk crypto verify-hash …`  ·  `ntk-crypto-verify-hash …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto verify-pbkdf2`

Run the verify pbkdf2 tool.

- **Call forms:** `ntk crypto verify-pbkdf2 …`  ·  `ntk-crypto-verify-pbkdf2 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto vigenere`

Run the vigenere tool.

- **Call forms:** `ntk crypto vigenere …`  ·  `ntk-crypto-vigenere …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk crypto xor`

Run the xor tool.

- **Call forms:** `ntk crypto xor …`  ·  `ntk-crypto-xor …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="security"></a>`security` — Security audit & scanning

_Security audit & scanning. 31 tools._

### `ntk security admin-check`

Run the admin check tool.

- **Call forms:** `ntk security admin-check …`  ·  `ntk-security-admin-check …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security arp-table`

Run the arp table tool.

- **Call forms:** `ntk security arp-table …`  ·  `ntk-security-arp-table …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security base-detect`

Run the base detect tool.

- **Call forms:** `ntk security base-detect …`  ·  `ntk-security-base-detect …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security breach-check-format`

Run the breach check format tool.

- **Call forms:** `ntk security breach-check-format …`  ·  `ntk-security-breach-check-format …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security cert-info`

Run the cert info tool.

- **Call forms:** `ntk security cert-info …`  ·  `ntk-security-cert-info …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security cipher-list`

Run the cipher list tool.

- **Call forms:** `ntk security cipher-list …`  ·  `ntk-security-cipher-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security dns-leak-hint`

Run the dns leak hint tool.

- **Call forms:** `ntk security dns-leak-hint …`  ·  `ntk-security-dns-leak-hint …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security entropy`

Run the entropy tool.

- **Call forms:** `ntk security entropy …`  ·  `ntk-security-entropy …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security failed-logins`

Run the failed logins tool.

- **Call forms:** `ntk security failed-logins …`  ·  `ntk-security-failed-logins …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security firewall-rules-count`

Run the firewall rules count tool.

- **Call forms:** `ntk security firewall-rules-count …`  ·  `ntk-security-firewall-rules-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security firewall-status`

Run the firewall status tool.

- **Call forms:** `ntk security firewall-status …`  ·  `ntk-security-firewall-status …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security hash-identify`

Run the hash identify tool.

- **Call forms:** `ntk security hash-identify …`  ·  `ntk-security-hash-identify …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security hosts-file-show`

Run the hosts file show tool.

- **Call forms:** `ntk security hosts-file-show …`  ·  `ntk-security-hosts-file-show …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security listening-services`

Run the listening services tool.

- **Call forms:** `ntk security listening-services …`  ·  `ntk-security-listening-services …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security mac-vendor-format`

Run the mac vendor format tool.

- **Call forms:** `ntk security mac-vendor-format …`  ·  `ntk-security-mac-vendor-format …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security open-ports`

Run the open ports tool.

- **Call forms:** `ntk security open-ports …`  ·  `ntk-security-open-ports …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security passphrase`

Run the passphrase tool.

- **Call forms:** `ntk security passphrase …`  ·  `ntk-security-passphrase …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security password-gen-strong`

Run the password gen strong tool.

- **Call forms:** `ntk security password-gen-strong …`  ·  `ntk-security-password-gen-strong …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security password-strength`

Run the password strength tool.

- **Call forms:** `ntk security password-strength …`  ·  `ntk-security-password-strength …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security permissions-audit`

Run the permissions audit tool.

- **Call forms:** `ntk security permissions-audit …`  ·  `ntk-security-permissions-audit …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security pin-gen`

Run the pin gen tool.

- **Call forms:** `ntk security pin-gen …`  ·  `ntk-security-pin-gen …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security port-audit`

Run the port audit tool.

- **Call forms:** `ntk security port-audit …`  ·  `ntk-security-port-audit …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security random-password`

Run the random password tool.

- **Call forms:** `ntk security random-password …`  ·  `ntk-security-random-password …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security secret-scan`

Run the secret scan tool.

- **Call forms:** `ntk security secret-scan …`  ·  `ntk-security-secret-scan …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security ssh-config-audit`

Run the ssh config audit tool.

- **Call forms:** `ntk security ssh-config-audit …`  ·  `ntk-security-ssh-config-audit …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security ssl-check`

Run the ssl check tool.

- **Call forms:** `ntk security ssl-check …`  ·  `ntk-security-ssl-check …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security suid-find`

Run the suid find tool.

- **Call forms:** `ntk security suid-find …`  ·  `ntk-security-suid-find …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security tls-versions`

Run the tls versions tool.

- **Call forms:** `ntk security tls-versions …`  ·  `ntk-security-tls-versions …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security uac-status`

Run the uac status tool.

- **Call forms:** `ntk security uac-status …`  ·  `ntk-security-uac-status …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security url-safety-hint`

Run the url safety hint tool.

- **Call forms:** `ntk security url-safety-hint …`  ·  `ntk-security-url-safety-hint …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk security weak-file-perms`

Run the weak file perms tool.

- **Call forms:** `ntk security weak-file-perms …`  ·  `ntk-security-weak-file-perms …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="dev"></a>`dev` — Developer workflow

_Developer workflow. 30 tools._

### `ntk dev base64url`

Run the base64url tool.

- **Call forms:** `ntk dev base64url …`  ·  `ntk-dev-base64url …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev changelog-gen`

Run the changelog gen tool.

- **Call forms:** `ntk dev changelog-gen …`  ·  `ntk-dev-changelog-gen …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev color-convert`

Run the color convert tool.

- **Call forms:** `ntk dev color-convert …`  ·  `ntk-dev-color-convert …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev cron-explain`

Run the cron explain tool.

- **Call forms:** `ntk dev cron-explain …`  ·  `ntk-dev-cron-explain …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev date-to-epoch`

Run the date to epoch tool.

- **Call forms:** `ntk dev date-to-epoch …`  ·  `ntk-dev-date-to-epoch …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev dockerfile-gen`

Run the dockerfile gen tool.

- **Call forms:** `ntk dev dockerfile-gen …`  ·  `ntk-dev-dockerfile-gen …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev env-example-gen`

Run the env example gen tool.

- **Call forms:** `ntk dev env-example-gen …`  ·  `ntk-dev-env-example-gen …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev epoch-to-date`

Run the epoch to date tool.

- **Call forms:** `ntk dev epoch-to-date …`  ·  `ntk-dev-epoch-to-date …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev gitignore-gen`

Run the gitignore gen tool.

- **Call forms:** `ntk dev gitignore-gen …`  ·  `ntk-dev-gitignore-gen …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev htpasswd`

Run the htpasswd tool.

- **Call forms:** `ntk dev htpasswd …`  ·  `ntk-dev-htpasswd …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev http-server`

Run the http server tool.

- **Call forms:** `ntk dev http-server …`  ·  `ntk-dev-http-server …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev json-to-code`

Run the json to code tool.

- **Call forms:** `ntk dev json-to-code …`  ·  `ntk-dev-json-to-code …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev jwt-decode`

Run the jwt decode tool.

- **Call forms:** `ntk dev jwt-decode …`  ·  `ntk-dev-jwt-decode …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev license-gen`

Run the license gen tool.

- **Call forms:** `ntk dev license-gen …`  ·  `ntk-dev-license-gen …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev loc`

Run the loc tool.

- **Call forms:** `ntk dev loc …`  ·  `ntk-dev-loc …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev lorem`

Run the lorem tool.

- **Call forms:** `ntk dev lorem …`  ·  `ntk-dev-lorem …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev md-toc`

Run the md toc tool.

- **Call forms:** `ntk dev md-toc …`  ·  `ntk-dev-md-toc …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev mock-json`

Run the mock json tool.

- **Call forms:** `ntk dev mock-json …`  ·  `ntk-dev-mock-json …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev password`

Run the password tool.

- **Call forms:** `ntk dev password …`  ·  `ntk-dev-password …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev port-free`

Run the port free tool.

- **Call forms:** `ntk dev port-free …`  ·  `ntk-dev-port-free …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev readme-gen`

Run the readme gen tool.

- **Call forms:** `ntk dev readme-gen …`  ·  `ntk-dev-readme-gen …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev regex-explain-basic`

Run the regex explain basic tool.

- **Call forms:** `ntk dev regex-explain-basic …`  ·  `ntk-dev-regex-explain-basic …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev regex-test`

Run the regex test tool.

- **Call forms:** `ntk dev regex-test …`  ·  `ntk-dev-regex-test …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev scaffold-file`

Run the scaffold file tool.

- **Call forms:** `ntk dev scaffold-file …`  ·  `ntk-dev-scaffold-file …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev semver-bump`

Run the semver bump tool.

- **Call forms:** `ntk dev semver-bump …`  ·  `ntk-dev-semver-bump …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev semver-compare`

Run the semver compare tool.

- **Call forms:** `ntk dev semver-compare …`  ·  `ntk-dev-semver-compare …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev slug`

Run the slug tool.

- **Call forms:** `ntk dev slug …`  ·  `ntk-dev-slug …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev timestamp`

Run the timestamp tool.

- **Call forms:** `ntk dev timestamp …`  ·  `ntk-dev-timestamp …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev todo-scan`

Run the todo scan tool.

- **Call forms:** `ntk dev todo-scan …`  ·  `ntk-dev-todo-scan …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk dev uuid`

Run the uuid tool.

- **Call forms:** `ntk dev uuid …`  ·  `ntk-dev-uuid …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="git"></a>`git` — Git helpers

_Git helpers. 31 tools._

### `ntk git ahead-behind`

Runs `ntk git ahead-behind` (see `-h` for details).

- **Call forms:** `ntk git ahead-behind …`  ·  `ntk-git-ahead-behind …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git blame-summary`

Runs `ntk git blame-summary` (see `-h` for details).

- **Call forms:** `ntk git blame-summary …`  ·  `ntk-git-blame-summary …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git branch-age`

Runs `ntk git branch-age` (see `-h` for details).

- **Call forms:** `ntk git branch-age …`  ·  `ntk-git-branch-age …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git branches`

Runs `ntk git branches` (see `-h` for details).

- **Call forms:** `ntk git branches …`  ·  `ntk-git-branches …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git changed-files`

Runs `ntk git changed-files` (see `-h` for details).

- **Call forms:** `ntk git changed-files …`  ·  `ntk-git-changed-files …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git clean-preview`

Runs `ntk git clean-preview` (see `-h` for details).

- **Call forms:** `ntk git clean-preview …`  ·  `ntk-git-clean-preview …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git commit-count`

Runs `ntk git commit-count` (see `-h` for details).

- **Call forms:** `ntk git commit-count …`  ·  `ntk-git-commit-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git config-list`

Runs `ntk git config-list` (see `-h` for details).

- **Call forms:** `ntk git config-list …`  ·  `ntk-git-config-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git contributors`

Runs `ntk git contributors` (see `-h` for details).

- **Call forms:** `ntk git contributors …`  ·  `ntk-git-contributors …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git current-branch`

Runs `ntk git current-branch` (see `-h` for details).

- **Call forms:** `ntk git current-branch …`  ·  `ntk-git-current-branch …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git diff-stat`

Runs `ntk git diff-stat` (see `-h` for details).

- **Call forms:** `ntk git diff-stat …`  ·  `ntk-git-diff-stat …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git fetch-dry`

Runs `ntk git fetch-dry` (see `-h` for details).

- **Call forms:** `ntk git fetch-dry …`  ·  `ntk-git-fetch-dry …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git file-history`

Runs `ntk git file-history` (see `-h` for details).

- **Call forms:** `ntk git file-history …`  ·  `ntk-git-file-history …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git first-commit`

Runs `ntk git first-commit` (see `-h` for details).

- **Call forms:** `ntk git first-commit …`  ·  `ntk-git-first-commit …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git gc-preview`

Runs `ntk git gc-preview` (see `-h` for details).

- **Call forms:** `ntk git gc-preview …`  ·  `ntk-git-gc-preview …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git ignored`

Runs `ntk git ignored` (see `-h` for details).

- **Call forms:** `ntk git ignored …`  ·  `ntk-git-ignored …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git is-repo`

Runs `ntk git is-repo` (see `-h` for details).

- **Call forms:** `ntk git is-repo …`  ·  `ntk-git-is-repo …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git largest-files`

Runs `ntk git largest-files` (see `-h` for details).

- **Call forms:** `ntk git largest-files …`  ·  `ntk-git-largest-files …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git last-commit`

Runs `ntk git last-commit` (see `-h` for details).

- **Call forms:** `ntk git last-commit …`  ·  `ntk-git-last-commit …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git log`

Runs `ntk git log` (see `-h` for details).

- **Call forms:** `ntk git log …`  ·  `ntk-git-log …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git orphan-branches`

Runs `ntk git orphan-branches` (see `-h` for details).

- **Call forms:** `ntk git orphan-branches …`  ·  `ntk-git-orphan-branches …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git remote-url`

Runs `ntk git remote-url` (see `-h` for details).

- **Call forms:** `ntk git remote-url …`  ·  `ntk-git-remote-url …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git remotes`

Runs `ntk git remotes` (see `-h` for details).

- **Call forms:** `ntk git remotes …`  ·  `ntk-git-remotes …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git root`

Runs `ntk git root` (see `-h` for details).

- **Call forms:** `ntk git root …`  ·  `ntk-git-root …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git staged`

Runs `ntk git staged` (see `-h` for details).

- **Call forms:** `ntk git staged …`  ·  `ntk-git-staged …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git stash-list`

Runs `ntk git stash-list` (see `-h` for details).

- **Call forms:** `ntk git stash-list …`  ·  `ntk-git-stash-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git status`

Runs `ntk git status` (see `-h` for details).

- **Call forms:** `ntk git status …`  ·  `ntk-git-status …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git tags`

Runs `ntk git tags` (see `-h` for details).

- **Call forms:** `ntk git tags …`  ·  `ntk-git-tags …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git unstaged`

Runs `ntk git unstaged` (see `-h` for details).

- **Call forms:** `ntk git unstaged …`  ·  `ntk-git-unstaged …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git untracked`

Runs `ntk git untracked` (see `-h` for details).

- **Call forms:** `ntk git untracked …`  ·  `ntk-git-untracked …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk git user-info`

Runs `ntk git user-info` (see `-h` for details).

- **Call forms:** `ntk git user-info …`  ·  `ntk-git-user-info …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="web"></a>`web` — Web, HTTP & API

_Web, HTTP & API. 31 tools._

### `ntk web api-get-json`

Run the api get json tool.

- **Call forms:** `ntk web api-get-json …`  ·  `ntk-web-api-get-json …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web bench`

Run the bench tool.

- **Call forms:** `ntk web bench …`  ·  `ntk-web-bench …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web cache-headers`

Run the cache headers tool.

- **Call forms:** `ntk web cache-headers …`  ·  `ntk-web-cache-headers …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web content-type`

Run the content type tool.

- **Call forms:** `ntk web content-type …`  ·  `ntk-web-content-type …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web cookies-show`

Run the cookies show tool.

- **Call forms:** `ntk web cookies-show …`  ·  `ntk-web-cookies-show …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web cors-check`

Run the cors check tool.

- **Call forms:** `ntk web cors-check …`  ·  `ntk-web-cors-check …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web download`

Run the download tool.

- **Call forms:** `ntk web download …`  ·  `ntk-web-download …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web favicon-url`

Run the favicon url tool.

- **Call forms:** `ntk web favicon-url …`  ·  `ntk-web-favicon-url …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web get`

Run the get tool.

- **Call forms:** `ntk web get …`  ·  `ntk-web-get …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web gzip-check`

Run the gzip check tool.

- **Call forms:** `ntk web gzip-check …`  ·  `ntk-web-gzip-check …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web head`

Run the head tool.

- **Call forms:** `ntk web head …`  ·  `ntk-web-head …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web headers`

Run the headers tool.

- **Call forms:** `ntk web headers …`  ·  `ntk-web-headers …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web http2-check`

Run the http2 check tool.

- **Call forms:** `ntk web http2-check …`  ·  `ntk-web-http2-check …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web ip-of-host`

Run the ip of host tool.

- **Call forms:** `ntk web ip-of-host …`  ·  `ntk-web-ip-of-host …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web json-endpoint-keys`

Run the json endpoint keys tool.

- **Call forms:** `ntk web json-endpoint-keys …`  ·  `ntk-web-json-endpoint-keys …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web links`

Run the links tool.

- **Call forms:** `ntk web links …`  ·  `ntk-web-links …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web meta-tags`

Run the meta tags tool.

- **Call forms:** `ntk web meta-tags …`  ·  `ntk-web-meta-tags …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web ping-http`

Run the ping http tool.

- **Call forms:** `ntk web ping-http …`  ·  `ntk-web-ping-http …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web post`

Run the post tool.

- **Call forms:** `ntk web post …`  ·  `ntk-web-post …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web query-parse`

Run the query parse tool.

- **Call forms:** `ntk web query-parse …`  ·  `ntk-web-query-parse …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web redirects`

Run the redirects tool.

- **Call forms:** `ntk web redirects …`  ·  `ntk-web-redirects …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web response-time`

Run the response time tool.

- **Call forms:** `ntk web response-time …`  ·  `ntk-web-response-time …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web robots`

Run the robots tool.

- **Call forms:** `ntk web robots …`  ·  `ntk-web-robots …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web security-headers`

Run the security headers tool.

- **Call forms:** `ntk web security-headers …`  ·  `ntk-web-security-headers …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web sitemap`

Run the sitemap tool.

- **Call forms:** `ntk web sitemap …`  ·  `ntk-web-sitemap …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web ssl-expiry-days`

Run the ssl expiry days tool.

- **Call forms:** `ntk web ssl-expiry-days …`  ·  `ntk-web-ssl-expiry-days …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web status`

Run the status tool.

- **Call forms:** `ntk web status …`  ·  `ntk-web-status …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web title`

Run the title tool.

- **Call forms:** `ntk web title …`  ·  `ntk-web-title …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web url-decode`

Run the url decode tool.

- **Call forms:** `ntk web url-decode …`  ·  `ntk-web-url-decode …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web url-encode`

Run the url encode tool.

- **Call forms:** `ntk web url-encode …`  ·  `ntk-web-url-encode …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk web user-agent-test`

Run the user agent test tool.

- **Call forms:** `ntk web user-agent-test …`  ·  `ntk-web-user-agent-test …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="media"></a>`media` — Media info & simple ops

_Media info & simple ops. 31 tools._

### `ntk media audio-info`

Run the audio info tool.

- **Call forms:** `ntk media audio-info …`  ·  `ntk-media-audio-info …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media batch-resize`

Run the batch resize tool.

- **Call forms:** `ntk media batch-resize …`  ·  `ntk-media-batch-resize …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media color-palette`

Run the color palette tool.

- **Call forms:** `ntk media color-palette …`  ·  `ntk-media-color-palette …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media contact-sheet`

Run the contact sheet tool.

- **Call forms:** `ntk media contact-sheet …`  ·  `ntk-media-contact-sheet …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media exif-show`

Run the exif show tool.

- **Call forms:** `ntk media exif-show …`  ·  `ntk-media-exif-show …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media exif-strip`

Run the exif strip tool.

- **Call forms:** `ntk media exif-strip …`  ·  `ntk-media-exif-strip …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media extract-audio`

Run the extract audio tool.

- **Call forms:** `ntk media extract-audio …`  ·  `ntk-media-extract-audio …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media favicon-make`

Run the favicon make tool.

- **Call forms:** `ntk media favicon-make …`  ·  `ntk-media-favicon-make …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media gif-frames`

Run the gif frames tool.

- **Call forms:** `ntk media gif-frames …`  ·  `ntk-media-gif-frames …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media image-blur`

Run the image blur tool.

- **Call forms:** `ntk media image-blur …`  ·  `ntk-media-image-blur …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media image-brightness`

Run the image brightness tool.

- **Call forms:** `ntk media image-brightness …`  ·  `ntk-media-image-brightness …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media image-compress`

Run the image compress tool.

- **Call forms:** `ntk media image-compress …`  ·  `ntk-media-image-compress …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media image-convert`

Run the image convert tool.

- **Call forms:** `ntk media image-convert …`  ·  `ntk-media-image-convert …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media image-crop`

Run the image crop tool.

- **Call forms:** `ntk media image-crop …`  ·  `ntk-media-image-crop …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media image-dimensions`

Run the image dimensions tool.

- **Call forms:** `ntk media image-dimensions …`  ·  `ntk-media-image-dimensions …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media image-dominant-color`

Run the image dominant color tool.

- **Call forms:** `ntk media image-dominant-color …`  ·  `ntk-media-image-dominant-color …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media image-flip`

Run the image flip tool.

- **Call forms:** `ntk media image-flip …`  ·  `ntk-media-image-flip …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media image-format-detect`

Run the image format detect tool.

- **Call forms:** `ntk media image-format-detect …`  ·  `ntk-media-image-format-detect …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media image-grayscale`

Run the image grayscale tool.

- **Call forms:** `ntk media image-grayscale …`  ·  `ntk-media-image-grayscale …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media image-info`

Run the image info tool.

- **Call forms:** `ntk media image-info …`  ·  `ntk-media-image-info …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media image-resize`

Run the image resize tool.

- **Call forms:** `ntk media image-resize …`  ·  `ntk-media-image-resize …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media image-rotate`

Run the image rotate tool.

- **Call forms:** `ntk media image-rotate …`  ·  `ntk-media-image-rotate …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media image-thumbnail`

Run the image thumbnail tool.

- **Call forms:** `ntk media image-thumbnail …`  ·  `ntk-media-image-thumbnail …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media images-count`

Run the images count tool.

- **Call forms:** `ntk media images-count …`  ·  `ntk-media-images-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media img-to-ascii`

Run the img to ascii tool.

- **Call forms:** `ntk media img-to-ascii …`  ·  `ntk-media-img-to-ascii …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media jpg-to-png`

Run the jpg to png tool.

- **Call forms:** `ntk media jpg-to-png …`  ·  `ntk-media-jpg-to-png …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media largest-image`

Run the largest image tool.

- **Call forms:** `ntk media largest-image …`  ·  `ntk-media-largest-image …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media png-to-jpg`

Run the png to jpg tool.

- **Call forms:** `ntk media png-to-jpg …`  ·  `ntk-media-png-to-jpg …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media qr-gen`

Run the qr gen tool.

- **Call forms:** `ntk media qr-gen …`  ·  `ntk-media-qr-gen …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media video-info`

Run the video info tool.

- **Call forms:** `ntk media video-info …`  ·  `ntk-media-video-info …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk media video-to-gif`

Run the video to gif tool.

- **Call forms:** `ntk media video-to-gif …`  ·  `ntk-media-video-to-gif …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="docker"></a>`docker` — Docker & containers

_Docker & containers. 31 tools._

### `ntk docker build`

Tool.

- **Call forms:** `ntk docker build …`  ·  `ntk-docker-build …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker build ...`
- **Parameters:** positional args: 1 known (args[0]); flags: --format

### `ntk docker compose-ps`

Tool.

- **Call forms:** `ntk docker compose-ps …`  ·  `ntk-docker-compose-ps …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker container-ips`

Tool.

- **Call forms:** `ntk docker container-ips …`  ·  `ntk-docker-container-ips …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker dangling-images`

Tool.

- **Call forms:** `ntk docker dangling-images …`  ·  `ntk-docker-dangling-images …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker disk-usage`

Tool.

- **Call forms:** `ntk docker disk-usage …`  ·  `ntk-docker-disk-usage …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker exec-hint`

Tool.

- **Call forms:** `ntk docker exec-hint …`  ·  `ntk-docker-exec-hint …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker exec-hint ...`
- **Parameters:** positional args: 1 known (args[0]); flags: --format

### `ntk docker healthcheck`

Tool.

- **Call forms:** `ntk docker healthcheck …`  ·  `ntk-docker-healthcheck …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker healthcheck ...`
- **Parameters:** positional args: 1 known (args[0]); flags: --format

### `ntk docker image-count`

Tool.

- **Call forms:** `ntk docker image-count …`  ·  `ntk-docker-image-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker images`

Tool.

- **Call forms:** `ntk docker images …`  ·  `ntk-docker-images …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker info`

Tool.

- **Call forms:** `ntk docker info …`  ·  `ntk-docker-info …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker inspect`

Tool.

- **Call forms:** `ntk docker inspect …`  ·  `ntk-docker-inspect …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker inspect ...`
- **Parameters:** positional args: 1 known (args[0]); flags: --format

### `ntk docker logs`

Tool.

- **Call forms:** `ntk docker logs …`  ·  `ntk-docker-logs …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker logs ...`
- **Parameters:** positional args: 1 known (args[0]); flags: --format

### `ntk docker networks`

Tool.

- **Call forms:** `ntk docker networks …`  ·  `ntk-docker-networks …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker port`

Tool.

- **Call forms:** `ntk docker port …`  ·  `ntk-docker-port …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker port ...`
- **Parameters:** positional args: 1 known (args[0]); flags: --format

### `ntk docker prune`

Tool.

- **Call forms:** `ntk docker prune …`  ·  `ntk-docker-prune …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker prune-preview`

Tool.

- **Call forms:** `ntk docker prune-preview …`  ·  `ntk-docker-prune-preview …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker ps`

Tool.

- **Call forms:** `ntk docker ps …`  ·  `ntk-docker-ps …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker ps-all`

Tool.

- **Call forms:** `ntk docker ps-all …`  ·  `ntk-docker-ps-all …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker pull`

Tool.

- **Call forms:** `ntk docker pull …`  ·  `ntk-docker-pull …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker pull ...`
- **Parameters:** positional args: 1 known (args[0]); flags: --format

### `ntk docker restart`

Tool.

- **Call forms:** `ntk docker restart …`  ·  `ntk-docker-restart …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker restart ...`
- **Parameters:** positional args: 1 known (args[0]); flags: --format

### `ntk docker rm`

Tool.

- **Call forms:** `ntk docker rm …`  ·  `ntk-docker-rm …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker rm ...`
- **Parameters:** positional args: 1 known (args[0]); flags: --format

### `ntk docker rmi`

Tool.

- **Call forms:** `ntk docker rmi …`  ·  `ntk-docker-rmi …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker rmi ...`
- **Parameters:** positional args: 1 known (args[0]); flags: --format

### `ntk docker running-count`

Tool.

- **Call forms:** `ntk docker running-count …`  ·  `ntk-docker-running-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker size-by-image`

Tool.

- **Call forms:** `ntk docker size-by-image …`  ·  `ntk-docker-size-by-image …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker start`

Tool.

- **Call forms:** `ntk docker start …`  ·  `ntk-docker-start …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker start ...`
- **Parameters:** positional args: 1 known (args[0]); flags: --format

### `ntk docker stats`

Tool.

- **Call forms:** `ntk docker stats …`  ·  `ntk-docker-stats …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** flags: --no-stream

### `ntk docker stop`

Tool.

- **Call forms:** `ntk docker stop …`  ·  `ntk-docker-stop …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker stop ...`
- **Parameters:** positional args: 1 known (args[0]); flags: --format

### `ntk docker tag`

Tool.

- **Call forms:** `ntk docker tag …`  ·  `ntk-docker-tag …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker tag ...`
- **Parameters:** positional args: 1 known (args[0]); flags: --format

### `ntk docker top`

Tool.

- **Call forms:** `ntk docker top …`  ·  `ntk-docker-top …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk docker top ...`
- **Parameters:** positional args: 1 known (args[0]); flags: --format

### `ntk docker version`

Tool.

- **Call forms:** `ntk docker version …`  ·  `ntk-docker-version …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk docker volumes`

Tool.

- **Call forms:** `ntk docker volumes …`  ·  `ntk-docker-volumes …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="cloud"></a>`cloud` — Cloud & DevOps

_Cloud & DevOps. 30 tools._

### `ntk cloud aws-arn-parse`

Tool.

- **Call forms:** `ntk cloud aws-arn-parse …`  ·  `ntk-cloud-aws-arn-parse …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud aws-arn-parse <value>`
- **Parameters:** accepts a variable list of args

### `ntk cloud aws-ec2-list`

Tool.

- **Call forms:** `ntk cloud aws-ec2-list …`  ·  `ntk-cloud-aws-ec2-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud aws-identity`

Tool.

- **Call forms:** `ntk cloud aws-identity …`  ·  `ntk-cloud-aws-identity …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud aws-regions`

Tool.

- **Call forms:** `ntk cloud aws-regions …`  ·  `ntk-cloud-aws-regions …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud aws-s3-ls`

Tool.

- **Call forms:** `ntk cloud aws-s3-ls …`  ·  `ntk-cloud-aws-s3-ls …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud az-account`

Tool.

- **Call forms:** `ntk cloud az-account …`  ·  `ntk-cloud-az-account …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud cloud-init-gen`

Tool.

- **Call forms:** `ntk cloud cloud-init-gen …`  ·  `ntk-cloud-cloud-init-gen …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud cloud-init-gen <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk cloud cron-yaml-gen`

Tool.

- **Call forms:** `ntk cloud cron-yaml-gen …`  ·  `ntk-cloud-cron-yaml-gen …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud cron-yaml-gen <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk cloud dockerfile-gen`

Tool.

- **Call forms:** `ntk cloud dockerfile-gen …`  ·  `ntk-cloud-dockerfile-gen …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud dockerfile-gen <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk cloud dockerhub-tags`

Tool.

- **Call forms:** `ntk cloud dockerhub-tags …`  ·  `ntk-cloud-dockerhub-tags …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud dockerhub-tags <value>`
- **Parameters:** accepts a variable list of args

### `ntk cloud env-to-k8s-secret`

Tool.

- **Call forms:** `ntk cloud env-to-k8s-secret …`  ·  `ntk-cloud-env-to-k8s-secret …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud env-to-k8s-secret <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk cloud gcloud-config`

Tool.

- **Call forms:** `ntk cloud gcloud-config …`  ·  `ntk-cloud-gcloud-config …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud gcloud-project`

Tool.

- **Call forms:** `ntk cloud gcloud-project …`  ·  `ntk-cloud-gcloud-project …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud gcp-zones-list`

Tool.

- **Call forms:** `ntk cloud gcp-zones-list …`  ·  `ntk-cloud-gcp-zones-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud gh-rate-limit`

Tool.

- **Call forms:** `ntk cloud gh-rate-limit …`  ·  `ntk-cloud-gh-rate-limit …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud gh-rate-limit <value>`
- **Parameters:** accepts a variable list of args

### `ntk cloud gh-releases`

Tool.

- **Call forms:** `ntk cloud gh-releases …`  ·  `ntk-cloud-gh-releases …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud gh-releases <value>`
- **Parameters:** accepts a variable list of args

### `ntk cloud gh-repo-info`

Tool.

- **Call forms:** `ntk cloud gh-repo-info …`  ·  `ntk-cloud-gh-repo-info …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud gh-repo-info <value>`
- **Parameters:** accepts a variable list of args

### `ntk cloud helm-list`

Tool.

- **Call forms:** `ntk cloud helm-list …`  ·  `ntk-cloud-helm-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud k8s-namespace-gen`

Tool.

- **Call forms:** `ntk cloud k8s-namespace-gen …`  ·  `ntk-cloud-k8s-namespace-gen …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud k8s-namespace-gen <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk cloud k8s-yaml-gen`

Tool.

- **Call forms:** `ntk cloud k8s-yaml-gen …`  ·  `ntk-cloud-k8s-yaml-gen …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud k8s-yaml-gen <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk cloud kube-ctx`

Tool.

- **Call forms:** `ntk cloud kube-ctx …`  ·  `ntk-cloud-kube-ctx …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud kube-deploy`

Tool.

- **Call forms:** `ntk cloud kube-deploy …`  ·  `ntk-cloud-kube-deploy …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud kube-events`

Tool.

- **Call forms:** `ntk cloud kube-events …`  ·  `ntk-cloud-kube-events …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud kube-events <value>`
- **Parameters:** accepts a variable list of args

### `ntk cloud kube-logs`

Tool.

- **Call forms:** `ntk cloud kube-logs …`  ·  `ntk-cloud-kube-logs …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud kube-logs <value>`
- **Parameters:** accepts a variable list of args

### `ntk cloud kube-nodes`

Tool.

- **Call forms:** `ntk cloud kube-nodes …`  ·  `ntk-cloud-kube-nodes …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud kube-ns`

Tool.

- **Call forms:** `ntk cloud kube-ns …`  ·  `ntk-cloud-kube-ns …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud kube-pods`

Tool.

- **Call forms:** `ntk cloud kube-pods …`  ·  `ntk-cloud-kube-pods …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud kube-svc`

Tool.

- **Call forms:** `ntk cloud kube-svc …`  ·  `ntk-cloud-kube-svc …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk cloud s3-url-parse`

Tool.

- **Call forms:** `ntk cloud s3-url-parse …`  ·  `ntk-cloud-s3-url-parse …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk cloud s3-url-parse <value>`
- **Parameters:** accepts a variable list of args

### `ntk cloud tf-fmt-check`

Tool.

- **Call forms:** `ntk cloud tf-fmt-check …`  ·  `ntk-cloud-tf-fmt-check …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="database"></a>`database` — Database tools

_Database tools. 30 tools._

### `ntk database connection-string-parse`

connection-string-parse tool.

- **Call forms:** `ntk database connection-string-parse …`  ·  `ntk-database-connection-string-parse …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database connection-string-parse <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database csv-to-sqlite`

csv-to-sqlite tool.

- **Call forms:** `ntk database csv-to-sqlite …`  ·  `ntk-database-csv-to-sqlite …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database csv-to-sqlite <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database db-url-parse`

db-url-parse tool.

- **Call forms:** `ntk database db-url-parse …`  ·  `ntk-database-db-url-parse …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database db-url-parse <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database json-to-sqlite`

json-to-sqlite tool.

- **Call forms:** `ntk database json-to-sqlite …`  ·  `ntk-database-json-to-sqlite …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database json-to-sqlite <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database mysql-url-parse`

mysql-url-parse tool.

- **Call forms:** `ntk database mysql-url-parse …`  ·  `ntk-database-mysql-url-parse …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database mysql-url-parse <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database pg-url-parse`

pg-url-parse tool.

- **Call forms:** `ntk database pg-url-parse …`  ·  `ntk-database-pg-url-parse …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database pg-url-parse <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database redis-ping`

redis-ping tool.

- **Call forms:** `ntk database redis-ping …`  ·  `ntk-database-redis-ping …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database redis-ping <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database rows-count-all`

rows-count-all tool.

- **Call forms:** `ntk database rows-count-all …`  ·  `ntk-database-rows-count-all …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database rows-count-all <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sql-format`

sql-format tool.

- **Call forms:** `ntk database sql-format …`  ·  `ntk-database-sql-format …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sql-format <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-backup`

sqlite-backup tool.

- **Call forms:** `ntk database sqlite-backup …`  ·  `ntk-database-sqlite-backup …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-backup <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-columns`

sqlite-columns tool.

- **Call forms:** `ntk database sqlite-columns …`  ·  `ntk-database-sqlite-columns …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-columns <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-count`

sqlite-count tool.

- **Call forms:** `ntk database sqlite-count …`  ·  `ntk-database-sqlite-count …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-count <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-create`

sqlite-create tool.

- **Call forms:** `ntk database sqlite-create …`  ·  `ntk-database-sqlite-create …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-create <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-distinct`

sqlite-distinct tool.

- **Call forms:** `ntk database sqlite-distinct …`  ·  `ntk-database-sqlite-distinct …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-distinct <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-drop`

sqlite-drop tool.

- **Call forms:** `ntk database sqlite-drop …`  ·  `ntk-database-sqlite-drop …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-drop <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-dump`

sqlite-dump tool.

- **Call forms:** `ntk database sqlite-dump …`  ·  `ntk-database-sqlite-dump …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-dump <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-export-json`

sqlite-export-json tool.

- **Call forms:** `ntk database sqlite-export-json …`  ·  `ntk-database-sqlite-export-json …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-export-json <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-head`

sqlite-head tool.

- **Call forms:** `ntk database sqlite-head …`  ·  `ntk-database-sqlite-head …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-head <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-indexes`

sqlite-indexes tool.

- **Call forms:** `ntk database sqlite-indexes …`  ·  `ntk-database-sqlite-indexes …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-indexes <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-info`

sqlite-info tool.

- **Call forms:** `ntk database sqlite-info …`  ·  `ntk-database-sqlite-info …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-info <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-integrity`

sqlite-integrity tool.

- **Call forms:** `ntk database sqlite-integrity …`  ·  `ntk-database-sqlite-integrity …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-integrity <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-min-max`

sqlite-min-max tool.

- **Call forms:** `ntk database sqlite-min-max …`  ·  `ntk-database-sqlite-min-max …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-min-max <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-pragma`

sqlite-pragma tool.

- **Call forms:** `ntk database sqlite-pragma …`  ·  `ntk-database-sqlite-pragma …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-pragma <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-query`

sqlite-query tool.

- **Call forms:** `ntk database sqlite-query …`  ·  `ntk-database-sqlite-query …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-query <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-random-row`

sqlite-random-row tool.

- **Call forms:** `ntk database sqlite-random-row …`  ·  `ntk-database-sqlite-random-row …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-random-row <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-schema`

sqlite-schema tool.

- **Call forms:** `ntk database sqlite-schema …`  ·  `ntk-database-sqlite-schema …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-schema <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-size`

sqlite-size tool.

- **Call forms:** `ntk database sqlite-size …`  ·  `ntk-database-sqlite-size …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-size <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-tables`

sqlite-tables tool.

- **Call forms:** `ntk database sqlite-tables …`  ·  `ntk-database-sqlite-tables …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-tables <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-to-csv`

sqlite-to-csv tool.

- **Call forms:** `ntk database sqlite-to-csv …`  ·  `ntk-database-sqlite-to-csv …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-to-csv <db>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk database sqlite-vacuum`

sqlite-vacuum tool.

- **Call forms:** `ntk database sqlite-vacuum …`  ·  `ntk-database-sqlite-vacuum …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk database sqlite-vacuum <db>`
- **Parameters:** positional args: 1 known (args[0])


## <a id="math"></a>`math` — Math, stats & number tools

_Math, stats & number tools. 40 tools._

### `ntk math abs`

Absolute value.

- **Call forms:** `ntk math abs …`  ·  `ntk-math-abs …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math abs <n>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk math average-list`

Average of a comma list.

- **Call forms:** `ntk math average-list …`  ·  `ntk-math-average-list …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math average-list <n1,n2,...>`
- **Parameters:** accepts a variable list of args

### `ntk math base-convert`

Convert integer between bases: n from to.

- **Call forms:** `ntk math base-convert …`  ·  `ntk-math-base-convert …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math base-convert <n> <from> <to>`
- **Parameters:** positional args: 3 known (args[0], args[1], args[2])

### `ntk math bin`

Decimal to binary.

- **Call forms:** `ntk math bin …`  ·  `ntk-math-bin …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math bin <n>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk math calc`

Evaluate a math expression, e.g. 2*(3+4).

- **Call forms:** `ntk math calc …`  ·  `ntk-math-calc …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math calc <expr>`
- **Parameters:** accepts a variable list of args

### `ntk math clamp`

Clamp n to [lo,hi].

- **Call forms:** `ntk math clamp …`  ·  `ntk-math-clamp …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math clamp <n> <lo> <hi>`
- **Parameters:** positional args: 3 known (args[0], args[1], args[2])

### `ntk math combinations`

Combinations C(n,r).

- **Call forms:** `ntk math combinations …`  ·  `ntk-math-combinations …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math combinations <n> <r>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk math deg-to-rad`

Degrees to radians.

- **Call forms:** `ntk math deg-to-rad …`  ·  `ntk-math-deg-to-rad …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math deg-to-rad <deg>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk math dice`

Roll dice, e.g. 2d6.

- **Call forms:** `ntk math dice …`  ·  `ntk-math-dice …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math dice <NdM>  e.g. 2d6`
- **Parameters:** positional args: 1 known (args[0])

### `ntk math factorial`

Factorial of n.

- **Call forms:** `ntk math factorial …`  ·  `ntk-math-factorial …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math factorial <n>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk math fibonacci`

First n Fibonacci numbers.

- **Call forms:** `ntk math fibonacci …`  ·  `ntk-math-fibonacci …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math fibonacci <n>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk math from-roman`

Roman numeral to integer.

- **Call forms:** `ntk math from-roman …`  ·  `ntk-math-from-roman …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math from-roman <ROMAN>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk math gcd`

Greatest common divisor.

- **Call forms:** `ntk math gcd …`  ·  `ntk-math-gcd …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math gcd <a> <b> ...`
- **Parameters:** accepts a variable list of args

### `ntk math hex`

Decimal to hexadecimal.

- **Call forms:** `ntk math hex …`  ·  `ntk-math-hex …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math hex <n>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk math is-square`

Check if a number is a perfect square.

- **Call forms:** `ntk math is-square …`  ·  `ntk-math-is-square …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math is-square <n>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk math lcm`

Least common multiple.

- **Call forms:** `ntk math lcm …`  ·  `ntk-math-lcm …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math lcm <a> <b> ...`
- **Parameters:** accepts a variable list of args

### `ntk math log`

Logarithm (base optional, default e).

- **Call forms:** `ntk math log …`  ·  `ntk-math-log …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math log <x> [base]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk math max`

Maximum value.

- **Call forms:** `ntk math max …`  ·  `ntk-math-max …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk math mean`

Arithmetic mean of numbers.

- **Call forms:** `ntk math mean …`  ·  `ntk-math-mean …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk math median`

Median of numbers.

- **Call forms:** `ntk math median …`  ·  `ntk-math-median …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk math min`

Minimum value.

- **Call forms:** `ntk math min …`  ·  `ntk-math-min …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk math mode`

Most common value.

- **Call forms:** `ntk math mode …`  ·  `ntk-math-mode …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk math oct`

Decimal to octal.

- **Call forms:** `ntk math oct …`  ·  `ntk-math-oct …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math oct <n>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk math percent`

x is what percent of y.

- **Call forms:** `ntk math percent …`  ·  `ntk-math-percent …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math percent <x> <y>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk math percent-change`

Percent change from a to b.

- **Call forms:** `ntk math percent-change …`  ·  `ntk-math-percent-change …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math percent-change <old> <new>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk math permutations`

Permutations P(n,r).

- **Call forms:** `ntk math permutations …`  ·  `ntk-math-permutations …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math permutations <n> <r>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk math pow`

x raised to y.

- **Call forms:** `ntk math pow …`  ·  `ntk-math-pow …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math pow <x> <y>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk math prime-check`

Check if a number is prime.

- **Call forms:** `ntk math prime-check …`  ·  `ntk-math-prime-check …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math prime-check <n>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk math primes-upto`

List primes up to n.

- **Call forms:** `ntk math primes-upto …`  ·  `ntk-math-primes-upto …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math primes-upto <n>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk math product`

Product of numbers.

- **Call forms:** `ntk math product …`  ·  `ntk-math-product …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk math quadratic`

Solve ax^2+bx+c=0: a b c.

- **Call forms:** `ntk math quadratic …`  ·  `ntk-math-quadratic …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math quadratic <a> <b> <c>`
- **Parameters:** positional args: 3 known (args[0], args[1], args[2])

### `ntk math rad-to-deg`

Radians to degrees.

- **Call forms:** `ntk math rad-to-deg …`  ·  `ntk-math-rad-to-deg …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math rad-to-deg <rad>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk math random-int`

Random integer in [a,b].

- **Call forms:** `ntk math random-int …`  ·  `ntk-math-random-int …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math random-int <a> <b>`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk math range`

Range (max-min).

- **Call forms:** `ntk math range …`  ·  `ntk-math-range …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk math roman`

Integer to Roman numeral.

- **Call forms:** `ntk math roman …`  ·  `ntk-math-roman …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math roman <1-3999>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk math round-to`

Round n to d decimals.

- **Call forms:** `ntk math round-to …`  ·  `ntk-math-round-to …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math round-to <n> [decimals]`
- **Parameters:** positional args: 2 known (args[0], args[1])

### `ntk math sqrt`

Square root.

- **Call forms:** `ntk math sqrt …`  ·  `ntk-math-sqrt …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk math sqrt <n>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk math stdev`

Standard deviation.

- **Call forms:** `ntk math stdev …`  ·  `ntk-math-stdev …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk math sum`

Sum of numbers.

- **Call forms:** `ntk math sum …`  ·  `ntk-math-sum …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk math variance`

Variance.

- **Call forms:** `ntk math variance …`  ·  `ntk-math-variance …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="time"></a>`time` — Date, time, timers & zones

_Date, time, timers & zones. 31 tools._

### `ntk time add-days`

add-days tool.

- **Call forms:** `ntk time add-days …`  ·  `ntk-time-add-days …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time add-days [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time age`

age tool.

- **Call forms:** `ntk time age …`  ·  `ntk-time-age …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time age [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time business-days`

business-days tool.

- **Call forms:** `ntk time business-days …`  ·  `ntk-time-business-days …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time business-days [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time calendar`

calendar tool.

- **Call forms:** `ntk time calendar …`  ·  `ntk-time-calendar …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time calendar [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time countdown`

countdown tool.

- **Call forms:** `ntk time countdown …`  ·  `ntk-time-countdown …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time countdown [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time date-to-epoch`

date-to-epoch tool.

- **Call forms:** `ntk time date-to-epoch …`  ·  `ntk-time-date-to-epoch …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time date-to-epoch [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time day-of-year`

day-of-year tool.

- **Call forms:** `ntk time day-of-year …`  ·  `ntk-time-day-of-year …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time day-of-year [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time days-until`

days-until tool.

- **Call forms:** `ntk time days-until …`  ·  `ntk-time-days-until …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time days-until [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time diff-days`

diff-days tool.

- **Call forms:** `ntk time diff-days …`  ·  `ntk-time-diff-days …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time diff-days [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time duration-humanize`

duration-humanize tool.

- **Call forms:** `ntk time duration-humanize …`  ·  `ntk-time-duration-humanize …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time duration-humanize [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time epoch`

epoch tool.

- **Call forms:** `ntk time epoch …`  ·  `ntk-time-epoch …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time epoch [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time epoch-to-date`

epoch-to-date tool.

- **Call forms:** `ntk time epoch-to-date …`  ·  `ntk-time-epoch-to-date …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time epoch-to-date [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time format`

format tool.

- **Call forms:** `ntk time format …`  ·  `ntk-time-format …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time format [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time is-leap`

is-leap tool.

- **Call forms:** `ntk time is-leap …`  ·  `ntk-time-is-leap …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time is-leap [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time iso-now`

iso-now tool.

- **Call forms:** `ntk time iso-now …`  ·  `ntk-time-iso-now …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time iso-now [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time iso-to-unix`

iso-to-unix tool.

- **Call forms:** `ntk time iso-to-unix …`  ·  `ntk-time-iso-to-unix …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time iso-to-unix [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time month-name`

month-name tool.

- **Call forms:** `ntk time month-name …`  ·  `ntk-time-month-name …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time month-name [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time now`

now tool.

- **Call forms:** `ntk time now …`  ·  `ntk-time-now …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time now [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time parse`

parse tool.

- **Call forms:** `ntk time parse …`  ·  `ntk-time-parse …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time parse [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time quarter`

quarter tool.

- **Call forms:** `ntk time quarter …`  ·  `ntk-time-quarter …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time quarter [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time seconds-until`

seconds-until tool.

- **Call forms:** `ntk time seconds-until …`  ·  `ntk-time-seconds-until …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time seconds-until [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time sleep`

sleep tool.

- **Call forms:** `ntk time sleep …`  ·  `ntk-time-sleep …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time sleep [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time time-in`

time-in tool.

- **Call forms:** `ntk time time-in …`  ·  `ntk-time-time-in …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time time-in [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time timestamp-ms`

timestamp-ms tool.

- **Call forms:** `ntk time timestamp-ms …`  ·  `ntk-time-timestamp-ms …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time timestamp-ms [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time timezone`

timezone tool.

- **Call forms:** `ntk time timezone …`  ·  `ntk-time-timezone …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time timezone [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time timezones-list`

timezones-list tool.

- **Call forms:** `ntk time timezones-list …`  ·  `ntk-time-timezones-list …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time timezones-list [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time unix-to-iso`

unix-to-iso tool.

- **Call forms:** `ntk time unix-to-iso …`  ·  `ntk-time-unix-to-iso …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time unix-to-iso [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time utc-now`

utc-now tool.

- **Call forms:** `ntk time utc-now …`  ·  `ntk-time-utc-now …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time utc-now [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time week-number`

week-number tool.

- **Call forms:** `ntk time week-number …`  ·  `ntk-time-week-number …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time week-number [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time weekday`

weekday tool.

- **Call forms:** `ntk time weekday …`  ·  `ntk-time-weekday …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time weekday [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk time world-clock`

world-clock tool.

- **Call forms:** `ntk time world-clock …`  ·  `ntk-time-world-clock …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk time world-clock [value]`
- **Parameters:** positional args: 1 known (args[0])


## <a id="convert"></a>`convert` — Units & format conversion

_Units & format conversion. 31 tools._

### `ntk convert angle`

angle tool.

- **Call forms:** `ntk convert angle …`  ·  `ntk-convert-angle …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert angle <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert area`

area tool.

- **Call forms:** `ntk convert area …`  ·  `ntk-convert-area …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert area <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert ascii-to-hex`

ascii-to-hex tool.

- **Call forms:** `ntk convert ascii-to-hex …`  ·  `ntk-convert-ascii-to-hex …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert ascii-to-hex <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert bin-to-dec`

bin-to-dec tool.

- **Call forms:** `ntk convert bin-to-dec …`  ·  `ntk-convert-bin-to-dec …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert bin-to-dec <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert celsius-fahrenheit`

celsius-fahrenheit tool.

- **Call forms:** `ntk convert celsius-fahrenheit …`  ·  `ntk-convert-celsius-fahrenheit …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert celsius-fahrenheit <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert cm-inch`

cm-inch tool.

- **Call forms:** `ntk convert cm-inch …`  ·  `ntk-convert-cm-inch …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert cm-inch <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert data`

data tool.

- **Call forms:** `ntk convert data …`  ·  `ntk-convert-data …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert data <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert dec-to-bin`

dec-to-bin tool.

- **Call forms:** `ntk convert dec-to-bin …`  ·  `ntk-convert-dec-to-bin …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert dec-to-bin <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert dec-to-hex`

dec-to-hex tool.

- **Call forms:** `ntk convert dec-to-hex …`  ·  `ntk-convert-dec-to-hex …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert dec-to-hex <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert energy`

energy tool.

- **Call forms:** `ntk convert energy …`  ·  `ntk-convert-energy …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert energy <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert fahrenheit-celsius`

fahrenheit-celsius tool.

- **Call forms:** `ntk convert fahrenheit-celsius …`  ·  `ntk-convert-fahrenheit-celsius …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert fahrenheit-celsius <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert hex-to-ascii`

hex-to-ascii tool.

- **Call forms:** `ntk convert hex-to-ascii …`  ·  `ntk-convert-hex-to-ascii …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert hex-to-ascii <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert hex-to-dec`

hex-to-dec tool.

- **Call forms:** `ntk convert hex-to-dec …`  ·  `ntk-convert-hex-to-dec …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert hex-to-dec <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert hex-to-rgb`

hex-to-rgb tool.

- **Call forms:** `ntk convert hex-to-rgb …`  ·  `ntk-convert-hex-to-rgb …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert hex-to-rgb <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert inch-cm`

inch-cm tool.

- **Call forms:** `ntk convert inch-cm …`  ·  `ntk-convert-inch-cm …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert inch-cm <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert kg-lbs`

kg-lbs tool.

- **Call forms:** `ntk convert kg-lbs …`  ·  `ntk-convert-kg-lbs …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert kg-lbs <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert km-miles`

km-miles tool.

- **Call forms:** `ntk convert km-miles …`  ·  `ntk-convert-km-miles …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert km-miles <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert lbs-kg`

lbs-kg tool.

- **Call forms:** `ntk convert lbs-kg …`  ·  `ntk-convert-lbs-kg …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert lbs-kg <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert length`

length tool.

- **Call forms:** `ntk convert length …`  ·  `ntk-convert-length …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert length <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert liter-gallon`

liter-gallon tool.

- **Call forms:** `ntk convert liter-gallon …`  ·  `ntk-convert-liter-gallon …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert liter-gallon <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert mass`

mass tool.

- **Call forms:** `ntk convert mass …`  ·  `ntk-convert-mass …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert mass <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert miles-km`

miles-km tool.

- **Call forms:** `ntk convert miles-km …`  ·  `ntk-convert-miles-km …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert miles-km <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert number-to-words`

number-to-words tool.

- **Call forms:** `ntk convert number-to-words …`  ·  `ntk-convert-number-to-words …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert number-to-words <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert pressure`

pressure tool.

- **Call forms:** `ntk convert pressure …`  ·  `ntk-convert-pressure …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert pressure <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert rgb-to-hex`

rgb-to-hex tool.

- **Call forms:** `ntk convert rgb-to-hex …`  ·  `ntk-convert-rgb-to-hex …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert rgb-to-hex <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert speed`

speed tool.

- **Call forms:** `ntk convert speed …`  ·  `ntk-convert-speed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert speed <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert temp`

temp tool.

- **Call forms:** `ntk convert temp …`  ·  `ntk-convert-temp …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert temp <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert time-unit`

time-unit tool.

- **Call forms:** `ntk convert time-unit …`  ·  `ntk-convert-time-unit …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert time-unit <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert unit-list`

unit-list tool.

- **Call forms:** `ntk convert unit-list …`  ·  `ntk-convert-unit-list …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert unit-list <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert utf8-bytes`

utf8-bytes tool.

- **Call forms:** `ntk convert utf8-bytes …`  ·  `ntk-convert-utf8-bytes …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert utf8-bytes <value>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk convert volume`

volume tool.

- **Call forms:** `ntk convert volume …`  ·  `ntk-convert-volume …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk convert volume <value>`
- **Parameters:** positional args: 1 known (args[0])


## <a id="generate"></a>`generate` — Generators (passwords, UUID, QR, ...)

_Generators (passwords, UUID, QR, ...). 31 tools._

### `ntk generate api-key`

api-key tool.

- **Call forms:** `ntk generate api-key …`  ·  `ntk-generate-api-key …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate api-key [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate base64-random`

base64-random tool.

- **Call forms:** `ntk generate base64-random …`  ·  `ntk-generate-base64-random …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate base64-random [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate color`

color tool.

- **Call forms:** `ntk generate color …`  ·  `ntk-generate-color …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate color [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate color-palette`

color-palette tool.

- **Call forms:** `ntk generate color-palette …`  ·  `ntk-generate-color-palette …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate color-palette [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate credit-card`

credit-card tool.

- **Call forms:** `ntk generate credit-card …`  ·  `ntk-generate-credit-card …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate credit-card [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate date-random`

date-random tool.

- **Call forms:** `ntk generate date-random …`  ·  `ntk-generate-date-random …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate date-random [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate email`

email tool.

- **Call forms:** `ntk generate email …`  ·  `ntk-generate-email …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate email [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate hash-salt`

hash-salt tool.

- **Call forms:** `ntk generate hash-salt …`  ·  `ntk-generate-hash-salt …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate hash-salt [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate hex`

hex tool.

- **Call forms:** `ntk generate hex …`  ·  `ntk-generate-hex …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate hex [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate ipv4`

ipv4 tool.

- **Call forms:** `ntk generate ipv4 …`  ·  `ntk-generate-ipv4 …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate ipv4 [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate ipv6`

ipv6 tool.

- **Call forms:** `ntk generate ipv6 …`  ·  `ntk-generate-ipv6 …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate ipv6 [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate lorem`

lorem tool.

- **Call forms:** `ntk generate lorem …`  ·  `ntk-generate-lorem …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate lorem [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate lorem-paragraphs`

lorem-paragraphs tool.

- **Call forms:** `ntk generate lorem-paragraphs …`  ·  `ntk-generate-lorem-paragraphs …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate lorem-paragraphs [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate mac-address`

mac-address tool.

- **Call forms:** `ntk generate mac-address …`  ·  `ntk-generate-mac-address …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate mac-address [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate name`

name tool.

- **Call forms:** `ntk generate name …`  ·  `ntk-generate-name …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate name [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate otp-secret`

otp-secret tool.

- **Call forms:** `ntk generate otp-secret …`  ·  `ntk-generate-otp-secret …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate otp-secret [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate passphrase`

passphrase tool.

- **Call forms:** `ntk generate passphrase …`  ·  `ntk-generate-passphrase …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate passphrase [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate passphrase-dashed`

passphrase-dashed tool.

- **Call forms:** `ntk generate passphrase-dashed …`  ·  `ntk-generate-passphrase-dashed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate passphrase-dashed [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate password`

password tool.

- **Call forms:** `ntk generate password …`  ·  `ntk-generate-password …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate password [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate phone`

phone tool.

- **Call forms:** `ntk generate phone …`  ·  `ntk-generate-phone …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate phone [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate pin`

pin tool.

- **Call forms:** `ntk generate pin …`  ·  `ntk-generate-pin …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate pin [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate random-pick`

random-pick tool.

- **Call forms:** `ntk generate random-pick …`  ·  `ntk-generate-random-pick …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate random-pick [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate sentence`

sentence tool.

- **Call forms:** `ntk generate sentence …`  ·  `ntk-generate-sentence …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate sentence [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate slug`

slug tool.

- **Call forms:** `ntk generate slug …`  ·  `ntk-generate-slug …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate slug [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate strong-password`

strong-password tool.

- **Call forms:** `ntk generate strong-password …`  ·  `ntk-generate-strong-password …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate strong-password [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate token`

token tool.

- **Call forms:** `ntk generate token …`  ·  `ntk-generate-token …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate token [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate username`

username tool.

- **Call forms:** `ntk generate username …`  ·  `ntk-generate-username …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate username [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate uuid`

uuid tool.

- **Call forms:** `ntk generate uuid …`  ·  `ntk-generate-uuid …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate uuid [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate uuid-batch`

uuid-batch tool.

- **Call forms:** `ntk generate uuid-batch …`  ·  `ntk-generate-uuid-batch …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate uuid-batch [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate uuid5`

uuid5 tool.

- **Call forms:** `ntk generate uuid5 …`  ·  `ntk-generate-uuid5 …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate uuid5 [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk generate word`

word tool.

- **Call forms:** `ntk generate word …`  ·  `ntk-generate-word …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk generate word [value]`
- **Parameters:** positional args: 1 known (args[0])


## <a id="monitor"></a>`monitor` — Live system monitors

_Live system monitors. 31 tools._

### `ntk monitor battery`

battery tool.

- **Call forms:** `ntk monitor battery …`  ·  `ntk-monitor-battery …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor battery [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor boot-time`

boot-time tool.

- **Call forms:** `ntk monitor boot-time …`  ·  `ntk-monitor-boot-time …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor boot-time [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor connections-count`

connections-count tool.

- **Call forms:** `ntk monitor connections-count …`  ·  `ntk-monitor-connections-count …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor connections-count [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor cpu`

cpu tool.

- **Call forms:** `ntk monitor cpu …`  ·  `ntk-monitor-cpu …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor cpu [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor cpu-freq`

cpu-freq tool.

- **Call forms:** `ntk monitor cpu-freq …`  ·  `ntk-monitor-cpu-freq …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor cpu-freq [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor cpu-per-core`

cpu-per-core tool.

- **Call forms:** `ntk monitor cpu-per-core …`  ·  `ntk-monitor-cpu-per-core …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor cpu-per-core [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor cpu-times`

cpu-times tool.

- **Call forms:** `ntk monitor cpu-times …`  ·  `ntk-monitor-cpu-times …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor cpu-times [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor disk-io`

disk-io tool.

- **Call forms:** `ntk monitor disk-io …`  ·  `ntk-monitor-disk-io …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor disk-io [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor disk-percent`

disk-percent tool.

- **Call forms:** `ntk monitor disk-percent …`  ·  `ntk-monitor-disk-percent …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor disk-percent [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor disk-usage`

disk-usage tool.

- **Call forms:** `ntk monitor disk-usage …`  ·  `ntk-monitor-disk-usage …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `available`
    - `ntk monitor disk-usage [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor gpu`

gpu tool.

- **Call forms:** `ntk monitor gpu …`  ·  `ntk-monitor-gpu …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor gpu [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor io-counters`

io-counters tool.

- **Call forms:** `ntk monitor io-counters …`  ·  `ntk-monitor-io-counters …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor io-counters [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor listening-ports`

listening-ports tool.

- **Call forms:** `ntk monitor listening-ports …`  ·  `ntk-monitor-listening-ports …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor listening-ports [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor load`

load tool.

- **Call forms:** `ntk monitor load …`  ·  `ntk-monitor-load …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor load [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor mem`

mem tool.

- **Call forms:** `ntk monitor mem …`  ·  `ntk-monitor-mem …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor mem [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor memory-percent`

memory-percent tool.

- **Call forms:** `ntk monitor memory-percent …`  ·  `ntk-monitor-memory-percent …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor memory-percent [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor net-counters`

net-counters tool.

- **Call forms:** `ntk monitor net-counters …`  ·  `ntk-monitor-net-counters …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor net-counters [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor net-io`

net-io tool.

- **Call forms:** `ntk monitor net-io …`  ·  `ntk-monitor-net-io …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor net-io [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor net-speed`

net-speed tool.

- **Call forms:** `ntk monitor net-speed …`  ·  `ntk-monitor-net-speed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor net-speed [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor per-disk-usage`

per-disk-usage tool.

- **Call forms:** `ntk monitor per-disk-usage …`  ·  `ntk-monitor-per-disk-usage …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `available`
    - `ntk monitor per-disk-usage [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor process-count`

process-count tool.

- **Call forms:** `ntk monitor process-count …`  ·  `ntk-monitor-process-count …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor process-count [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor processes`

processes tool.

- **Call forms:** `ntk monitor processes …`  ·  `ntk-monitor-processes …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor processes [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor swap`

swap tool.

- **Call forms:** `ntk monitor swap …`  ·  `ntk-monitor-swap …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor swap [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor temps`

temps tool.

- **Call forms:** `ntk monitor temps …`  ·  `ntk-monitor-temps …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor temps [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor threads`

threads tool.

- **Call forms:** `ntk monitor threads …`  ·  `ntk-monitor-threads …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor threads [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor top-cpu`

top-cpu tool.

- **Call forms:** `ntk monitor top-cpu …`  ·  `ntk-monitor-top-cpu …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor top-cpu [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor top-mem`

top-mem tool.

- **Call forms:** `ntk monitor top-mem …`  ·  `ntk-monitor-top-mem …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor top-mem [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor uptime`

uptime tool.

- **Call forms:** `ntk monitor uptime …`  ·  `ntk-monitor-uptime …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor uptime [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor users-logged`

users-logged tool.

- **Call forms:** `ntk monitor users-logged …`  ·  `ntk-monitor-users-logged …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor users-logged [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor watch-cpu`

watch-cpu tool.

- **Call forms:** `ntk monitor watch-cpu …`  ·  `ntk-monitor-watch-cpu …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor watch-cpu [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk monitor watch-mem`

watch-mem tool.

- **Call forms:** `ntk monitor watch-mem …`  ·  `ntk-monitor-watch-mem …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk monitor watch-mem [value]`
- **Parameters:** positional args: 1 known (args[0])


## <a id="benchmark"></a>`benchmark` — Speed benchmarks

_Speed benchmarks. 31 tools._

### `ntk benchmark allocate-bench`

allocate-bench tool.

- **Call forms:** `ntk benchmark allocate-bench …`  ·  `ntk-benchmark-allocate-bench …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark allocate-bench [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark base64-speed`

base64-speed tool.

- **Call forms:** `ntk benchmark base64-speed …`  ·  `ntk-benchmark-base64-speed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark base64-speed [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark checksum-speed`

checksum-speed tool.

- **Call forms:** `ntk benchmark checksum-speed …`  ·  `ntk-benchmark-checksum-speed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark checksum-speed [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark comprehension-speed`

comprehension-speed tool.

- **Call forms:** `ntk benchmark comprehension-speed …`  ·  `ntk-benchmark-comprehension-speed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark comprehension-speed [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark concat-speed`

concat-speed tool.

- **Call forms:** `ntk benchmark concat-speed …`  ·  `ntk-benchmark-concat-speed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark concat-speed [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark cpu`

cpu tool.

- **Call forms:** `ntk benchmark cpu …`  ·  `ntk-benchmark-cpu …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark cpu [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark dict-ops`

dict-ops tool.

- **Call forms:** `ntk benchmark dict-ops …`  ·  `ntk-benchmark-dict-ops …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark dict-ops [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark disk-read`

disk-read tool.

- **Call forms:** `ntk benchmark disk-read …`  ·  `ntk-benchmark-disk-read …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark disk-read [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark disk-write`

disk-write tool.

- **Call forms:** `ntk benchmark disk-write …`  ·  `ntk-benchmark-disk-write …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark disk-write [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark dns-speed`

dns-speed tool.

- **Call forms:** `ntk benchmark dns-speed …`  ·  `ntk-benchmark-dns-speed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark dns-speed [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark encode-speed`

encode-speed tool.

- **Call forms:** `ntk benchmark encode-speed …`  ·  `ntk-benchmark-encode-speed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark encode-speed [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark fib-bench`

fib-bench tool.

- **Call forms:** `ntk benchmark fib-bench …`  ·  `ntk-benchmark-fib-bench …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark fib-bench [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark float-ops`

float-ops tool.

- **Call forms:** `ntk benchmark float-ops …`  ·  `ntk-benchmark-float-ops …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark float-ops [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark hash-speed`

hash-speed tool.

- **Call forms:** `ntk benchmark hash-speed …`  ·  `ntk-benchmark-hash-speed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark hash-speed [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark http-speed`

http-speed tool.

- **Call forms:** `ntk benchmark http-speed …`  ·  `ntk-benchmark-http-speed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark http-speed [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark int-ops`

int-ops tool.

- **Call forms:** `ntk benchmark int-ops …`  ·  `ntk-benchmark-int-ops …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark int-ops [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark json-parse-speed`

json-parse-speed tool.

- **Call forms:** `ntk benchmark json-parse-speed …`  ·  `ntk-benchmark-json-parse-speed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark json-parse-speed [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark list-ops`

list-ops tool.

- **Call forms:** `ntk benchmark list-ops …`  ·  `ntk-benchmark-list-ops …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark list-ops [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark loop-bench`

loop-bench tool.

- **Call forms:** `ntk benchmark loop-bench …`  ·  `ntk-benchmark-loop-bench …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark loop-bench [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark matrix-bench`

matrix-bench tool.

- **Call forms:** `ntk benchmark matrix-bench …`  ·  `ntk-benchmark-matrix-bench …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark matrix-bench [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark memory`

memory tool.

- **Call forms:** `ntk benchmark memory …`  ·  `ntk-benchmark-memory …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark memory [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark pi-calc`

pi-calc tool.

- **Call forms:** `ntk benchmark pi-calc …`  ·  `ntk-benchmark-pi-calc …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark pi-calc [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark prime-speed`

prime-speed tool.

- **Call forms:** `ntk benchmark prime-speed …`  ·  `ntk-benchmark-prime-speed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark prime-speed [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark random-speed`

random-speed tool.

- **Call forms:** `ntk benchmark random-speed …`  ·  `ntk-benchmark-random-speed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark random-speed [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark regex-speed`

regex-speed tool.

- **Call forms:** `ntk benchmark regex-speed …`  ·  `ntk-benchmark-regex-speed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark regex-speed [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark set-ops`

set-ops tool.

- **Call forms:** `ntk benchmark set-ops …`  ·  `ntk-benchmark-set-ops …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark set-ops [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark sort-speed`

sort-speed tool.

- **Call forms:** `ntk benchmark sort-speed …`  ·  `ntk-benchmark-sort-speed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark sort-speed [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark sort-vs-sorted`

sort-vs-sorted tool.

- **Call forms:** `ntk benchmark sort-vs-sorted …`  ·  `ntk-benchmark-sort-vs-sorted …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark sort-vs-sorted [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark sqlite-insert-speed`

sqlite-insert-speed tool.

- **Call forms:** `ntk benchmark sqlite-insert-speed …`  ·  `ntk-benchmark-sqlite-insert-speed …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark sqlite-insert-speed [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark startup-self`

startup-self tool.

- **Call forms:** `ntk benchmark startup-self …`  ·  `ntk-benchmark-startup-self …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark startup-self [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk benchmark string-ops`

string-ops tool.

- **Call forms:** `ntk benchmark string-ops …`  ·  `ntk-benchmark-string-ops …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk benchmark string-ops [value]`
- **Parameters:** positional args: 1 known (args[0])


## <a id="disk"></a>`disk` — Disk & storage analysis

_Disk & storage analysis. 30 tools._

### `ntk disk bigfiles`

bigfiles tool.

- **Call forms:** `ntk disk bigfiles …`  ·  `ntk-disk-bigfiles …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk bigfiles [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk by-ext`

by-ext tool.

- **Call forms:** `ntk disk by-ext …`  ·  `ntk-disk-by-ext …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk by-ext [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk count`

count tool.

- **Call forms:** `ntk disk count …`  ·  `ntk-disk-count …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk count [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk depth`

depth tool.

- **Call forms:** `ntk disk depth …`  ·  `ntk-disk-depth …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk depth [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk du`

du tool.

- **Call forms:** `ntk disk du …`  ·  `ntk-disk-du …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk du [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk dupes`

dupes tool.

- **Call forms:** `ntk disk dupes …`  ·  `ntk-disk-dupes …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk dupes [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk empty-dirs`

empty-dirs tool.

- **Call forms:** `ntk disk empty-dirs …`  ·  `ntk-disk-empty-dirs …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk empty-dirs [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk extensions-stats`

extensions-stats tool.

- **Call forms:** `ntk disk extensions-stats …`  ·  `ntk-disk-extensions-stats …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk extensions-stats [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk file-types`

file-types tool.

- **Call forms:** `ntk disk file-types …`  ·  `ntk-disk-file-types …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk file-types [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk find-large`

find-large tool.

- **Call forms:** `ntk disk find-large …`  ·  `ntk-disk-find-large …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk find-large [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk find-old`

find-old tool.

- **Call forms:** `ntk disk find-old …`  ·  `ntk-disk-find-old …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk find-old [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk free`

free tool.

- **Call forms:** `ntk disk free …`  ·  `ntk-disk-free …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk free [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk hidden-files`

hidden-files tool.

- **Call forms:** `ntk disk hidden-files …`  ·  `ntk-disk-hidden-files …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk hidden-files [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk largest-dir`

largest-dir tool.

- **Call forms:** `ntk disk largest-dir …`  ·  `ntk-disk-largest-dir …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk largest-dir [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk mounts`

mounts tool.

- **Call forms:** `ntk disk mounts …`  ·  `ntk-disk-mounts …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk mounts [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk newest`

newest tool.

- **Call forms:** `ntk disk newest …`  ·  `ntk-disk-newest …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk newest [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk oldest`

oldest tool.

- **Call forms:** `ntk disk oldest …`  ·  `ntk-disk-oldest …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk oldest [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk partitions`

partitions tool.

- **Call forms:** `ntk disk partitions …`  ·  `ntk-disk-partitions …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk partitions [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk permissions-summary`

permissions-summary tool.

- **Call forms:** `ntk disk permissions-summary …`  ·  `ntk-disk-permissions-summary …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk permissions-summary [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk readonly-files`

readonly-files tool.

- **Call forms:** `ntk disk readonly-files …`  ·  `ntk-disk-readonly-files …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk readonly-files [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk recent-files`

recent-files tool.

- **Call forms:** `ntk disk recent-files …`  ·  `ntk-disk-recent-files …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk recent-files [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk scan`

scan tool.

- **Call forms:** `ntk disk scan …`  ·  `ntk-disk-scan …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk scan [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk size`

size tool.

- **Call forms:** `ntk disk size …`  ·  `ntk-disk-size …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk size [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk space-by-folder`

space-by-folder tool.

- **Call forms:** `ntk disk space-by-folder …`  ·  `ntk-disk-space-by-folder …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk space-by-folder [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk symlinks`

symlinks tool.

- **Call forms:** `ntk disk symlinks …`  ·  `ntk-disk-symlinks …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk symlinks [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk total-files`

total-files tool.

- **Call forms:** `ntk disk total-files …`  ·  `ntk-disk-total-files …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk total-files [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk total-size`

total-size tool.

- **Call forms:** `ntk disk total-size …`  ·  `ntk-disk-total-size …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk total-size [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk tree`

tree tool.

- **Call forms:** `ntk disk tree …`  ·  `ntk-disk-tree …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk tree [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk usage`

usage tool.

- **Call forms:** `ntk disk usage …`  ·  `ntk-disk-usage …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `available`
    - `ntk disk usage [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk disk zero-byte`

zero-byte tool.

- **Call forms:** `ntk disk zero-byte …`  ·  `ntk-disk-zero-byte …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk disk zero-byte [value]`
- **Parameters:** positional args: 1 known (args[0])


## <a id="process"></a>`process` — Process management

_Process management. 32 tools._

### `ntk process children`

children tool.

- **Call forms:** `ntk process children …`  ·  `ntk-process-children …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process children [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process cmdline`

cmdline tool.

- **Call forms:** `ntk process cmdline …`  ·  `ntk-process-cmdline …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process cmdline [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process connections`

connections tool.

- **Call forms:** `ntk process connections …`  ·  `ntk-process-connections …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process connections [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process count`

count tool.

- **Call forms:** `ntk process count …`  ·  `ntk-process-count …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process count [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process cpu-of`

cpu-of tool.

- **Call forms:** `ntk process cpu-of …`  ·  `ntk-process-cpu-of …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process cpu-of [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process create-time`

create-time tool.

- **Call forms:** `ntk process create-time …`  ·  `ntk-process-create-time …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process create-time [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process cwd-of`

cwd-of tool.

- **Call forms:** `ntk process cwd-of …`  ·  `ntk-process-cwd-of …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process cwd-of [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process exe-of`

exe-of tool.

- **Call forms:** `ntk process exe-of …`  ·  `ntk-process-exe-of …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process exe-of [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process find`

find tool.

- **Call forms:** `ntk process find …`  ·  `ntk-process-find …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process find [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process info`

info tool.

- **Call forms:** `ntk process info …`  ·  `ntk-process-info …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process info [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process kill`

kill tool.

- **Call forms:** `ntk process kill …`  ·  `ntk-process-kill …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process kill [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process kill-name`

kill-name tool.

- **Call forms:** `ntk process kill-name …`  ·  `ntk-process-kill-name …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process kill-name [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process kill-port`

kill-port tool.

- **Call forms:** `ntk process kill-port …`  ·  `ntk-process-kill-port …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process kill-port [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process list`

list tool.

- **Call forms:** `ntk process list …`  ·  `ntk-process-list …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process list [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process list-by-cpu`

list-by-cpu tool.

- **Call forms:** `ntk process list-by-cpu …`  ·  `ntk-process-list-by-cpu …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process list-by-cpu [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process list-by-mem`

list-by-mem tool.

- **Call forms:** `ntk process list-by-mem …`  ·  `ntk-process-list-by-mem …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process list-by-mem [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process mem-of`

mem-of tool.

- **Call forms:** `ntk process mem-of …`  ·  `ntk-process-mem-of …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process mem-of [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process newest`

newest tool.

- **Call forms:** `ntk process newest …`  ·  `ntk-process-newest …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process newest [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process oldest`

oldest tool.

- **Call forms:** `ntk process oldest …`  ·  `ntk-process-oldest …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process oldest [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process open-files`

open-files tool.

- **Call forms:** `ntk process open-files …`  ·  `ntk-process-open-files …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process open-files [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process parent`

parent tool.

- **Call forms:** `ntk process parent …`  ·  `ntk-process-parent …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process parent [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process port-owner`

port-owner tool.

- **Call forms:** `ntk process port-owner …`  ·  `ntk-process-port-owner …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process port-owner [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process priority`

priority tool.

- **Call forms:** `ntk process priority …`  ·  `ntk-process-priority …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process priority [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process resume`

resume tool.

- **Call forms:** `ntk process resume …`  ·  `ntk-process-resume …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process resume [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process running-count`

running-count tool.

- **Call forms:** `ntk process running-count …`  ·  `ntk-process-running-count …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process running-count [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process set-priority`

set-priority tool.

- **Call forms:** `ntk process set-priority …`  ·  `ntk-process-set-priority …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process set-priority [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process status`

status tool.

- **Call forms:** `ntk process status …`  ·  `ntk-process-status …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process status [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process suspend`

suspend tool.

- **Call forms:** `ntk process suspend …`  ·  `ntk-process-suspend …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process suspend [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process threads`

threads tool.

- **Call forms:** `ntk process threads …`  ·  `ntk-process-threads …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process threads [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process top`

top tool.

- **Call forms:** `ntk process top …`  ·  `ntk-process-top …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process top [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process tree`

tree tool.

- **Call forms:** `ntk process tree …`  ·  `ntk-process-tree …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process tree [value]`
- **Parameters:** positional args: 1 known (args[0])

### `ntk process user-processes`

user-processes tool.

- **Call forms:** `ntk process user-processes …`  ·  `ntk-process-user-processes …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ntk process user-processes [value]`
- **Parameters:** positional args: 1 known (args[0])


## <a id="search"></a>`search` — Search files, text & web

_Search files, text & web. 30 tools._

### `ntk search bigger-than`

Runs `ntk search bigger-than` (see `-h` for details).

- **Call forms:** `ntk search bigger-than …`  ·  `ntk-search-bigger-than …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search broken-symlinks`

Runs `ntk search broken-symlinks` (see `-h` for details).

- **Call forms:** `ntk search broken-symlinks …`  ·  `ntk-search-broken-symlinks …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search by-date`

Run as: `by-date <YYYY-MM-DD> [path]`

- **Call forms:** `ntk search by-date …`  ·  `ntk-search-by-date …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `by-date <YYYY-MM-DD> [path]`
- **Parameters:** none (or optional; run with `-h`)

### `ntk search content`

Runs `ntk search content` (see `-h` for details).

- **Call forms:** `ntk search content …`  ·  `ntk-search-content …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search count-matches`

Run as: `count-matches <word> <path>`

- **Call forms:** `ntk search count-matches …`  ·  `ntk-search-count-matches …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `count-matches <word> <path>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk search dupes`

Run as: `dupes [path]`

- **Call forms:** `ntk search dupes …`  ·  `ntk-search-dupes …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `dupes [path]`
- **Parameters:** none (or optional; run with `-h`)

### `ntk search empty-files`

Run as: `empty-files [path]`

- **Call forms:** `ntk search empty-files …`  ·  `ntk-search-empty-files …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `empty-files [path]`
- **Parameters:** none (or optional; run with `-h`)

### `ntk search executable`

Runs `ntk search executable` (see `-h` for details).

- **Call forms:** `ntk search executable …`  ·  `ntk-search-executable …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search ext`

Run as: `ext <extension> [path]`

- **Call forms:** `ntk search ext …`  ·  `ntk-search-ext …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `ext <extension> [path]`
- **Parameters:** none (or optional; run with `-h`)

### `ntk search file-type`

Runs `ntk search file-type` (see `-h` for details).

- **Call forms:** `ntk search file-type …`  ·  `ntk-search-file-type …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search files`

Run as: `files <pattern> [path]`

- **Call forms:** `ntk search files …`  ·  `ntk-search-files …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `files <pattern> [path]`
- **Parameters:** none (or optional; run with `-h`)

### `ntk search find-dir`

Runs `ntk search find-dir` (see `-h` for details).

- **Call forms:** `ntk search find-dir …`  ·  `ntk-search-find-dir …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search first-match`

Runs `ntk search first-match` (see `-h` for details).

- **Call forms:** `ntk search first-match …`  ·  `ntk-search-first-match …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search fuzzy-name`

Runs `ntk search fuzzy-name` (see `-h` for details).

- **Call forms:** `ntk search fuzzy-name …`  ·  `ntk-search-fuzzy-name …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search grep-recursive`

Runs `ntk search grep-recursive` (see `-h` for details).

- **Call forms:** `ntk search grep-recursive …`  ·  `ntk-search-grep-recursive …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search hidden`

Runs `ntk search hidden` (see `-h` for details).

- **Call forms:** `ntk search hidden …`  ·  `ntk-search-hidden …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search in-file`

Runs `ntk search in-file` (see `-h` for details).

- **Call forms:** `ntk search in-file …`  ·  `ntk-search-in-file …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search largest`

Runs `ntk search largest` (see `-h` for details).

- **Call forms:** `ntk search largest …`  ·  `ntk-search-largest …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search lines-with`

Runs `ntk search lines-with` (see `-h` for details).

- **Call forms:** `ntk search lines-with …`  ·  `ntk-search-lines-with …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search match-any`

Run as: `match-any <words,csv> <path>`

- **Call forms:** `ntk search match-any …`  ·  `ntk-search-match-any …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `match-any <words,csv> <path>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk search name`

Run as: `name <substring> [path]`

- **Call forms:** `ntk search name …`  ·  `ntk-search-name …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `name <substring> [path]`
- **Parameters:** none (or optional; run with `-h`)

### `ntk search newer-than`

Runs `ntk search newer-than` (see `-h` for details).

- **Call forms:** `ntk search newer-than …`  ·  `ntk-search-newer-than …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search nth-line`

Run as: `nth-line <n> <file>`

- **Call forms:** `ntk search nth-line …`  ·  `ntk-search-nth-line …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `nth-line <n> <file>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk search older-than`

Runs `ntk search older-than` (see `-h` for details).

- **Call forms:** `ntk search older-than …`  ·  `ntk-search-older-than …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search recent`

Runs `ntk search recent` (see `-h` for details).

- **Call forms:** `ntk search recent …`  ·  `ntk-search-recent …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search regex`

Runs `ntk search regex` (see `-h` for details).

- **Call forms:** `ntk search regex …`  ·  `ntk-search-regex …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search replace-preview`

Run as: `replace-preview <old> <new> <path>`

- **Call forms:** `ntk search replace-preview …`  ·  `ntk-search-replace-preview …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `replace-preview <old> <new> <path>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk search smaller-than`

Runs `ntk search smaller-than` (see `-h` for details).

- **Call forms:** `ntk search smaller-than …`  ·  `ntk-search-smaller-than …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search symlinks`

Runs `ntk search symlinks` (see `-h` for details).

- **Call forms:** `ntk search symlinks …`  ·  `ntk-search-symlinks …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk search text`

Runs `ntk search text` (see `-h` for details).

- **Call forms:** `ntk search text …`  ·  `ntk-search-text …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="archive"></a>`archive` — Archives & backups

_Archives & backups. 31 tools._

### `ntk archive b64-decode-file`

Runs `ntk archive b64-decode-file` (see `-h` for details).

- **Call forms:** `ntk archive b64-decode-file …`  ·  `ntk-archive-b64-decode-file …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive b64-encode-file`

Runs `ntk archive b64-encode-file` (see `-h` for details).

- **Call forms:** `ntk archive b64-encode-file …`  ·  `ntk-archive-b64-encode-file …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive backup`

Runs `ntk archive backup` (see `-h` for details).

- **Call forms:** `ntk archive backup …`  ·  `ntk-archive-backup …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive checksum-archive`

Runs `ntk archive checksum-archive` (see `-h` for details).

- **Call forms:** `ntk archive checksum-archive …`  ·  `ntk-archive-checksum-archive …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive compress-ratio`

Runs `ntk archive compress-ratio` (see `-h` for details).

- **Call forms:** `ntk archive compress-ratio …`  ·  `ntk-archive-compress-ratio …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive extract`

Runs `ntk archive extract` (see `-h` for details).

- **Call forms:** `ntk archive extract …`  ·  `ntk-archive-extract …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive folder-to-zip`

Runs `ntk archive folder-to-zip` (see `-h` for details).

- **Call forms:** `ntk archive folder-to-zip …`  ·  `ntk-archive-folder-to-zip …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive gunzip`

Runs `ntk archive gunzip` (see `-h` for details).

- **Call forms:** `ntk archive gunzip …`  ·  `ntk-archive-gunzip …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive gz-size`

Runs `ntk archive gz-size` (see `-h` for details).

- **Call forms:** `ntk archive gz-size …`  ·  `ntk-archive-gz-size …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive gzip`

Runs `ntk archive gzip` (see `-h` for details).

- **Call forms:** `ntk archive gzip …`  ·  `ntk-archive-gzip …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive join-files`

Runs `ntk archive join-files` (see `-h` for details).

- **Call forms:** `ntk archive join-files …`  ·  `ntk-archive-join-files …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive largest-in-zip`

Runs `ntk archive largest-in-zip` (see `-h` for details).

- **Call forms:** `ntk archive largest-in-zip …`  ·  `ntk-archive-largest-in-zip …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive list-supported`

Runs `ntk archive list-supported` (see `-h` for details).

- **Call forms:** `ntk archive list-supported …`  ·  `ntk-archive-list-supported …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive split-file`

Runs `ntk archive split-file` (see `-h` for details).

- **Call forms:** `ntk archive split-file …`  ·  `ntk-archive-split-file …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive tar`

Runs `ntk archive tar` (see `-h` for details).

- **Call forms:** `ntk archive tar …`  ·  `ntk-archive-tar …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive tar-list`

Runs `ntk archive tar-list` (see `-h` for details).

- **Call forms:** `ntk archive tar-list …`  ·  `ntk-archive-tar-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive tar-size`

Runs `ntk archive tar-size` (see `-h` for details).

- **Call forms:** `ntk archive tar-size …`  ·  `ntk-archive-tar-size …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive targz`

Runs `ntk archive targz` (see `-h` for details).

- **Call forms:** `ntk archive targz …`  ·  `ntk-archive-targz …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive untar`

Runs `ntk archive untar` (see `-h` for details).

- **Call forms:** `ntk archive untar …`  ·  `ntk-archive-untar …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive untargz`

Runs `ntk archive untargz` (see `-h` for details).

- **Call forms:** `ntk archive untargz …`  ·  `ntk-archive-untargz …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive unzip`

Runs `ntk archive unzip` (see `-h` for details).

- **Call forms:** `ntk archive unzip …`  ·  `ntk-archive-unzip …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive zip`

Run as: `zip <src> <dest>`

- **Call forms:** `ntk archive zip …`  ·  `ntk-archive-zip …`
- **Platform:** Windows 10/11 · Linux
- **Usage:**
    - `zip <src> <dest>`
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive zip-add`

Runs `ntk archive zip-add` (see `-h` for details).

- **Call forms:** `ntk archive zip-add …`  ·  `ntk-archive-zip-add …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive zip-comment`

Runs `ntk archive zip-comment` (see `-h` for details).

- **Call forms:** `ntk archive zip-comment …`  ·  `ntk-archive-zip-comment …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive zip-count`

Runs `ntk archive zip-count` (see `-h` for details).

- **Call forms:** `ntk archive zip-count …`  ·  `ntk-archive-zip-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive zip-extract-one`

Runs `ntk archive zip-extract-one` (see `-h` for details).

- **Call forms:** `ntk archive zip-extract-one …`  ·  `ntk-archive-zip-extract-one …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive zip-flatten`

Runs `ntk archive zip-flatten` (see `-h` for details).

- **Call forms:** `ntk archive zip-flatten …`  ·  `ntk-archive-zip-flatten …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive zip-info`

Runs `ntk archive zip-info` (see `-h` for details).

- **Call forms:** `ntk archive zip-info …`  ·  `ntk-archive-zip-info …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive zip-list`

Runs `ntk archive zip-list` (see `-h` for details).

- **Call forms:** `ntk archive zip-list …`  ·  `ntk-archive-zip-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive zip-size`

Runs `ntk archive zip-size` (see `-h` for details).

- **Call forms:** `ntk archive zip-size …`  ·  `ntk-archive-zip-size …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk archive zip-test`

Runs `ntk archive zip-test` (see `-h` for details).

- **Call forms:** `ntk archive zip-test …`  ·  `ntk-archive-zip-test …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="image"></a>`image` — Image editing

_Image editing. 32 tools._

### `ntk image batch-convert`

Runs `ntk image batch-convert` (see `-h` for details).

- **Call forms:** `ntk image batch-convert …`  ·  `ntk-image-batch-convert …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image blur`

Runs `ntk image blur` (see `-h` for details).

- **Call forms:** `ntk image blur …`  ·  `ntk-image-blur …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image border`

Runs `ntk image border` (see `-h` for details).

- **Call forms:** `ntk image border …`  ·  `ntk-image-border …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image brightness`

Runs `ntk image brightness` (see `-h` for details).

- **Call forms:** `ntk image brightness …`  ·  `ntk-image-brightness …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image compress`

Runs `ntk image compress` (see `-h` for details).

- **Call forms:** `ntk image compress …`  ·  `ntk-image-compress …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image contrast`

Runs `ntk image contrast` (see `-h` for details).

- **Call forms:** `ntk image contrast …`  ·  `ntk-image-contrast …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image convert`

Runs `ntk image convert` (see `-h` for details).

- **Call forms:** `ntk image convert …`  ·  `ntk-image-convert …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image crop`

Runs `ntk image crop` (see `-h` for details).

- **Call forms:** `ntk image crop …`  ·  `ntk-image-crop …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image dimensions`

Runs `ntk image dimensions` (see `-h` for details).

- **Call forms:** `ntk image dimensions …`  ·  `ntk-image-dimensions …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image dominant-color`

Runs `ntk image dominant-color` (see `-h` for details).

- **Call forms:** `ntk image dominant-color …`  ·  `ntk-image-dominant-color …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image exif`

Runs `ntk image exif` (see `-h` for details).

- **Call forms:** `ntk image exif …`  ·  `ntk-image-exif …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image fit`

Runs `ntk image fit` (see `-h` for details).

- **Call forms:** `ntk image fit …`  ·  `ntk-image-fit …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image flip`

Runs `ntk image flip` (see `-h` for details).

- **Call forms:** `ntk image flip …`  ·  `ntk-image-flip …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image format-detect`

Runs `ntk image format-detect` (see `-h` for details).

- **Call forms:** `ntk image format-detect …`  ·  `ntk-image-format-detect …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image grayscale`

Runs `ntk image grayscale` (see `-h` for details).

- **Call forms:** `ntk image grayscale …`  ·  `ntk-image-grayscale …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image histogram`

Runs `ntk image histogram` (see `-h` for details).

- **Call forms:** `ntk image histogram …`  ·  `ntk-image-histogram …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image info`

Runs `ntk image info` (see `-h` for details).

- **Call forms:** `ntk image info …`  ·  `ntk-image-info …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image invert`

Runs `ntk image invert` (see `-h` for details).

- **Call forms:** `ntk image invert …`  ·  `ntk-image-invert …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image largest-image`

Runs `ntk image largest-image` (see `-h` for details).

- **Call forms:** `ntk image largest-image …`  ·  `ntk-image-largest-image …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image mirror`

Runs `ntk image mirror` (see `-h` for details).

- **Call forms:** `ntk image mirror …`  ·  `ntk-image-mirror …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image pad`

Runs `ntk image pad` (see `-h` for details).

- **Call forms:** `ntk image pad …`  ·  `ntk-image-pad …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image palette`

Runs `ntk image palette` (see `-h` for details).

- **Call forms:** `ntk image palette …`  ·  `ntk-image-palette …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image pixelate`

Runs `ntk image pixelate` (see `-h` for details).

- **Call forms:** `ntk image pixelate …`  ·  `ntk-image-pixelate …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image resize`

Runs `ntk image resize` (see `-h` for details).

- **Call forms:** `ntk image resize …`  ·  `ntk-image-resize …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image rotate`

Runs `ntk image rotate` (see `-h` for details).

- **Call forms:** `ntk image rotate …`  ·  `ntk-image-rotate …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image scale`

Runs `ntk image scale` (see `-h` for details).

- **Call forms:** `ntk image scale …`  ·  `ntk-image-scale …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image sharpen`

Runs `ntk image sharpen` (see `-h` for details).

- **Call forms:** `ntk image sharpen …`  ·  `ntk-image-sharpen …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image strip-exif`

Runs `ntk image strip-exif` (see `-h` for details).

- **Call forms:** `ntk image strip-exif …`  ·  `ntk-image-strip-exif …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image thumbnail`

Runs `ntk image thumbnail` (see `-h` for details).

- **Call forms:** `ntk image thumbnail …`  ·  `ntk-image-thumbnail …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image to-jpg`

Runs `ntk image to-jpg` (see `-h` for details).

- **Call forms:** `ntk image to-jpg …`  ·  `ntk-image-to-jpg …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image to-png`

Runs `ntk image to-png` (see `-h` for details).

- **Call forms:** `ntk image to-png …`  ·  `ntk-image-to-png …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk image to-webp`

Runs `ntk image to-webp` (see `-h` for details).

- **Call forms:** `ntk image to-webp …`  ·  `ntk-image-to-webp …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="audio"></a>`audio` — Audio tools

_Audio tools. 31 tools._

### `ntk audio bitrate`

Runs `ntk audio bitrate` (see `-h` for details).

- **Call forms:** `ntk audio bitrate …`  ·  `ntk-audio-bitrate …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio channels`

Runs `ntk audio channels` (see `-h` for details).

- **Call forms:** `ntk audio channels …`  ·  `ntk-audio-channels …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio codec`

Runs `ntk audio codec` (see `-h` for details).

- **Call forms:** `ntk audio codec …`  ·  `ntk-audio-codec …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio concat`

Runs `ntk audio concat` (see `-h` for details).

- **Call forms:** `ntk audio concat …`  ·  `ntk-audio-concat …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio convert`

Runs `ntk audio convert` (see `-h` for details).

- **Call forms:** `ntk audio convert …`  ·  `ntk-audio-convert …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio cut`

Runs `ntk audio cut` (see `-h` for details).

- **Call forms:** `ntk audio cut …`  ·  `ntk-audio-cut …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio duration`

Runs `ntk audio duration` (see `-h` for details).

- **Call forms:** `ntk audio duration …`  ·  `ntk-audio-duration …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio extract-from-video`

Runs `ntk audio extract-from-video` (see `-h` for details).

- **Call forms:** `ntk audio extract-from-video …`  ·  `ntk-audio-extract-from-video …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio fade-in`

Runs `ntk audio fade-in` (see `-h` for details).

- **Call forms:** `ntk audio fade-in …`  ·  `ntk-audio-fade-in …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio fade-out`

Runs `ntk audio fade-out` (see `-h` for details).

- **Call forms:** `ntk audio fade-out …`  ·  `ntk-audio-fade-out …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio format-detect`

Runs `ntk audio format-detect` (see `-h` for details).

- **Call forms:** `ntk audio format-detect …`  ·  `ntk-audio-format-detect …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio gain`

Runs `ntk audio gain` (see `-h` for details).

- **Call forms:** `ntk audio gain …`  ·  `ntk-audio-gain …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio info`

Runs `ntk audio info` (see `-h` for details).

- **Call forms:** `ntk audio info …`  ·  `ntk-audio-info …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio loudness`

Runs `ntk audio loudness` (see `-h` for details).

- **Call forms:** `ntk audio loudness …`  ·  `ntk-audio-loudness …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio metadata`

Runs `ntk audio metadata` (see `-h` for details).

- **Call forms:** `ntk audio metadata …`  ·  `ntk-audio-metadata …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio mono`

Runs `ntk audio mono` (see `-h` for details).

- **Call forms:** `ntk audio mono …`  ·  `ntk-audio-mono …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio normalize`

Runs `ntk audio normalize` (see `-h` for details).

- **Call forms:** `ntk audio normalize …`  ·  `ntk-audio-normalize …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio resample`

Runs `ntk audio resample` (see `-h` for details).

- **Call forms:** `ntk audio resample …`  ·  `ntk-audio-resample …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio reverse`

Runs `ntk audio reverse` (see `-h` for details).

- **Call forms:** `ntk audio reverse …`  ·  `ntk-audio-reverse …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio sample-rate`

Runs `ntk audio sample-rate` (see `-h` for details).

- **Call forms:** `ntk audio sample-rate …`  ·  `ntk-audio-sample-rate …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio speed`

Runs `ntk audio speed` (see `-h` for details).

- **Call forms:** `ntk audio speed …`  ·  `ntk-audio-speed …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio split-by-time`

Runs `ntk audio split-by-time` (see `-h` for details).

- **Call forms:** `ntk audio split-by-time …`  ·  `ntk-audio-split-by-time …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio strip-metadata`

Runs `ntk audio strip-metadata` (see `-h` for details).

- **Call forms:** `ntk audio strip-metadata …`  ·  `ntk-audio-strip-metadata …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio tags`

Runs `ntk audio tags` (see `-h` for details).

- **Call forms:** `ntk audio tags …`  ·  `ntk-audio-tags …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio to-flac`

Runs `ntk audio to-flac` (see `-h` for details).

- **Call forms:** `ntk audio to-flac …`  ·  `ntk-audio-to-flac …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio to-mp3`

Runs `ntk audio to-mp3` (see `-h` for details).

- **Call forms:** `ntk audio to-mp3 …`  ·  `ntk-audio-to-mp3 …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio to-ogg`

Runs `ntk audio to-ogg` (see `-h` for details).

- **Call forms:** `ntk audio to-ogg …`  ·  `ntk-audio-to-ogg …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio to-wav`

Runs `ntk audio to-wav` (see `-h` for details).

- **Call forms:** `ntk audio to-wav …`  ·  `ntk-audio-to-wav …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio trim`

Runs `ntk audio trim` (see `-h` for details).

- **Call forms:** `ntk audio trim …`  ·  `ntk-audio-trim …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio volume`

Runs `ntk audio volume` (see `-h` for details).

- **Call forms:** `ntk audio volume …`  ·  `ntk-audio-volume …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk audio waveform-data`

Runs `ntk audio waveform-data` (see `-h` for details).

- **Call forms:** `ntk audio waveform-data …`  ·  `ntk-audio-waveform-data …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="code"></a>`code` — Code analysis & formatting

_Code analysis & formatting. 32 tools._

### `ntk code blank-lines`

Runs `ntk code blank-lines` (see `-h` for details).

- **Call forms:** `ntk code blank-lines …`  ·  `ntk-code-blank-lines …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code byte-count`

Runs `ntk code byte-count` (see `-h` for details).

- **Call forms:** `ntk code byte-count …`  ·  `ntk-code-byte-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code class-count`

Runs `ntk code class-count` (see `-h` for details).

- **Call forms:** `ntk code class-count …`  ·  `ntk-code-class-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code comment-ratio`

Runs `ntk code comment-ratio` (see `-h` for details).

- **Call forms:** `ntk code comment-ratio …`  ·  `ntk-code-comment-ratio …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code count-lines`

Runs `ntk code count-lines` (see `-h` for details).

- **Call forms:** `ntk code count-lines …`  ·  `ntk-code-count-lines …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code duplicate-lines`

Runs `ntk code duplicate-lines` (see `-h` for details).

- **Call forms:** `ntk code duplicate-lines …`  ·  `ntk-code-duplicate-lines …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code empty-files`

Runs `ntk code empty-files` (see `-h` for details).

- **Call forms:** `ntk code empty-files …`  ·  `ntk-code-empty-files …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code encoding`

Runs `ntk code encoding` (see `-h` for details).

- **Call forms:** `ntk code encoding …`  ·  `ntk-code-encoding …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code file-ext-stats`

Runs `ntk code file-ext-stats` (see `-h` for details).

- **Call forms:** `ntk code file-ext-stats …`  ·  `ntk-code-file-ext-stats …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code fixme-scan`

Runs `ntk code fixme-scan` (see `-h` for details).

- **Call forms:** `ntk code fixme-scan …`  ·  `ntk-code-fixme-scan …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code format-json`

Runs `ntk code format-json` (see `-h` for details).

- **Call forms:** `ntk code format-json …`  ·  `ntk-code-format-json …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code function-count`

Runs `ntk code function-count` (see `-h` for details).

- **Call forms:** `ntk code function-count …`  ·  `ntk-code-function-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code header-check`

Runs `ntk code header-check` (see `-h` for details).

- **Call forms:** `ntk code header-check …`  ·  `ntk-code-header-check …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code import-list`

Runs `ntk code import-list` (see `-h` for details).

- **Call forms:** `ntk code import-list …`  ·  `ntk-code-import-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code indent-check`

Runs `ntk code indent-check` (see `-h` for details).

- **Call forms:** `ntk code indent-check …`  ·  `ntk-code-indent-check …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code languages`

Runs `ntk code languages` (see `-h` for details).

- **Call forms:** `ntk code languages …`  ·  `ntk-code-languages …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code largest-file`

Runs `ntk code largest-file` (see `-h` for details).

- **Call forms:** `ntk code largest-file …`  ·  `ntk-code-largest-file …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code line-endings`

Runs `ntk code line-endings` (see `-h` for details).

- **Call forms:** `ntk code line-endings …`  ·  `ntk-code-line-endings …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code lines-of`

Runs `ntk code lines-of` (see `-h` for details).

- **Call forms:** `ntk code lines-of …`  ·  `ntk-code-lines-of …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code loc`

Runs `ntk code loc` (see `-h` for details).

- **Call forms:** `ntk code loc …`  ·  `ntk-code-loc …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code longest-function-hint`

Runs `ntk code longest-function-hint` (see `-h` for details).

- **Call forms:** `ntk code longest-function-hint …`  ·  `ntk-code-longest-function-hint …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code longest-line`

Runs `ntk code longest-line` (see `-h` for details).

- **Call forms:** `ntk code longest-line …`  ·  `ntk-code-longest-line …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code max-line-length`

Runs `ntk code max-line-length` (see `-h` for details).

- **Call forms:** `ntk code max-line-length …`  ·  `ntk-code-max-line-length …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code minify-json`

Runs `ntk code minify-json` (see `-h` for details).

- **Call forms:** `ntk code minify-json …`  ·  `ntk-code-minify-json …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code print-scan`

Runs `ntk code print-scan` (see `-h` for details).

- **Call forms:** `ntk code print-scan …`  ·  `ntk-code-print-scan …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code shebang`

Runs `ntk code shebang` (see `-h` for details).

- **Call forms:** `ntk code shebang …`  ·  `ntk-code-shebang …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code string-count`

Runs `ntk code string-count` (see `-h` for details).

- **Call forms:** `ntk code string-count …`  ·  `ntk-code-string-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code tabs-to-spaces`

Runs `ntk code tabs-to-spaces` (see `-h` for details).

- **Call forms:** `ntk code tabs-to-spaces …`  ·  `ntk-code-tabs-to-spaces …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** flags: --yes

### `ntk code todo-scan`

Runs `ntk code todo-scan` (see `-h` for details).

- **Call forms:** `ntk code todo-scan …`  ·  `ntk-code-todo-scan …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code trailing-whitespace`

Runs `ntk code trailing-whitespace` (see `-h` for details).

- **Call forms:** `ntk code trailing-whitespace …`  ·  `ntk-code-trailing-whitespace …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code wc-code`

Runs `ntk code wc-code` (see `-h` for details).

- **Call forms:** `ntk code wc-code …`  ·  `ntk-code-wc-code …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk code whitespace-only`

Runs `ntk code whitespace-only` (see `-h` for details).

- **Call forms:** `ntk code whitespace-only …`  ·  `ntk-code-whitespace-only …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="api"></a>`api` — API testing & clients

_API testing & clients. 32 tools._

### `ntk api auth-bearer-get`

Runs `ntk api auth-bearer-get` (see `-h` for details).

- **Call forms:** `ntk api auth-bearer-get …`  ·  `ntk-api-auth-bearer-get …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api content-type`

Runs `ntk api content-type` (see `-h` for details).

- **Call forms:** `ntk api content-type …`  ·  `ntk-api-content-type …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api cookies`

Runs `ntk api cookies` (see `-h` for details).

- **Call forms:** `ntk api cookies …`  ·  `ntk-api-cookies …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api curl-gen`

Runs `ntk api curl-gen` (see `-h` for details).

- **Call forms:** `ntk api curl-gen …`  ·  `ntk-api-curl-gen …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api delete`

Runs `ntk api delete` (see `-h` for details).

- **Call forms:** `ntk api delete …`  ·  `ntk-api-delete …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api download-json`

Runs `ntk api download-json` (see `-h` for details).

- **Call forms:** `ntk api download-json …`  ·  `ntk-api-download-json …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api form-post`

Runs `ntk api form-post` (see `-h` for details).

- **Call forms:** `ntk api form-post …`  ·  `ntk-api-form-post …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api get`

Runs `ntk api get` (see `-h` for details).

- **Call forms:** `ntk api get …`  ·  `ntk-api-get …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api graphql`

Runs `ntk api graphql` (see `-h` for details).

- **Call forms:** `ntk api graphql …`  ·  `ntk-api-graphql …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api head`

Runs `ntk api head` (see `-h` for details).

- **Call forms:** `ntk api head …`  ·  `ntk-api-head …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api headers`

Runs `ntk api headers` (see `-h` for details).

- **Call forms:** `ntk api headers …`  ·  `ntk-api-headers …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api health-check`

Runs `ntk api health-check` (see `-h` for details).

- **Call forms:** `ntk api health-check …`  ·  `ntk-api-health-check …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api http-methods`

Runs `ntk api http-methods` (see `-h` for details).

- **Call forms:** `ntk api http-methods …`  ·  `ntk-api-http-methods …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api json-count`

Runs `ntk api json-count` (see `-h` for details).

- **Call forms:** `ntk api json-count …`  ·  `ntk-api-json-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api json-get`

Runs `ntk api json-get` (see `-h` for details).

- **Call forms:** `ntk api json-get …`  ·  `ntk-api-json-get …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api json-keys`

Runs `ntk api json-keys` (see `-h` for details).

- **Call forms:** `ntk api json-keys …`  ·  `ntk-api-json-keys …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api json-path`

Runs `ntk api json-path` (see `-h` for details).

- **Call forms:** `ntk api json-path …`  ·  `ntk-api-json-path …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api ping-endpoint`

Runs `ntk api ping-endpoint` (see `-h` for details).

- **Call forms:** `ntk api ping-endpoint …`  ·  `ntk-api-ping-endpoint …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api post`

Runs `ntk api post` (see `-h` for details).

- **Call forms:** `ntk api post …`  ·  `ntk-api-post …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api put`

Runs `ntk api put` (see `-h` for details).

- **Call forms:** `ntk api put …`  ·  `ntk-api-put …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api query-parse`

Runs `ntk api query-parse` (see `-h` for details).

- **Call forms:** `ntk api query-parse …`  ·  `ntk-api-query-parse …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api rate-test`

Runs `ntk api rate-test` (see `-h` for details).

- **Call forms:** `ntk api rate-test …`  ·  `ntk-api-rate-test …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api redirect-chain`

Runs `ntk api redirect-chain` (see `-h` for details).

- **Call forms:** `ntk api redirect-chain …`  ·  `ntk-api-redirect-chain …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api response-time`

Runs `ntk api response-time` (see `-h` for details).

- **Call forms:** `ntk api response-time …`  ·  `ntk-api-response-time …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api rest-test`

Runs `ntk api rest-test` (see `-h` for details).

- **Call forms:** `ntk api rest-test …`  ·  `ntk-api-rest-test …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api retry-get`

Runs `ntk api retry-get` (see `-h` for details).

- **Call forms:** `ntk api retry-get …`  ·  `ntk-api-retry-get …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api size-of`

Runs `ntk api size-of` (see `-h` for details).

- **Call forms:** `ntk api size-of …`  ·  `ntk-api-size-of …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api status`

Runs `ntk api status` (see `-h` for details).

- **Call forms:** `ntk api status …`  ·  `ntk-api-status …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api timeout-test`

Runs `ntk api timeout-test` (see `-h` for details).

- **Call forms:** `ntk api timeout-test …`  ·  `ntk-api-timeout-test …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api url-decode`

Runs `ntk api url-decode` (see `-h` for details).

- **Call forms:** `ntk api url-decode …`  ·  `ntk-api-url-decode …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api url-encode`

Runs `ntk api url-encode` (see `-h` for details).

- **Call forms:** `ntk api url-encode …`  ·  `ntk-api-url-encode …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk api user-agent`

Runs `ntk api user-agent` (see `-h` for details).

- **Call forms:** `ntk api user-agent …`  ·  `ntk-api-user-agent …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="os"></a>`os` — OS settings, services & tasks

_OS settings, services & tasks. 33 tools._

### `ntk os arch`

Runs `ntk os arch` (see `-h` for details).

- **Call forms:** `ntk os arch …`  ·  `ntk-os-arch …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os boot-time`

Runs `ntk os boot-time` (see `-h` for details).

- **Call forms:** `ntk os boot-time …`  ·  `ntk-os-boot-time …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os cpu-count`

Runs `ntk os cpu-count` (see `-h` for details).

- **Call forms:** `ntk os cpu-count …`  ·  `ntk-os-cpu-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os cron-list`

Runs `ntk os cron-list` (see `-h` for details).

- **Call forms:** `ntk os cron-list …`  ·  `ntk-os-cron-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os current-user`

Runs `ntk os current-user` (see `-h` for details).

- **Call forms:** `ntk os current-user …`  ·  `ntk-os-current-user …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os default-gateway`

Runs `ntk os default-gateway` (see `-h` for details).

- **Call forms:** `ntk os default-gateway …`  ·  `ntk-os-default-gateway …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os disk-list`

Runs `ntk os disk-list` (see `-h` for details).

- **Call forms:** `ntk os disk-list …`  ·  `ntk-os-disk-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os dns-servers`

Runs `ntk os dns-servers` (see `-h` for details).

- **Call forms:** `ntk os dns-servers …`  ·  `ntk-os-dns-servers …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os env`

Runs `ntk os env` (see `-h` for details).

- **Call forms:** `ntk os env …`  ·  `ntk-os-env …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os env-count`

Runs `ntk os env-count` (see `-h` for details).

- **Call forms:** `ntk os env-count …`  ·  `ntk-os-env-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os home-dir`

Runs `ntk os home-dir` (see `-h` for details).

- **Call forms:** `ntk os home-dir …`  ·  `ntk-os-home-dir …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os hostname`

Runs `ntk os hostname` (see `-h` for details).

- **Call forms:** `ntk os hostname …`  ·  `ntk-os-hostname …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os installed-programs`

Runs `ntk os installed-programs` (see `-h` for details).

- **Call forms:** `ntk os installed-programs …`  ·  `ntk-os-installed-programs …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os is-admin`

Runs `ntk os is-admin` (see `-h` for details).

- **Call forms:** `ntk os is-admin …`  ·  `ntk-os-is-admin …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os kernel`

Runs `ntk os kernel` (see `-h` for details).

- **Call forms:** `ntk os kernel …`  ·  `ntk-os-kernel …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os locale`

Runs `ntk os locale` (see `-h` for details).

- **Call forms:** `ntk os locale …`  ·  `ntk-os-locale …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os node-name`

Runs `ntk os node-name` (see `-h` for details).

- **Call forms:** `ntk os node-name …`  ·  `ntk-os-node-name …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os os-version`

Runs `ntk os os-version` (see `-h` for details).

- **Call forms:** `ntk os os-version …`  ·  `ntk-os-os-version …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os path-list`

Runs `ntk os path-list` (see `-h` for details).

- **Call forms:** `ntk os path-list …`  ·  `ntk-os-path-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os pid-self`

Runs `ntk os pid-self` (see `-h` for details).

- **Call forms:** `ntk os pid-self …`  ·  `ntk-os-pid-self …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os platform`

Runs `ntk os platform` (see `-h` for details).

- **Call forms:** `ntk os platform …`  ·  `ntk-os-platform …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os processes-count`

Runs `ntk os processes-count` (see `-h` for details).

- **Call forms:** `ntk os processes-count …`  ·  `ntk-os-processes-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os python-version`

Runs `ntk os python-version` (see `-h` for details).

- **Call forms:** `ntk os python-version …`  ·  `ntk-os-python-version …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os reg-read`

Runs `ntk os reg-read` (see `-h` for details).

- **Call forms:** `ntk os reg-read …`  ·  `ntk-os-reg-read …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os scheduled-tasks`

Runs `ntk os scheduled-tasks` (see `-h` for details).

- **Call forms:** `ntk os scheduled-tasks …`  ·  `ntk-os-scheduled-tasks …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os services`

Runs `ntk os services` (see `-h` for details).

- **Call forms:** `ntk os services …`  ·  `ntk-os-services …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os shell`

Runs `ntk os shell` (see `-h` for details).

- **Call forms:** `ntk os shell …`  ·  `ntk-os-shell …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os startup-items`

Runs `ntk os startup-items` (see `-h` for details).

- **Call forms:** `ntk os startup-items …`  ·  `ntk-os-startup-items …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os system-encoding`

Runs `ntk os system-encoding` (see `-h` for details).

- **Call forms:** `ntk os system-encoding …`  ·  `ntk-os-system-encoding …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os temp-dir`

Runs `ntk os temp-dir` (see `-h` for details).

- **Call forms:** `ntk os temp-dir …`  ·  `ntk-os-temp-dir …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os timezone`

Runs `ntk os timezone` (see `-h` for details).

- **Call forms:** `ntk os timezone …`  ·  `ntk-os-timezone …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os uptime`

Runs `ntk os uptime` (see `-h` for details).

- **Call forms:** `ntk os uptime …`  ·  `ntk-os-uptime …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk os users`

Runs `ntk os users` (see `-h` for details).

- **Call forms:** `ntk os users …`  ·  `ntk-os-users …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="hardware"></a>`hardware` — Hardware & sensors

_Hardware & sensors. 32 tools._

### `ntk hardware architecture`

Runs `ntk hardware architecture` (see `-h` for details).

- **Call forms:** `ntk hardware architecture …`  ·  `ntk-hardware-architecture …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware battery`

Runs `ntk hardware battery` (see `-h` for details).

- **Call forms:** `ntk hardware battery …`  ·  `ntk-hardware-battery …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware bios`

Runs `ntk hardware bios` (see `-h` for details).

- **Call forms:** `ntk hardware bios …`  ·  `ntk-hardware-bios …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware boot-device-hint`

Runs `ntk hardware boot-device-hint` (see `-h` for details).

- **Call forms:** `ntk hardware boot-device-hint …`  ·  `ntk-hardware-boot-device-hint …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware byte-order`

Runs `ntk hardware byte-order` (see `-h` for details).

- **Call forms:** `ntk hardware byte-order …`  ·  `ntk-hardware-byte-order …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware core-temps`

Runs `ntk hardware core-temps` (see `-h` for details).

- **Call forms:** `ntk hardware core-temps …`  ·  `ntk-hardware-core-temps …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware cpu`

Runs `ntk hardware cpu` (see `-h` for details).

- **Call forms:** `ntk hardware cpu …`  ·  `ntk-hardware-cpu …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware cpu-cores`

Runs `ntk hardware cpu-cores` (see `-h` for details).

- **Call forms:** `ntk hardware cpu-cores …`  ·  `ntk-hardware-cpu-cores …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware cpu-freq`

Runs `ntk hardware cpu-freq` (see `-h` for details).

- **Call forms:** `ntk hardware cpu-freq …`  ·  `ntk-hardware-cpu-freq …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware cpu-model`

Runs `ntk hardware cpu-model` (see `-h` for details).

- **Call forms:** `ntk hardware cpu-model …`  ·  `ntk-hardware-cpu-model …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware cpu-usage`

Runs `ntk hardware cpu-usage` (see `-h` for details).

- **Call forms:** `ntk hardware cpu-usage …`  ·  `ntk-hardware-cpu-usage …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware cpu-vendor`

Runs `ntk hardware cpu-vendor` (see `-h` for details).

- **Call forms:** `ntk hardware cpu-vendor …`  ·  `ntk-hardware-cpu-vendor …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware disk-count`

Runs `ntk hardware disk-count` (see `-h` for details).

- **Call forms:** `ntk hardware disk-count …`  ·  `ntk-hardware-disk-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware disk-model-hint`

Runs `ntk hardware disk-model-hint` (see `-h` for details).

- **Call forms:** `ntk hardware disk-model-hint …`  ·  `ntk-hardware-disk-model-hint …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware disks`

Runs `ntk hardware disks` (see `-h` for details).

- **Call forms:** `ntk hardware disks …`  ·  `ntk-hardware-disks …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware free-ram`

Runs `ntk hardware free-ram` (see `-h` for details).

- **Call forms:** `ntk hardware free-ram …`  ·  `ntk-hardware-free-ram …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware gpu`

Runs `ntk hardware gpu` (see `-h` for details).

- **Call forms:** `ntk hardware gpu …`  ·  `ntk-hardware-gpu …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware load-avg`

Runs `ntk hardware load-avg` (see `-h` for details).

- **Call forms:** `ntk hardware load-avg …`  ·  `ntk-hardware-load-avg …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware logical-cores`

Runs `ntk hardware logical-cores` (see `-h` for details).

- **Call forms:** `ntk hardware logical-cores …`  ·  `ntk-hardware-logical-cores …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware mac-addresses`

Runs `ntk hardware mac-addresses` (see `-h` for details).

- **Call forms:** `ntk hardware mac-addresses …`  ·  `ntk-hardware-mac-addresses …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware monitor-hint`

Runs `ntk hardware monitor-hint` (see `-h` for details).

- **Call forms:** `ntk hardware monitor-hint …`  ·  `ntk-hardware-monitor-hint …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware motherboard`

Runs `ntk hardware motherboard` (see `-h` for details).

- **Call forms:** `ntk hardware motherboard …`  ·  `ntk-hardware-motherboard …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware network-adapters`

Runs `ntk hardware network-adapters` (see `-h` for details).

- **Call forms:** `ntk hardware network-adapters …`  ·  `ntk-hardware-network-adapters …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware partition-count`

Runs `ntk hardware partition-count` (see `-h` for details).

- **Call forms:** `ntk hardware partition-count …`  ·  `ntk-hardware-partition-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware physical-cores`

Runs `ntk hardware physical-cores` (see `-h` for details).

- **Call forms:** `ntk hardware physical-cores …`  ·  `ntk-hardware-physical-cores …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware ram`

Runs `ntk hardware ram` (see `-h` for details).

- **Call forms:** `ntk hardware ram …`  ·  `ntk-hardware-ram …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware ram-usage`

Runs `ntk hardware ram-usage` (see `-h` for details).

- **Call forms:** `ntk hardware ram-usage …`  ·  `ntk-hardware-ram-usage …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware sensors-temp`

Runs `ntk hardware sensors-temp` (see `-h` for details).

- **Call forms:** `ntk hardware sensors-temp …`  ·  `ntk-hardware-sensors-temp …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware swap-total`

Runs `ntk hardware swap-total` (see `-h` for details).

- **Call forms:** `ntk hardware swap-total …`  ·  `ntk-hardware-swap-total …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware total-ram`

Runs `ntk hardware total-ram` (see `-h` for details).

- **Call forms:** `ntk hardware total-ram …`  ·  `ntk-hardware-total-ram …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware usb-hint`

Runs `ntk hardware usb-hint` (see `-h` for details).

- **Call forms:** `ntk hardware usb-hint …`  ·  `ntk-hardware-usb-hint …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk hardware virtualization`

Runs `ntk hardware virtualization` (see `-h` for details).

- **Call forms:** `ntk hardware virtualization …`  ·  `ntk-hardware-virtualization …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="productivity"></a>`productivity` — Notes, todo, calc & fun

_Notes, todo, calc & fun. 33 tools._

### `ntk productivity age`

Runs `ntk productivity age` (see `-h` for details).

- **Call forms:** `ntk productivity age …`  ·  `ntk-productivity-age …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity ascii-banner`

Runs `ntk productivity ascii-banner` (see `-h` for details).

- **Call forms:** `ntk productivity ascii-banner …`  ·  `ntk-productivity-ascii-banner …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity base64-decode`

Runs `ntk productivity base64-decode` (see `-h` for details).

- **Call forms:** `ntk productivity base64-decode …`  ·  `ntk-productivity-base64-decode …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity base64-encode`

Runs `ntk productivity base64-encode` (see `-h` for details).

- **Call forms:** `ntk productivity base64-encode …`  ·  `ntk-productivity-base64-encode …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity calc`

Runs `ntk productivity calc` (see `-h` for details).

- **Call forms:** `ntk productivity calc …`  ·  `ntk-productivity-calc …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity char-count`

Runs `ntk productivity char-count` (see `-h` for details).

- **Call forms:** `ntk productivity char-count …`  ·  `ntk-productivity-char-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity coin`

Runs `ntk productivity coin` (see `-h` for details).

- **Call forms:** `ntk productivity coin …`  ·  `ntk-productivity-coin …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity color`

Runs `ntk productivity color` (see `-h` for details).

- **Call forms:** `ntk productivity color …`  ·  `ntk-productivity-color …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity countdown-days`

Runs `ntk productivity countdown-days` (see `-h` for details).

- **Call forms:** `ntk productivity countdown-days …`  ·  `ntk-productivity-countdown-days …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity dice`

Runs `ntk productivity dice` (see `-h` for details).

- **Call forms:** `ntk productivity dice …`  ·  `ntk-productivity-dice …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity flip-multiple`

Runs `ntk productivity flip-multiple` (see `-h` for details).

- **Call forms:** `ntk productivity flip-multiple …`  ·  `ntk-productivity-flip-multiple …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity lower`

Runs `ntk productivity lower` (see `-h` for details).

- **Call forms:** `ntk productivity lower …`  ·  `ntk-productivity-lower …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity motivate`

Runs `ntk productivity motivate` (see `-h` for details).

- **Call forms:** `ntk productivity motivate …`  ·  `ntk-productivity-motivate …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity note-add`

Runs `ntk productivity note-add` (see `-h` for details).

- **Call forms:** `ntk productivity note-add …`  ·  `ntk-productivity-note-add …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity note-clear`

Runs `ntk productivity note-clear` (see `-h` for details).

- **Call forms:** `ntk productivity note-clear …`  ·  `ntk-productivity-note-clear …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** flags: --yes

### `ntk productivity note-list`

Runs `ntk productivity note-list` (see `-h` for details).

- **Call forms:** `ntk productivity note-list …`  ·  `ntk-productivity-note-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity password`

Runs `ntk productivity password` (see `-h` for details).

- **Call forms:** `ntk productivity password …`  ·  `ntk-productivity-password …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity pick-number`

Runs `ntk productivity pick-number` (see `-h` for details).

- **Call forms:** `ntk productivity pick-number …`  ·  `ntk-productivity-pick-number …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity pomodoro`

Runs `ntk productivity pomodoro` (see `-h` for details).

- **Call forms:** `ntk productivity pomodoro …`  ·  `ntk-productivity-pomodoro …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity quote`

Runs `ntk productivity quote` (see `-h` for details).

- **Call forms:** `ntk productivity quote …`  ·  `ntk-productivity-quote …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity random-pick`

Runs `ntk productivity random-pick` (see `-h` for details).

- **Call forms:** `ntk productivity random-pick …`  ·  `ntk-productivity-random-pick …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity reverse-text`

Runs `ntk productivity reverse-text` (see `-h` for details).

- **Call forms:** `ntk productivity reverse-text …`  ·  `ntk-productivity-reverse-text …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity roll`

Runs `ntk productivity roll` (see `-h` for details).

- **Call forms:** `ntk productivity roll …`  ·  `ntk-productivity-roll …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity shuffle`

Runs `ntk productivity shuffle` (see `-h` for details).

- **Call forms:** `ntk productivity shuffle …`  ·  `ntk-productivity-shuffle …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity stopwatch`

Runs `ntk productivity stopwatch` (see `-h` for details).

- **Call forms:** `ntk productivity stopwatch …`  ·  `ntk-productivity-stopwatch …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity timer`

Runs `ntk productivity timer` (see `-h` for details).

- **Call forms:** `ntk productivity timer …`  ·  `ntk-productivity-timer …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity todo-add`

Runs `ntk productivity todo-add` (see `-h` for details).

- **Call forms:** `ntk productivity todo-add …`  ·  `ntk-productivity-todo-add …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity todo-clear`

Runs `ntk productivity todo-clear` (see `-h` for details).

- **Call forms:** `ntk productivity todo-clear …`  ·  `ntk-productivity-todo-clear …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** flags: --yes

### `ntk productivity todo-done`

Runs `ntk productivity todo-done` (see `-h` for details).

- **Call forms:** `ntk productivity todo-done …`  ·  `ntk-productivity-todo-done …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity todo-list`

Runs `ntk productivity todo-list` (see `-h` for details).

- **Call forms:** `ntk productivity todo-list …`  ·  `ntk-productivity-todo-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity upper`

Runs `ntk productivity upper` (see `-h` for details).

- **Call forms:** `ntk productivity upper …`  ·  `ntk-productivity-upper …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity uuid`

Runs `ntk productivity uuid` (see `-h` for details).

- **Call forms:** `ntk productivity uuid …`  ·  `ntk-productivity-uuid …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk productivity word-count`

Runs `ntk productivity word-count` (see `-h` for details).

- **Call forms:** `ntk productivity word-count …`  ·  `ntk-productivity-word-count …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)


## <a id="admin"></a>`admin` — Admin: users, firewall, tasks

_Admin: users, firewall, tasks. 31 tools._

### `ntk admin cron-list`

List cron jobs (Linux).

- **Call forms:** `ntk admin cron-list …`  ·  `ntk-admin-cron-list …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin current-privileges`

Show current user privileges/groups.

- **Call forms:** `ntk admin current-privileges …`  ·  `ntk-admin-current-privileges …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin current-user`

Show the current user name.

- **Call forms:** `ntk admin current-user …`  ·  `ntk-admin-current-user …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin disk-permissions`

Show permissions of a path: <path>.

- **Call forms:** `ntk admin disk-permissions …`  ·  `ntk-admin-disk-permissions …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** positional args: 1 known (args[0])

### `ntk admin env-system`

Show important system environment variables.

- **Call forms:** `ntk admin env-system …`  ·  `ntk-admin-env-system …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin event-log-tail`

Show recent system log entries.

- **Call forms:** `ntk admin event-log-tail …`  ·  `ntk-admin-event-log-tail …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** flags: --no-pager

### `ntk admin failed-logins`

Show failed login attempts (best-effort).

- **Call forms:** `ntk admin failed-logins …`  ·  `ntk-admin-failed-logins …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin firewall-rules-count`

Count firewall rules.

- **Call forms:** `ntk admin firewall-rules-count …`  ·  `ntk-admin-firewall-rules-count …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin firewall-status`

Show firewall status.

- **Call forms:** `ntk admin firewall-status …`  ·  `ntk-admin-firewall-status …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin groups-list`

List groups.

- **Call forms:** `ntk admin groups-list …`  ·  `ntk-admin-groups-list …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin hostname`

Show the machine hostname.

- **Call forms:** `ntk admin hostname …`  ·  `ntk-admin-hostname …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin hostname-info`

Show full hostname/domain info.

- **Call forms:** `ntk admin hostname-info …`  ·  `ntk-admin-hostname-info …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin hosts-file`

Show the hosts file.

- **Call forms:** `ntk admin hosts-file …`  ·  `ntk-admin-hosts-file …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin installed-count`

Count installed programs (best-effort).

- **Call forms:** `ntk admin installed-count …`  ·  `ntk-admin-installed-count …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** flags: --get-selections

### `ntk admin is-admin`

Check if running with admin/root rights.

- **Call forms:** `ntk admin is-admin …`  ·  `ntk-admin-is-admin …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin last-boot`

Show last boot time.

- **Call forms:** `ntk admin last-boot …`  ·  `ntk-admin-last-boot …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin lock-screen`

Lock the screen.

- **Call forms:** `ntk admin lock-screen …`  ·  `ntk-admin-lock-screen …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin logged-in`

Show currently logged-in users.

- **Call forms:** `ntk admin logged-in …`  ·  `ntk-admin-logged-in …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin network-shares`

List network shares.

- **Call forms:** `ntk admin network-shares …`  ·  `ntk-admin-network-shares …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** flags: --shares

### `ntk admin open-ports`

List listening ports (admin view).

- **Call forms:** `ntk admin open-ports …`  ·  `ntk-admin-open-ports …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin password-policy`

Show password policy (Windows).

- **Call forms:** `ntk admin password-policy …`  ·  `ntk-admin-password-policy …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin reboot`

Reboot the machine (requires --yes).

- **Call forms:** `ntk admin reboot …`  ·  `ntk-admin-reboot …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** flags: --yes

### `ntk admin scheduled-tasks`

List scheduled tasks / cron jobs.

- **Call forms:** `ntk admin scheduled-tasks …`  ·  `ntk-admin-scheduled-tasks …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin services-list`

List running services.

- **Call forms:** `ntk admin services-list …`  ·  `ntk-admin-services-list …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** flags: --no-legend, --no-pager, --state, --type

### `ntk admin shutdown`

Shut down the machine (requires --yes).

- **Call forms:** `ntk admin shutdown …`  ·  `ntk-admin-shutdown …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** flags: --yes

### `ntk admin ssh-keys-list`

List SSH keys in ~/.ssh.

- **Call forms:** `ntk admin ssh-keys-list …`  ·  `ntk-admin-ssh-keys-list …`
- **Platform:** Windows 10/11 · Linux
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin startup-programs`

List startup programs.

- **Call forms:** `ntk admin startup-programs …`  ·  `ntk-admin-startup-programs …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin sudoers-check`

Show sudo access (Linux).

- **Call forms:** `ntk admin sudoers-check …`  ·  `ntk-admin-sudoers-check …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin uac-status`

Show UAC status (Windows).

- **Call forms:** `ntk admin uac-status …`  ·  `ntk-admin-uac-status …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)

### `ntk admin user-info`

Show info about a user: <name>.

- **Call forms:** `ntk admin user-info …`  ·  `ntk-admin-user-info …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Usage:**
    - `ntk admin user-info <name>`
- **Parameters:** positional args: 1 known (args[0])

### `ntk admin users-list`

List local user accounts.

- **Call forms:** `ntk admin users-list …`  ·  `ntk-admin-users-list …`
- **Platform:** Windows 10/11 · Linux (adapts per OS)
- **Parameters:** none (or optional; run with `-h`)



---

**Grand total: 1034 commands across 33 categories.**

Every command is also documented live: `ntk <category> <tool> -h`.
