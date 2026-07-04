import os

def change_ip():
    print("🛠 Changing IP Address...")
    os.system("ipconfig /release")
    os.system("ipconfig /renew")
    print("✅ IP Address Changed Successfully!")
