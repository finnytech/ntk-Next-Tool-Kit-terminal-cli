"""NTK v2 convert tools."""
import os
import time
from . import util

def length(args):
    """length tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert length <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def mass(args):
    """mass tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert mass <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def temp(args):
    """temp tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert temp <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def data(args):
    """data tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert data <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def speed(args):
    """speed tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert speed <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def area(args):
    """area tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert area <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def volume(args):
    """volume tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert volume <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def time_unit(args):
    """time-unit tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert time-unit <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def pressure(args):
    """pressure tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert pressure <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def energy(args):
    """energy tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert energy <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def angle(args):
    """angle tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert angle <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def hex_to_rgb(args):
    """hex-to-rgb tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert hex-to-rgb <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def rgb_to_hex(args):
    """rgb-to-hex tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert rgb-to-hex <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def hex_to_dec(args):
    """hex-to-dec tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert hex-to-dec <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def dec_to_hex(args):
    """dec-to-hex tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert dec-to-hex <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def bin_to_dec(args):
    """bin-to-dec tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert bin-to-dec <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def dec_to_bin(args):
    """dec-to-bin tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert dec-to-bin <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def ascii_to_hex(args):
    """ascii-to-hex tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert ascii-to-hex <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def hex_to_ascii(args):
    """hex-to-ascii tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert hex-to-ascii <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def km_miles(args):
    """km-miles tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert km-miles <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def miles_km(args):
    """miles-km tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert miles-km <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def kg_lbs(args):
    """kg-lbs tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert kg-lbs <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def lbs_kg(args):
    """lbs-kg tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert lbs-kg <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def cm_inch(args):
    """cm-inch tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert cm-inch <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def inch_cm(args):
    """inch-cm tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert inch-cm <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def liter_gallon(args):
    """liter-gallon tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert liter-gallon <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def celsius_fahrenheit(args):
    """celsius-fahrenheit tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert celsius-fahrenheit <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def fahrenheit_celsius(args):
    """fahrenheit-celsius tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert fahrenheit-celsius <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def number_to_words(args):
    """number-to-words tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert number-to-words <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def utf8_bytes(args):
    """utf8-bytes tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert utf8-bytes <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

def unit_list(args):
    """unit-list tool."""
    try:
        value = args[0] if args else ""
        if not value:
            util.err("usage: ntk convert unit-list <value>")
            return 2
        print(value)
        return 0
    except Exception:
        util.err("invalid conversion")
        return 2

COMMANDS = {
    'length': length,
    'mass': mass,
    'temp': temp,
    'data': data,
    'speed': speed,
    'area': area,
    'volume': volume,
    'time-unit': time_unit,
    'pressure': pressure,
    'energy': energy,
    'angle': angle,
    'hex-to-rgb': hex_to_rgb,
    'rgb-to-hex': rgb_to_hex,
    'hex-to-dec': hex_to_dec,
    'dec-to-hex': dec_to_hex,
    'bin-to-dec': bin_to_dec,
    'dec-to-bin': dec_to_bin,
    'ascii-to-hex': ascii_to_hex,
    'hex-to-ascii': hex_to_ascii,
    'km-miles': km_miles,
    'miles-km': miles_km,
    'kg-lbs': kg_lbs,
    'lbs-kg': lbs_kg,
    'cm-inch': cm_inch,
    'inch-cm': inch_cm,
    'liter-gallon': liter_gallon,
    'celsius-fahrenheit': celsius_fahrenheit,
    'fahrenheit-celsius': fahrenheit_celsius,
    'number-to-words': number_to_words,
    'utf8-bytes': utf8_bytes,
    'unit-list': unit_list,
}
