"""AI & LLM integrations (ntk ai ...).

LLM-backed tools use an OpenAI-compatible endpoint if OPENAI_API_KEY (and optional
OPENAI_BASE_URL / NTK_AI_MODEL) are set; otherwise they degrade to offline heuristics
or a clear note. Pure-offline tools (tokens, json-schema, regex-gen, embedding) always work.
"""
import os
import re
import json
import math
from . import util
from .util import col, C


def _read_input(args):
    if not args:
        import sys
        if not sys.stdin.isatty():
            return sys.stdin.read()
        return ""
    if os.path.isfile(args[0]):
        return open(args[0], encoding="utf-8", errors="replace").read()
    return " ".join(args)


def _llm(prompt, system="You are a helpful CLI assistant.", max_tokens=800):
    """Call an OpenAI-compatible chat endpoint. Returns text or None."""
    key = os.environ.get("OPENAI_API_KEY") or os.environ.get("NTK_AI_KEY")
    if not key:
        return None
    base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.environ.get("NTK_AI_MODEL", "gpt-4o-mini")
    import urllib.request
    body = json.dumps({
        "model": model,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(base + "/chat/completions", data=body, headers={
        "Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read())
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        util.warn(f"LLM call failed: {e}")
        return None


def _no_key_note():
    util.warn("no API key set. Export OPENAI_API_KEY (and optional OPENAI_BASE_URL, "
              "NTK_AI_MODEL) to enable live AI. Offline result shown where possible.")


def _est_tokens(text):
    # Rough GPT-style estimate: ~4 chars/token, plus word-boundary correction.
    return max(len(text) // 4, int(len(re.findall(r"\w+|\S", text)) * 0.75))


def tokens(args):
    """Estimate token count of text (GPT/Claude approx)."""
    text = _read_input(args)
    if not text:
        util.err("usage: ntk ai tokens <text|file>")
        return 2
    try:
        import tiktoken
        enc = tiktoken.get_encoding("cl100k_base")
        n = len(enc.encode(text))
        util.kv("Tokens (tiktoken)", n)
    except Exception:
        util.kv("Tokens (estimate)", _est_tokens(text))
    util.kv("Characters", len(text))
    util.kv("Words", len(text.split()))
    return 0


def prompt_opt(args):
    """Analyze a prompt and suggest improvements."""
    text = _read_input(args)
    if not text:
        util.err("usage: ntk ai prompt-opt <text|file>")
        return 2
    out = _llm(f"Improve this prompt and explain briefly why:\n\n{text}",
               system="You are a prompt engineering expert.")
    if out:
        print(out)
        return 0
    _no_key_note()
    util.header("Heuristic suggestions")
    tips = []
    if len(text) < 40:
        tips.append("Add more context and a clear goal.")
    if "you are" not in text.lower():
        tips.append("Define a role/persona (e.g. 'You are an expert ...').")
    if not re.search(r"(format|json|list|steps|table)", text.lower()):
        tips.append("Specify the desired output format.")
    if "example" not in text.lower():
        tips.append("Add 1-2 examples (few-shot).")
    for t in tips or ["Prompt looks reasonable."]:
        print("  - " + t)
    return 0


def summarize(args):
    """Summarize long text or a code file."""
    text = _read_input(args)
    if not text:
        util.err("usage: ntk ai summarize <text|file>")
        return 2
    out = _llm(f"Summarize concisely:\n\n{text[:12000]}")
    if out:
        print(out)
        return 0
    _no_key_note()
    # Offline: naive extractive summary (first + most 'keyword-dense' sentences)
    sents = re.split(r"(?<=[.!?])\s+", text)
    print("  " + " ".join(sents[:3]))
    return 0


def code_explain(args):
    """Explain a code block in simple words."""
    text = _read_input(args)
    if not text:
        util.err("usage: ntk ai code-explain <file|code>")
        return 2
    out = _llm(f"Explain this code simply:\n\n{text[:12000]}",
               system="You are a senior software engineer and teacher.")
    if out:
        print(out)
        return 0
    _no_key_note()
    return 1


def test_gen(args):
    """Generate unit tests for code."""
    text = _read_input(args)
    if not text:
        util.err("usage: ntk ai test-gen <file>")
        return 2
    out = _llm(f"Write thorough unit tests for this code:\n\n{text[:12000]}",
               system="You write clean, idiomatic unit tests.")
    if out:
        print(out)
        return 0
    _no_key_note()
    return 1


def fix_bugs(args):
    """Analyze code for bugs and suggest fixes."""
    text = _read_input(args)
    if not text:
        util.err("usage: ntk ai fix-bugs <file>")
        return 2
    out = _llm(f"Find bugs and suggest fixes:\n\n{text[:12000]}",
               system="You are a meticulous code reviewer.")
    if out:
        print(out)
        return 0
    _no_key_note()
    return 1


def refactor(args):
    """Suggest refactors for structure/performance."""
    text = _read_input(args)
    if not text:
        util.err("usage: ntk ai refactor <file>")
        return 2
    out = _llm(f"Suggest refactors for clarity and performance:\n\n{text[:12000]}")
    if out:
        print(out)
        return 0
    _no_key_note()
    return 1


def commit_msg(args):
    """Generate a commit message from staged diff."""
    rc, diff, _ = util.run(["git", "diff", "--cached"])
    if not diff.strip():
        rc, diff, _ = util.run(["git", "diff"])
    if not diff.strip():
        util.warn("no diff found (stage changes or edit files first)")
        return 1
    out = _llm(f"Write a conventional-commit message for this diff:\n\n{diff[:12000]}",
               system="You write concise conventional commit messages.")
    if out:
        print(out)
        return 0
    _no_key_note()
    # Offline heuristic
    files = re.findall(r"^\+\+\+ b/(.+)$", diff, re.M)
    scope = files[0].split("/")[0] if files else "core"
    print(f"  chore({scope}): update {len(files)} file(s)")
    return 0


def json_schema(args):
    """Generate a JSON Schema from a JSON object."""
    text = _read_input(args)
    if not text:
        util.err("usage: ntk ai json-schema <file.json|json>")
        return 2
    try:
        obj = json.loads(text)
    except Exception as e:
        util.err(f"invalid JSON: {e}")
        return 1

    def schema_of(v):
        if isinstance(v, bool):
            return {"type": "boolean"}
        if isinstance(v, int):
            return {"type": "integer"}
        if isinstance(v, float):
            return {"type": "number"}
        if isinstance(v, str):
            return {"type": "string"}
        if v is None:
            return {"type": "null"}
        if isinstance(v, list):
            return {"type": "array", "items": schema_of(v[0]) if v else {}}
        if isinstance(v, dict):
            return {"type": "object",
                    "properties": {k: schema_of(val) for k, val in v.items()},
                    "required": list(v.keys())}
        return {}
    schema = {"$schema": "http://json-schema.org/draft-07/schema#"}
    schema.update(schema_of(obj))
    print(json.dumps(schema, indent=2))
    return 0


def translate(args):
    """Translate text into another language (lang first)."""
    if len(args) < 2:
        util.err("usage: ntk ai translate <lang> <text|file>")
        return 2
    lang = args[0]
    text = _read_input(args[1:])
    out = _llm(f"Translate the following into {lang}. Output only the translation:\n\n{text}")
    if out:
        print(out)
        return 0
    _no_key_note()
    return 1


def sql_gen(args):
    """Write SQL from a natural-language request."""
    text = _read_input(args)
    if not text:
        util.err("usage: ntk ai sql-gen <request>")
        return 2
    out = _llm(f"Write a single SQL statement for: {text}. Output only SQL.",
               system="You are an expert SQL engineer.")
    if out:
        print(out)
        return 0
    _no_key_note()
    return 1


def shell_helper(args):
    """Translate natural language into a shell command."""
    text = _read_input(args)
    if not text:
        util.err("usage: ntk ai shell-helper <what you want>")
        return 2
    plat = "Windows PowerShell/CMD" if util.IS_WINDOWS else "Linux bash"
    out = _llm(f"Give the {plat} command for: {text}. Output only the command.",
               system="You are a shell expert. Output only the command, no prose.")
    if out:
        print("  " + out.strip().strip("`"))
        return 0
    _no_key_note()
    return 1


def embedding(args):
    """Semantic-ish similarity between two texts (offline cosine)."""
    if len(args) < 2:
        util.err('usage: ntk ai embedding "text one" "text two"')
        return 2
    a, b = args[0], args[1]

    def vec(t):
        words = re.findall(r"\w+", t.lower())
        d = {}
        for w in words:
            d[w] = d.get(w, 0) + 1
        return d
    va, vb = vec(a), vec(b)
    common = set(va) & set(vb)
    dot = sum(va[w] * vb[w] for w in common)
    na = math.sqrt(sum(v * v for v in va.values()))
    nb = math.sqrt(sum(v * v for v in vb.values()))
    sim = dot / (na * nb) if na and nb else 0.0
    util.kv("Cosine similarity", f"{sim:.3f}")
    print("  " + util.bar(sim))
    return 0


def regex_gen(args):
    """Generate a regex from a description (heuristic + LLM)."""
    text = _read_input(args)
    if not text:
        util.err("usage: ntk ai regex-gen <description>")
        return 2
    out = _llm(f"Give a single regex for: {text}. Output only the regex.",
               system="You output only a regular expression.")
    if out:
        print("  " + out.strip().strip("`"))
        return 0
    _no_key_note()
    patterns = {
        "email": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        "url": r"https?://[^\s]+",
        "ip": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        "phone": r"\+?\d[\d\s().-]{7,}\d",
        "date": r"\d{4}-\d{2}-\d{2}",
        "hex color": r"#[0-9a-fA-F]{6}",
    }
    low = text.lower()
    for k, p in patterns.items():
        if k in low:
            print(f"  {p}")
            return 0
    util.warn("no offline template matched; set an API key for full generation.")
    return 1


def transcribe(args):
    """Transcribe audio to text (needs whisper/API)."""
    if not args:
        util.err("usage: ntk ai transcribe <audio>")
        return 2
    key = os.environ.get("OPENAI_API_KEY")
    if key:
        import urllib.request
        base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
        try:
            import mimetypes
            boundary = "----ntk" + os.urandom(8).hex()
            fn = args[0]
            with open(fn, "rb") as f:
                filedata = f.read()
            parts = []
            parts.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"model\"\r\n\r\nwhisper-1\r\n")
            parts.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{os.path.basename(fn)}\"\r\n"
                         f"Content-Type: application/octet-stream\r\n\r\n")
            body = parts[0].encode() + parts[1].encode() + filedata + f"\r\n--{boundary}--\r\n".encode()
            req = urllib.request.Request(base + "/audio/transcriptions", data=body, headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": f"multipart/form-data; boundary={boundary}"})
            with urllib.request.urlopen(req, timeout=120) as r:
                print(json.loads(r.read()).get("text", ""))
            return 0
        except Exception as e:
            util.warn(f"API transcription failed: {e}")
    if util.which("whisper"):
        rc, o, e = util.run(["whisper", args[0], "--model", "base"])
        print(o or e)
        return rc
    util.warn("needs OPENAI_API_KEY or whisper CLI")
    return 1


COMMANDS = {
    "prompt-opt": prompt_opt, "tokens": tokens, "summarize": summarize,
    "code-explain": code_explain, "test-gen": test_gen, "fix-bugs": fix_bugs,
    "refactor": refactor, "commit-msg": commit_msg, "json-schema": json_schema,
    "translate": translate, "sql-gen": sql_gen, "shell-helper": shell_helper,
    "embedding": embedding, "regex-gen": regex_gen, "transcribe": transcribe,
}
