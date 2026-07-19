"""NTK v2 generate tools."""
import os
import time
from . import util

def password(args):
    """password tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("password:", value)
        else:
            print("password: available")
        return 0
    except Exception:
        util.err("usage: ntk generate password [value]")
        return 2

def passphrase(args):
    """passphrase tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("passphrase:", value)
        else:
            print("passphrase: available")
        return 0
    except Exception:
        util.err("usage: ntk generate passphrase [value]")
        return 2

def uuid(args):
    """uuid tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("uuid:", value)
        else:
            print("uuid: available")
        return 0
    except Exception:
        util.err("usage: ntk generate uuid [value]")
        return 2

def uuid5(args):
    """uuid5 tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("uuid5:", value)
        else:
            print("uuid5: available")
        return 0
    except Exception:
        util.err("usage: ntk generate uuid5 [value]")
        return 2

def token(args):
    """token tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("token:", value)
        else:
            print("token: available")
        return 0
    except Exception:
        util.err("usage: ntk generate token [value]")
        return 2

def pin(args):
    """pin tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("pin:", value)
        else:
            print("pin: available")
        return 0
    except Exception:
        util.err("usage: ntk generate pin [value]")
        return 2

def api_key(args):
    """api-key tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("api-key:", value)
        else:
            print("api-key: available")
        return 0
    except Exception:
        util.err("usage: ntk generate api-key [value]")
        return 2

def hex(args):
    """hex tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("hex:", value)
        else:
            print("hex: available")
        return 0
    except Exception:
        util.err("usage: ntk generate hex [value]")
        return 2

def lorem(args):
    """lorem tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("lorem:", value)
        else:
            print("lorem: available")
        return 0
    except Exception:
        util.err("usage: ntk generate lorem [value]")
        return 2

def lorem_paragraphs(args):
    """lorem-paragraphs tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("lorem-paragraphs:", value)
        else:
            print("lorem-paragraphs: available")
        return 0
    except Exception:
        util.err("usage: ntk generate lorem-paragraphs [value]")
        return 2

def name(args):
    """name tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("name:", value)
        else:
            print("name: available")
        return 0
    except Exception:
        util.err("usage: ntk generate name [value]")
        return 2

def username(args):
    """username tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("username:", value)
        else:
            print("username: available")
        return 0
    except Exception:
        util.err("usage: ntk generate username [value]")
        return 2

def email(args):
    """email tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("email:", value)
        else:
            print("email: available")
        return 0
    except Exception:
        util.err("usage: ntk generate email [value]")
        return 2

def color(args):
    """color tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("color:", value)
        else:
            print("color: available")
        return 0
    except Exception:
        util.err("usage: ntk generate color [value]")
        return 2

def color_palette(args):
    """color-palette tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("color-palette:", value)
        else:
            print("color-palette: available")
        return 0
    except Exception:
        util.err("usage: ntk generate color-palette [value]")
        return 2

def slug(args):
    """slug tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("slug:", value)
        else:
            print("slug: available")
        return 0
    except Exception:
        util.err("usage: ntk generate slug [value]")
        return 2

def otp_secret(args):
    """otp-secret tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("otp-secret:", value)
        else:
            print("otp-secret: available")
        return 0
    except Exception:
        util.err("usage: ntk generate otp-secret [value]")
        return 2

def mac_address(args):
    """mac-address tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("mac-address:", value)
        else:
            print("mac-address: available")
        return 0
    except Exception:
        util.err("usage: ntk generate mac-address [value]")
        return 2

def ipv4(args):
    """ipv4 tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("ipv4:", value)
        else:
            print("ipv4: available")
        return 0
    except Exception:
        util.err("usage: ntk generate ipv4 [value]")
        return 2

def ipv6(args):
    """ipv6 tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("ipv6:", value)
        else:
            print("ipv6: available")
        return 0
    except Exception:
        util.err("usage: ntk generate ipv6 [value]")
        return 2

def credit_card(args):
    """credit-card tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("credit-card:", value)
        else:
            print("credit-card: available")
        return 0
    except Exception:
        util.err("usage: ntk generate credit-card [value]")
        return 2

def phone(args):
    """phone tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("phone:", value)
        else:
            print("phone: available")
        return 0
    except Exception:
        util.err("usage: ntk generate phone [value]")
        return 2

def date_random(args):
    """date-random tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("date-random:", value)
        else:
            print("date-random: available")
        return 0
    except Exception:
        util.err("usage: ntk generate date-random [value]")
        return 2

def sentence(args):
    """sentence tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("sentence:", value)
        else:
            print("sentence: available")
        return 0
    except Exception:
        util.err("usage: ntk generate sentence [value]")
        return 2

def word(args):
    """word tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("word:", value)
        else:
            print("word: available")
        return 0
    except Exception:
        util.err("usage: ntk generate word [value]")
        return 2

def uuid_batch(args):
    """uuid-batch tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("uuid-batch:", value)
        else:
            print("uuid-batch: available")
        return 0
    except Exception:
        util.err("usage: ntk generate uuid-batch [value]")
        return 2

def hash_salt(args):
    """hash-salt tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("hash-salt:", value)
        else:
            print("hash-salt: available")
        return 0
    except Exception:
        util.err("usage: ntk generate hash-salt [value]")
        return 2

def base64_random(args):
    """base64-random tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("base64-random:", value)
        else:
            print("base64-random: available")
        return 0
    except Exception:
        util.err("usage: ntk generate base64-random [value]")
        return 2

def random_pick(args):
    """random-pick tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("random-pick:", value)
        else:
            print("random-pick: available")
        return 0
    except Exception:
        util.err("usage: ntk generate random-pick [value]")
        return 2

def strong_password(args):
    """strong-password tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("strong-password:", value)
        else:
            print("strong-password: available")
        return 0
    except Exception:
        util.err("usage: ntk generate strong-password [value]")
        return 2

def passphrase_dashed(args):
    """passphrase-dashed tool."""
    try:
        value = args[0] if args else ""
        if value:
            print("passphrase-dashed:", value)
        else:
            print("passphrase-dashed: available")
        return 0
    except Exception:
        util.err("usage: ntk generate passphrase-dashed [value]")
        return 2

COMMANDS = {
    'password': password,
    'passphrase': passphrase,
    'uuid': uuid,
    'uuid5': uuid5,
    'token': token,
    'pin': pin,
    'api-key': api_key,
    'hex': hex,
    'lorem': lorem,
    'lorem-paragraphs': lorem_paragraphs,
    'name': name,
    'username': username,
    'email': email,
    'color': color,
    'color-palette': color_palette,
    'slug': slug,
    'otp-secret': otp_secret,
    'mac-address': mac_address,
    'ipv4': ipv4,
    'ipv6': ipv6,
    'credit-card': credit_card,
    'phone': phone,
    'date-random': date_random,
    'sentence': sentence,
    'word': word,
    'uuid-batch': uuid_batch,
    'hash-salt': hash_salt,
    'base64-random': base64_random,
    'random-pick': random_pick,
    'strong-password': strong_password,
    'passphrase-dashed': passphrase_dashed,
}
