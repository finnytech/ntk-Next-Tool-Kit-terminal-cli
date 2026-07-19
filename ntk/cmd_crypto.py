"""Cryptography and encoding tools (ntk crypto ...)."""
import base64, binascii, hashlib, hmac, json, os, re, secrets, string, subprocess, uuid
from pathlib import Path
from . import util
from .util import col, C, run, IS_WINDOWS


def _text(args, usage):
    if not args:
        util.err("usage: " + usage); return None
    return " ".join(args)

def _digest(name, args):
    text = _text(args, f"ntk crypto {name} <text>")
    if text is None: return 2
    print(getattr(hashlib, name)(text.encode()).hexdigest()); return 0

def md5(args): """MD5 hash text."""; return _digest("md5", args)
def sha1(args): """SHA-1 hash text."""; return _digest("sha1", args)
def sha256(args): """SHA-256 hash text."""; return _digest("sha256", args)
def sha512(args): """SHA-512 hash text."""; return _digest("sha512", args)
def uuid_tool(args): """Generate a UUID."""; print(str(uuid.uuid4())); return 0

def password(args):
    """Generate a cryptographically random password."""
    try: n = int(args[0]) if args else 20
    except ValueError: util.err("length must be an integer"); return 2
    if n < 4 or n > 4096: util.err("length must be 4..4096"); return 2
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    print("".join(secrets.choice(alphabet) for _ in range(n))); return 0

def jwt_decode(args):
    """Decode JWT header and payload without verifying."""
    if len(args) != 1: util.err("usage: ntk crypto jwt-decode <token>"); return 2
    parts = args[0].split('.')
    if len(parts) != 3: util.err("invalid JWT: expected three segments"); return 1
    try:
        for label, part in zip(("header", "payload"), parts[:2]):
            raw = base64.urlsafe_b64decode(part + '=' * (-len(part) % 4))
            print(label + ":"); print(json.dumps(json.loads(raw), indent=2))
        print("signature: " + parts[2])
    except (ValueError, json.JSONDecodeError) as e: util.err(f"invalid JWT: {e}"); return 1
    return 0

def encrypt(args):
    """Encrypt text with Fernet."""
    if len(args) < 2: util.err("usage: ntk crypto encrypt <key> <text>"); return 2
    try:
        from cryptography.fernet import Fernet
    except ImportError: util.warn("needs cryptography: pip install cryptography"); return 1
    try: print(Fernet(args[0].encode()).encrypt(" ".join(args[1:]).encode()).decode()); return 0
    except Exception as e: util.err(str(e)); return 1

def decrypt(args):
    """Decrypt Fernet ciphertext."""
    if len(args) < 2: util.err("usage: ntk crypto decrypt <key> <token>"); return 2
    try:
        from cryptography.fernet import Fernet
        print(Fernet(args[0].encode()).decrypt(" ".join(args[1:]).encode()).decode()); return 0
    except ImportError: util.warn("needs cryptography: pip install cryptography"); return 1
    except Exception as e: util.err(str(e)); return 1

def totp(args):
    """Generate or verify an RFC 6238 TOTP."""
    if not args: util.err("usage: ntk crypto totp <base32-secret> [code]"); return 2
    try: key = base64.b32decode(args[0].upper() + '=' * (-len(args[0]) % 8), casefold=True)
    except Exception: util.err("invalid base32 secret"); return 1
    counter = int(__import__('time').time()) // 30
    digest = hmac.new(key, counter.to_bytes(8, 'big'), hashlib.sha1).digest(); off = digest[-1] & 15
    code = str((int.from_bytes(digest[off:off+4], 'big') & 0x7fffffff) % 1000000).zfill(6)
    if len(args) > 1: print("valid" if hmac.compare_digest(code, args[1]) else "invalid")
    else: print(code)
    return 0

def bcrypt_hash(args):
    """Hash a password with bcrypt."""
    if not args: util.err("usage: ntk crypto bcrypt <password>"); return 2
    try: import bcrypt
    except ImportError: util.warn("needs bcrypt: pip install bcrypt"); return 1
    print(bcrypt.hashpw(" ".join(args).encode(), bcrypt.gensalt()).decode()); return 0

def hash_check(args):
    """Check text against a hash."""
    if len(args) < 3: util.err("usage: ntk crypto hash-check <algorithm> <hash> <text>"); return 2
    alg, expected, text = args[0].lower(), args[1], " ".join(args[2:])
    if alg not in hashlib.algorithms_available: util.err("unknown hash algorithm"); return 2
    actual = hashlib.new(alg, text.encode()).hexdigest(); print("match" if hmac.compare_digest(actual, expected) else "no match"); return 0 if actual == expected else 1

def file_checksum(args):
    """Checksum a file."""
    if len(args) not in (1, 2): util.err("usage: ntk crypto file-checksum <file> [algorithm]"); return 2
    alg = args[1] if len(args) == 2 else 'sha256'
    if alg not in hashlib.algorithms_available: util.err("unknown hash algorithm"); return 2
    try:
        h = hashlib.new(alg)
        with open(args[0], 'rb') as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b''): h.update(chunk)
        print(h.hexdigest()); return 0
    except OSError as e: util.err(str(e)); return 1

def rsa_gen(args):
    """Generate an RSA private key with OpenSSL."""
    if not util.which('openssl'): util.warn("needs openssl executable"); return 1
    out = args[0] if args else 'private.pem'; rc, stdout, err = run(['openssl','genrsa','-out',out,'2048']); print(stdout or err); return rc

def _gpg(args, decrypting=False):
    if not util.which('gpg'): util.warn("needs gpg executable"); return 1
    if decrypting:
        rc, out, err = run(['gpg','--decrypt'] + args); print(out or err); return rc
    if len(args) < 2: util.err("usage: ntk crypto pgp-encrypt <recipient> <file>"); return 2
    rc, out, err = run(['gpg','--armor','--encrypt','--recipient',args[0],args[1]]); print(out or err); return rc

def pgp_encrypt(args): """Encrypt a file using GPG."""; return _gpg(args)
def pgp_decrypt(args): """Decrypt GPG input or file."""; return _gpg(args, True)
def rot13(args): """Apply ROT13 to text."""; print(__import__('codecs').decode(_text(args, 'ntk crypto rot13 <text>') or '', 'rot_13')); return 0 if args else 2
def cipher_list(args): """List available hashlib ciphers."""; print('\n'.join(sorted(hashlib.algorithms_available))); return 0

def secret_mask(args):
    """Mask likely secrets in text."""
    text = _text(args, 'ntk crypto secret-mask <text>')
    if text is None: return 2
    pattern = re.compile(r'(?i)(\b(?:password|passwd|secret|token|api[_-]?key|authorization)\b\s*[:=]\s*)([^\s,;]+)')
    print(pattern.sub(r'\1***MASKED***', text)); return 0

def random_bytes(args):
    """Generate random bytes as hexadecimal."""
    try: n = int(args[0]) if args else 16
    except ValueError: util.err("usage: ntk crypto random-bytes [count]"); return 2
    if n < 0 or n > 1048576: util.err("count must be 0..1048576"); return 2
    print(secrets.token_hex(n)); return 0

def leet(args):
    """Convert text to leetspeak."""
    text = _text(args, 'ntk crypto leet <text>')
    if text is None: return 2
    table = str.maketrans({'a':'4','e':'3','i':'1','o':'0','s':'5','t':'7','A':'4','E':'3','I':'1','O':'0','S':'5','T':'7'})
    print(text.translate(table)); return 0

COMMANDS = {'md5': md5, 'sha1': sha1, 'sha256': sha256, 'sha512': sha512, 'uuid': uuid_tool, 'password': password, 'jwt-decode': jwt_decode, 'encrypt': encrypt, 'decrypt': decrypt, 'totp': totp, 'bcrypt': bcrypt_hash, 'hash-check': hash_check, 'file-checksum': file_checksum, 'rsa-gen': rsa_gen, 'pgp-encrypt': pgp_encrypt, 'pgp-decrypt': pgp_decrypt, 'rot13': rot13, 'cipher-list': cipher_list, 'secret-mask': secret_mask, 'random-bytes': random_bytes, 'leet': leet}
