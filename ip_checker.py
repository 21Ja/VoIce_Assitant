import requests
import socket

def get_local_ip():
    """Get the local IP address of the current machine."""
    local_ip = socket.gethostbyname(socket.gethostname())
    print(f"📍 Local IP Address: {local_ip}")
    return local_ip

def get_public_ip():
    """Get the public IP address using an external API."""
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        public_ip = response.json()["ip"]
        print(f"🌍 Public IP Address: {public_ip}")
        return public_ip
    except requests.RequestException:
        print("❌ Error fetching public IP.")
        return None

if __name__ == "__main__":
    get_local_ip()
    get_public_ip()
