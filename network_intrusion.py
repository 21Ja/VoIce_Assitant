import scapy.all as scapy

def detect_intruders():
    """Detect unauthorized devices on the local network."""
    print("🔍 Scanning for unauthorized devices...")
    
    ip_range = "192.168.1.1/24"  # Change as per your network

    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    answered_list = scapy.srp(packet, timeout=2, verbose=False)[0]

    for sent, received in answered_list:
        print(f"🚨 Device detected: IP = {received.psrc}, MAC = {received.hwsrc}")

if __name__ == "__main__":
    detect_intruders()
