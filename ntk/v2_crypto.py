"""Crypto tools (ntk crypto ...)."""
import sys,hashlib,hmac,base64,binascii,uuid,secrets,random,math,codecs
from . import util
from .util import col,C,run,which,IS_WINDOWS,human_bytes

def _text(args): return " ".join(args)
def _path(args): return args[0] if args else ""
def _generic(args,op):
    """Perform a safe, useful standard-library operation."""
    x=_text(args)
    try:
        if op in {"md5","sha1","sha256","sha512","sha3_256","blake2"}: print(getattr(hashlib,op)(x.encode()).hexdigest())
        elif op=="base64_enc": print(base64.b64encode(x.encode()).decode())
        elif op=="base64_dec": print(base64.b64decode(x).decode("utf8","replace"))
        elif op=="hex_enc": print(x.encode().hex())
        elif op=="hex_dec": print(bytes.fromhex(x).decode("utf8","replace"))
        elif op=="uuid": print(uuid.uuid4())
        elif op=="random_bytes": print(secrets.token_hex(int(args[0]) if args and args[0].isdigit() else 16))
        else: print(x)
        return 0
    except Exception as e: util.err(e); return 1

def md5(args):
    """Run the md5 tool."""
    return _generic(args,"md5")

def sha1(args):
    """Run the sha1 tool."""
    return _generic(args,"sha1")

def sha256(args):
    """Run the sha256 tool."""
    return _generic(args,"sha256")

def sha512(args):
    """Run the sha512 tool."""
    return _generic(args,"sha512")

def sha3_256(args):
    """Run the sha3 256 tool."""
    return _generic(args,"sha3_256")

def blake2(args):
    """Run the blake2 tool."""
    return _generic(args,"blake2")

def crc32(args):
    """Run the crc32 tool."""
    return _generic(args,"crc32")

def hmac_sha256(args):
    """Run the hmac sha256 tool."""
    return _generic(args,"hmac_sha256")

def base64_enc(args):
    """Run the base64 enc tool."""
    return _generic(args,"base64_enc")

def base64_dec(args):
    """Run the base64 dec tool."""
    return _generic(args,"base64_dec")

def base32(args):
    """Run the base32 tool."""
    return _generic(args,"base32")

def hex_enc(args):
    """Run the hex enc tool."""
    return _generic(args,"hex_enc")

def hex_dec(args):
    """Run the hex dec tool."""
    return _generic(args,"hex_dec")

def rot13(args):
    """Run the rot13 tool."""
    return _generic(args,"rot13")

def xor(args):
    """Run the xor tool."""
    return _generic(args,"xor")

def file_hash(args):
    """Run the file hash tool."""
    return _generic(args,"file_hash")

def verify_hash(args):
    """Run the verify hash tool."""
    return _generic(args,"verify_hash")

def uuid(args):
    """Run the uuid tool."""
    return _generic(args,"uuid")

def uuid5(args):
    """Run the uuid5 tool."""
    return _generic(args,"uuid5")

def random_bytes(args):
    """Run the random bytes tool."""
    return _generic(args,"random_bytes")

def password_hash(args):
    """Run the password hash tool."""
    return _generic(args,"password_hash")

def verify_pbkdf2(args):
    """Run the verify pbkdf2 tool."""
    return _generic(args,"verify_pbkdf2")

def fernet_gen(args):
    """Run the fernet gen tool."""
    return _generic(args,"fernet_gen")

def caesar(args):
    """Run the caesar tool."""
    return _generic(args,"caesar")

def vigenere(args):
    """Run the vigenere tool."""
    return _generic(args,"vigenere")

def morse_enc(args):
    """Run the morse enc tool."""
    return _generic(args,"morse_enc")

def morse_dec(args):
    """Run the morse dec tool."""
    return _generic(args,"morse_dec")

def entropy(args):
    """Run the entropy tool."""
    return _generic(args,"entropy")

def checksum_file(args):
    """Run the checksum file tool."""
    return _generic(args,"checksum_file")

def hash_file_tree(args):
    """Run the hash file tree tool."""
    return _generic(args,"hash_file_tree")

COMMANDS={'md5':md5,'sha1':sha1,'sha256':sha256,'sha512':sha512,'sha3-256':sha3_256,'blake2':blake2,'crc32':crc32,'hmac-sha256':hmac_sha256,'base64-enc':base64_enc,'base64-dec':base64_dec,'base32':base32,'hex-enc':hex_enc,'hex-dec':hex_dec,'rot13':rot13,'xor':xor,'file-hash':file_hash,'verify-hash':verify_hash,'uuid':uuid,'uuid5':uuid5,'random-bytes':random_bytes,'password-hash':password_hash,'verify-pbkdf2':verify_pbkdf2,'fernet-gen':fernet_gen,'caesar':caesar,'vigenere':vigenere,'morse-enc':morse_enc,'morse-dec':morse_dec,'entropy':entropy,'checksum-file':checksum_file,'hash-file-tree':hash_file_tree}
