import uuid

def get_mac_address():
    """Get the MAC address of the current system."""
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0, 48, 8)])
    print(f"🔍 MAC Address: {mac}")
    return mac

if __name__ == "__main__":
    get_mac_address()
