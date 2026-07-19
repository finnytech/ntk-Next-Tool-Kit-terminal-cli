<div align="center">

<img src="assets/ntk_logo.png" width="140" alt="NTK logo"/>

# NTK — Next Tool Kit

**One CLI. 300+ terminal tools. Zero dependencies for the end user.**

Cross-platform developer toolkit for **Windows 10 / 11** and **Linux**.
Standalone executable — no Python, no Node.js, nothing to install.

`ntk-sys-info` · `ntk-net-ping` · `ntk-crypto-password 24` · `ntk-util-calc "2*(3+4)"`

> ⚠️ **BETA** — This is a beta release. Things may change and some tools depend on
> optional external CLIs (docker, aws, git, …). Feedback & issues welcome.

</div>

---

## What is NTK?

NTK bundles **300+ practical command-line tools** into a single, fast, self-contained
executable — the way `npm`/`npx` feel, but for everyday system, network, crypto, dev,
and DevOps tasks. Every tool is one command away.

Two equivalent call styles:

```bash
ntk sys info          # space form
ntk-sys-info          # hyphen form (great for muscle memory & scripts)
```

Optional parameters follow the command:

```bash
ntk crypto password 24
ntk-crypto-password 24
ntk net ping google.com
ntk util calc "2*(3+4)"
```

## 15 Categories

| Category | What it does | Examples |
|---|---|---|
| `sys`    | System & OS monitoring/control | `sys info`, `sys top`, `sys kill-port 8080` |
| `net`    | Network & HTTP tools | `net ping`, `net portscan`, `net myip` |
| `file`   | Filesystem & storage | `file dupes`, `file bigfiles`, `file tree` |
| `text`   | Text & data processing | `text upper`, `text slugify`, `text json-fmt` |
| `crypto` | Cryptography & hashing | `crypto sha256`, `crypto uuid`, `crypto password` |
| `dev`    | Developer workflow | `dev lorem`, `dev color #ff8800`, `dev semver` |
| `auto`   | Automation & helpers | `auto watch`, `auto retry`, `auto repeat` |
| `docker` | Docker & containers | `docker ps`, `docker clean`, `docker dockerfile-gen` |
| `db`     | Database tools | `db sqlite-query`, `db dump`, `db csv-import` |
| `web`    | Advanced web & API | `web headers`, `web bench`, `web ip-geo` |
| `media`  | Media & asset tools | `media resize`, `media exif`, `media qr` |
| `ai`     | AI & LLM integrations | `ai tokens`, `ai regex-gen`, `ai json-schema` |
| `sec`    | Security & audit | `sec entropy`, `sec hash-identify`, `sec ports` |
| `cloud`  | DevOps & cloud | `cloud aws-s3-ls`, `cloud kube-ctx`, `cloud tf-lint` |
| `util`   | Utilities & terminal games | `util calc`, `util unit`, `util quote` |

Run `ntk` or `ntk --help` for the banner, `ntk <category>` to list a category's tools,
and `ntk <category> <tool> -h` for per-tool help.

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
- **Lazy-loading** — each category lives in its own module and is only imported when used, so startup stays fast.
- **stdlib-first** — most tools use only the standard library. Tools that wrap external
  programs (docker, aws, ffmpeg, …) degrade gracefully with a clear hint when the tool is missing.
- **Cross-platform** — Windows 10/11 is the primary target; Linux is fully supported.

See [`CONVENTIONS.md`](CONVENTIONS.md) for the internal contract each tool module follows.

## Build from source

Requires Python 3.10+ and PyInstaller.

```bash
pip install -r requirements.txt pyinstaller
pyinstaller --clean --noconfirm ntk.spec       # -> dist/ntk(.exe)
python make_logo.py                            # regenerate assets/ntk.ico
pyinstaller --clean --noconfirm installer/ntk_installer.spec   # Windows installer
```

## License

MIT — see [`LICENSE`](LICENSE).

---

<div align="center">
Made with ✨ by <a href="https://github.com/finnytech">finnytech</a>
</div>
