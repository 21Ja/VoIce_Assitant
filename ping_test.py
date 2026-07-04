import os

def ping_test(host="8.8.8.8"):
    """Check internet speed by pinging Google's DNS server."""
    response = os.system(f"ping -n 4 {host}")  # For Windows (-c 4 for Linux)
    
    if response == 0:
        print(f"✅ Internet connection is working.")
    else:
        print("❌ No internet connection.")

if __name__ == "__main__":
    ping_test()
