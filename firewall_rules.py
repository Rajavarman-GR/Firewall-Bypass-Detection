blocked_ips = set()

def block_ip(ip):
    blocked_ips.add(ip)
    print(f"[Firewall] Blocked IP: {ip}")

def is_ip_blocked(ip):
    return ip in blocked_ips
