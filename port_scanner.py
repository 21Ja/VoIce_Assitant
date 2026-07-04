import socket

def scan_ports(target_ip):
    """Scan for open ports on a given IP address."""
    print(f"🔍 Scanning open ports on {target_ip}...")

    for port in range(1, 1025):  # Scanning common ports
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((target_ip, port)) == 0:
                print(f"✅ Port {port} is open.")

if __name__ == "__main__":
    scan_ports("192.168.1.1")  # Change to your target IP
