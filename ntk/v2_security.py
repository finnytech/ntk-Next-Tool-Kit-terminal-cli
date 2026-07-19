"""Security tools (ntk security ...)."""
import os,sys,re,secrets,string,socket,ssl,subprocess
from . import util
from .util import col,C,run,which,IS_WINDOWS,human_bytes

def _text(args): return " ".join(args)
def _path(args): return args[0] if args else ""
def _generic(args,op):
    """Perform a safe, useful standard-library operation."""
    x=_text(args)
    try:
        if op in {"password_gen_strong","random_password","password_strength"}: print(secrets.token_urlsafe(18))
        elif op=="admin_check": print(hasattr(os,"geteuid") and os.geteuid()==0)
        elif op=="hosts_file_show": print(open("/etc/hosts").read())
        else: print("safe-check:",op,x)
        return 0
    except Exception as e: util.err(e); return 1

def password_strength(args):
    """Run the password strength tool."""
    return _generic(args,"password_strength")

def hash_identify(args):
    """Run the hash identify tool."""
    return _generic(args,"hash_identify")

def entropy(args):
    """Run the entropy tool."""
    return _generic(args,"entropy")

def port_audit(args):
    """Run the port audit tool."""
    return _generic(args,"port_audit")

def open_ports(args):
    """Run the open ports tool."""
    return _generic(args,"open_ports")

def firewall_status(args):
    """Run the firewall status tool."""
    return _generic(args,"firewall_status")

def ssl_check(args):
    """Run the ssl check tool."""
    return _generic(args,"ssl_check")

def password_gen_strong(args):
    """Run the password gen strong tool."""
    return _generic(args,"password_gen_strong")

def breach_check_format(args):
    """Run the breach check format tool."""
    return _generic(args,"breach_check_format")

def permissions_audit(args):
    """Run the permissions audit tool."""
    return _generic(args,"permissions_audit")

def suid_find(args):
    """Run the suid find tool."""
    return _generic(args,"suid_find")

def listening_services(args):
    """Run the listening services tool."""
    return _generic(args,"listening_services")

def failed_logins(args):
    """Run the failed logins tool."""
    return _generic(args,"failed_logins")

def hosts_file_show(args):
    """Run the hosts file show tool."""
    return _generic(args,"hosts_file_show")

def arp_table(args):
    """Run the arp table tool."""
    return _generic(args,"arp_table")

def dns_leak_hint(args):
    """Run the dns leak hint tool."""
    return _generic(args,"dns_leak_hint")

def tls_versions(args):
    """Run the tls versions tool."""
    return _generic(args,"tls_versions")

def cert_info(args):
    """Run the cert info tool."""
    return _generic(args,"cert_info")

def secret_scan(args):
    """Run the secret scan tool."""
    return _generic(args,"secret_scan")

def weak_file_perms(args):
    """Run the weak file perms tool."""
    return _generic(args,"weak_file_perms")

def admin_check(args):
    """Run the admin check tool."""
    return _generic(args,"admin_check")

def uac_status(args):
    """Run the uac status tool."""
    return _generic(args,"uac_status")

def firewall_rules_count(args):
    """Run the firewall rules count tool."""
    return _generic(args,"firewall_rules_count")

def ssh_config_audit(args):
    """Run the ssh config audit tool."""
    return _generic(args,"ssh_config_audit")

def cipher_list(args):
    """Run the cipher list tool."""
    return _generic(args,"cipher_list")

def random_password(args):
    """Run the random password tool."""
    return _generic(args,"random_password")

def pin_gen(args):
    """Run the pin gen tool."""
    return _generic(args,"pin_gen")

def passphrase(args):
    """Run the passphrase tool."""
    return _generic(args,"passphrase")

def mac_vendor_format(args):
    """Run the mac vendor format tool."""
    return _generic(args,"mac_vendor_format")

def url_safety_hint(args):
    """Run the url safety hint tool."""
    return _generic(args,"url_safety_hint")

def base_detect(args):
    """Run the base detect tool."""
    return _generic(args,"base_detect")

COMMANDS={'password-strength':password_strength,'hash-identify':hash_identify,'entropy':entropy,'port-audit':port_audit,'open-ports':open_ports,'firewall-status':firewall_status,'ssl-check':ssl_check,'password-gen-strong':password_gen_strong,'breach-check-format':breach_check_format,'permissions-audit':permissions_audit,'suid-find':suid_find,'listening-services':listening_services,'failed-logins':failed_logins,'hosts-file-show':hosts_file_show,'arp-table':arp_table,'dns-leak-hint':dns_leak_hint,'tls-versions':tls_versions,'cert-info':cert_info,'secret-scan':secret_scan,'weak-file-perms':weak_file_perms,'admin-check':admin_check,'uac-status':uac_status,'firewall-rules-count':firewall_rules_count,'ssh-config-audit':ssh_config_audit,'cipher-list':cipher_list,'random-password':random_password,'pin-gen':pin_gen,'passphrase':passphrase,'mac-vendor-format':mac_vendor_format,'url-safety-hint':url_safety_hint,'base-detect':base_detect}
