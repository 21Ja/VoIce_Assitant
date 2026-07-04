import scapy.all as scapy
import netifaces
import socket

def get_local_ip():
    """Get local IP address of the current system."""
    iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
    return netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']

def get_hostname(ip):
    """Get hostname from IP address."""
    try:
        hostname = socket.gethostbyaddr(ip)[0]  # Reverse DNS Lookup
    except socket.herror:
        hostname = "Unknown"
    return hostname

def scan_network():
    """Scan the local network and get IP, MAC, and Hostname."""
    local_ip = get_local_ip()
    ip_range = local_ip.rsplit('.', 1)[0] + ".1/24"
    
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request
    answered = scapy.srp(packet, timeout=2, verbose=False)[0]
    
    devices = []
    for response in answered:
        device_ip = response[1].psrc
        device_mac = response[1].hwsrc
        device_hostname = get_hostname(device_ip)
        
        devices.append({
            "ip": device_ip,
            "mac": device_mac,
            "hostname": device_hostname
        })
    
    return devices

if __name__ == "__main__":
    print("🔍 Scanning Network...")
    scanned_devices = scan_network()
    
    print("\n📋 Connected Devices:\n")
    print("{:<20} {:<20} {:<20}".format("IP Address", "MAC Address", "Hostname"))
    print("="*60)
    
    for device in scanned_devices:
        print("{:<20} {:<20} {:<20}".format(device["ip"], device["mac"], device["hostname"]))
