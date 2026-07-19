<div align="center">

<img src="assets/ntk_logo.png" width="140" alt="NTK logo"/>

# NTK — Next Tool Kit

**One CLI. 1000+ terminal tools. Zero dependencies for the end user.**

Cross-platform developer & power-user toolkit for **Windows 10 / 11** and **Linux**.
Standalone executable — no Python, no Node.js, nothing to install.

`ntk-system-os-info` · `ntk-network-ping` · `ntk-crypto-sha256` · `ntk-performance-ram-free`

Plus a **Manager app** (browse/search/copy every command in your browser), a built-in
**updater**, and a clean **uninstaller**.

> ⚠️ **BETA** — This is a beta release. Things may change and some tools depend on
> optional external CLIs (docker, aws, git, …). Feedback & issues welcome.

</div>

---

## ⚠️ Disclaimer — please read

NTK is **beta software provided "as is", without any warranty** (see [`LICENSE`](LICENSE)).

- **Errors can and will happen.** Some tools wrap external programs (docker, aws, ffmpeg, git, …)
  or need network access, elevated privileges, or a real terminal. If something is missing
  or unavailable, NTK prints a clear error and exits — it should **never** dump a raw crash,
  but bugs are still possible in a beta.
- **Use at your own risk.** Some tools modify files, processes, services, or system settings
  (e.g. `process kill`, `file shred`, `performance clean-disk`). Destructive actions preview
  first and require `--yes`. Double-check arguments before running. The author is **not liable**
  for any data loss or damage.
- **Not a security product.** The `security`/`crypto` helpers are convenience utilities, not audited
  security tooling. Don't rely on them for anything critical.
- **Found a bug?** Please open an issue:
  [github.com/finnytech/ntk-Next-Tool-Kit-terminal-cli/issues](https://github.com/finnytech/ntk-Next-Tool-Kit-terminal-cli/issues)

Every command supports `-h` for usage help, e.g. `ntk performance clean-disk -h`.

---

## What is NTK?

NTK bundles **1000+ practical command-line tools** across **33 universal categories**
into a single, fast, self-contained executable — the way `npm`/`npx` feel, but for
everyday system, performance, network, crypto, dev, and DevOps tasks. Every tool is one
command away.

Two equivalent call styles:

```bash
ntk system os-info      # space form
ntk-system-os-info      # hyphen form (great for muscle memory & scripts)
```

Optional parameters follow the command:

```bash
ntk crypto sha256 myfile.txt
ntk-crypto-sha256 myfile.txt
ntk network ping google.com
ntk math calc "2*(3+4)"
```

### ⚡ New in v2.0 — the `performance` category

Safe, one-command speed-ups that **never close your important programs or touch personal files**:

```bash
ntk performance mem-report      # what's using your RAM
ntk performance ram-free        # free trimmable memory (safe)
ntk performance clean-disk      # preview junk/temp/cache (asks before deleting)
ntk performance cpu-optimize    # tune power/CPU for speed
ntk performance health          # quick system health check
```

Destructive steps are **opt-in**: they preview first and require `--yes` to actually delete.

## Quick Start — install, use, update

A 60-second guide. Pick your platform, then just use `ntk`.

### 1. Install

**Windows 10 / 11** — download **`ntk-installer.exe`** from the [latest release](../../releases),
run it (approve the UAC/Admin prompt), then **open a NEW terminal**. Done.
The installer puts `ntk` on your system PATH (CMD **and** PowerShell) + Registry, and
installs the companions next to it: **`ntk-updater.exe`**, **`ntk-manager.exe`**, and
**`ntk-uninstall.exe`**.

**Linux** — download the `ntk` binary, then:
```bash
chmod +x ntk && sudo mv ntk /usr/local/bin/
```

> 💡 On Windows, if `ntk` seems "not found" right after installing, your terminal was
> open **before** the install. Just open a **fresh** CMD/PowerShell window — the PATH is
> set system-wide, so `ntk` then works from any folder.

### 2. Use it

```bash
ntk                          # banner + all 33 categories
ntk --help                   # help
ntk system                   # list every tool in the 'system' category
ntk system os-info           # run a tool (space form)
ntk-system-os-info           # exact same thing (hyphen form)
ntk-crypto-sha256 file.txt   # tools take parameters right after the name
ntk network ping google.com
ntk <cat> <tool> -h          # per-tool help
```

### 3. Manager app (browse • search • copy)

Prefer a UI? Launch the **NTK Manager** — a tiny launcher that opens a local page in your
browser where you can browse all 1000+ tools by category, **search** across every command,
read each tool's help, and **copy any command to the clipboard** with one click. It also has
**Update** and **Uninstall** buttons.

```bash
ntk-manager               # Windows: run it (or double-click ntk-manager.exe)
./ntk-manager             # Linux
```

No heavy GUI toolkit — it just starts a localhost server and opens your default browser.

### 4. Keep it up to date

Whenever a new release ships, just run the updater — it pulls the newest build from
GitHub and replaces your `ntk` in place (self-elevates on Windows if needed):

```bash
ntk update                # from the CLI (runs the bundled updater)
ntk-updater               # Windows: run it (or double-click ntk-updater.exe)
./ntk-updater             # Linux
ntk-updater --force       # re-download & reinstall even if versions match
```

### 5. Uninstall (100% clean)

Two equivalent ways — both remove the PATH entry, Registry keys, and Program Files folder:

```bash
ntk uninstall             # from the CLI
ntk-uninstall             # Windows: standalone uninstaller (self-elevates)
./ntk-uninstall           # Linux
ntk uninstall --purge     # also remove your ~/.ntk notes/todos
```

---

## 33 Categories (1000+ tools)

| Category | What it does | Examples |
|---|---|---|
| `system` | System & OS info/control | `system os-info`, `system hostname`, `system users` |
| `performance` | **Speed up:** free RAM, clean disk, CPU/GPU optimize | `performance ram-free`, `performance clean-disk`, `performance cpu-optimize` |
| `network` | Network, DNS, ports & connectivity | `network ping`, `network dns-lookup`, `network reverse-dns` |
| `file` | Files & folders | `file find`, `file tree`, `file size` |
| `text` | Text processing | `text upper`, `text lower`, `text title` |
| `data` | JSON/CSV/YAML/XML convert & query | `data json-format`, `data json-minify`, `data json-validate` |
| `crypto` | Hashing & encryption | `crypto md5`, `crypto sha1`, `crypto sha256` |
| `security` | Security audit & scanning | `security password-strength`, `security hash-identify`, `security entropy` |
| `dev` | Developer workflow | `dev lorem`, `dev uuid`, `dev timestamp` |
| `git` | Git helpers | `git status`, `git log`, `git branches` |
| `web` | Web, HTTP & API | `web get`, `web post`, `web head` |
| `media` | Media info & simple ops | `media image-info`, `media image-resize`, `media image-convert` |
| `docker` | Docker & containers | `docker ps`, `docker ps-all`, `docker images` |
| `cloud` | Cloud & DevOps | `cloud aws-identity`, `cloud aws-regions`, `cloud aws-s3-ls` |
| `database` | Database tools | `database sqlite-query`, `database sqlite-tables`, `database sqlite-schema` |
| `math` | Math, stats & number tools | `math calc`, `math mean`, `math median` |
| `time` | Date, time, timers & zones | `time now`, `time utc-now`, `time epoch` |
| `convert` | Units & format conversion | `convert length`, `convert mass`, `convert temp` |
| `generate` | Generators (passwords, UUID, QR, ...) | `generate password`, `generate passphrase`, `generate uuid` |
| `monitor` | Live system monitors | `monitor cpu`, `monitor cpu-per-core`, `monitor mem` |
| `benchmark` | Speed benchmarks | `benchmark cpu`, `benchmark memory`, `benchmark disk-write` |
| `disk` | Disk & storage analysis | `disk usage`, `disk tree`, `disk bigfiles` |
| `process` | Process management | `process list`, `process list-by-cpu`, `process list-by-mem` |
| `search` | Search files, text & web | `search files`, `search text`, `search regex` |
| `archive` | Archives & backups | `archive zip`, `archive unzip`, `archive zip-list` |
| `image` | Image editing | `image info`, `image resize`, `image scale` |
| `audio` | Audio tools | `audio info`, `audio duration`, `audio convert` |
| `code` | Code analysis & formatting | `code count-lines`, `code loc`, `code comment-ratio` |
| `api` | API testing & clients | `api get`, `api post`, `api put` |
| `os` | OS settings, services & tasks | `os env`, `os hostname`, `os os-version` |
| `hardware` | Hardware & sensors | `hardware cpu`, `hardware cpu-cores`, `hardware cpu-freq` |
| `productivity` | Notes, todo, calc & fun | `productivity note-add`, `productivity note-list`, `productivity note-clear` |
| `admin` | Admin: users, firewall, tasks | `admin is-admin`, `admin current-user`, `admin users-list` |

> v1 category names still work as **aliases** (`sys`→`system`, `net`→`network`,
> `sec`→`security`, `db`→`database`, `util`→`productivity`), so old scripts keep running.

Run `ntk` or `ntk --help` for the banner, `ntk <category>` to list a category's tools,
and `ntk <category> <tool> -h` for per-tool help.

📖 **Full reference:** every single command — on Windows **and** Linux, with all
parameters, options and platform notes — is documented in the
**[Command Handbook → `COMMANDS.md`](COMMANDS.md)**.

## Install

### Windows 10 / 11

1. Download **`ntk-installer.exe`** from the [latest release](../../releases).
2. Run it (it will request Administrator rights via UAC).
3. Open a **new** terminal (CMD or PowerShell) and run `ntk --help`.

The installer copies `ntk.exe` to `C:\Program Files\NTK`, adds it to the **system PATH**
(works in CMD **and** PowerShell), and registers it in the **Windows Registry**
(App Paths + an uninstall entry in *Apps & features*).

Prefer no installer? Just grab **`ntk.exe`** and put it anywhere on your PATH.

### Linux

```bash
# Download the 'ntk' binary from the latest release, then:
chmod +x ntk
sudo mv ntk /usr/local/bin/
ntk --help
```

No Python required — the runtime is bundled.

## Design

- **Standalone** — built with PyInstaller; the Python runtime is embedded.
- **Lazy-loading** — each of the 33 categories lives in its own module and is only imported when used, so startup stays fast even with 1000+ tools.
- **Safe-by-default** — the `performance` tools only ever touch caches/temp/trimmable memory, never your open apps or personal files, and confirm before deleting anything.
- **stdlib-first** — most tools use only the standard library. Tools that wrap external
  programs (docker, aws, ffmpeg, …) degrade gracefully with a clear hint when the tool is missing.
- **Cross-platform** — Windows 10/11 is the primary target; Linux is fully supported.

See [`CONVENTIONS.md`](CONVENTIONS.md) for the internal contract each tool module follows.

## Build from source

Requires Python 3.10+ and PyInstaller.

```bash
pip install -r requirements.txt pyinstaller
python make_logo.py                                           # regenerate assets/ntk.ico
pyinstaller --clean --noconfirm ntk.spec                     # -> dist/ntk(.exe)
pyinstaller --clean --noconfirm installer/ntk_updater.spec   # -> dist/ntk-updater(.exe)
pyinstaller --clean --noconfirm installer/ntk_manage.spec    # -> dist/ntk-manager(.exe)
pyinstaller --clean --noconfirm installer/ntk_uninstall.spec # -> dist/ntk-uninstall(.exe)
pyinstaller --clean --noconfirm installer/ntk_installer.spec # Windows installer (bundles all of the above)
```

## License

MIT — see [`LICENSE`](LICENSE).

---

<div align="center">
Made with ✨ by <a href="https://github.com/finnytech">finnytech</a>
</div>
