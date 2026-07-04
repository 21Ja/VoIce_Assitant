import os

def shutdown():
    print("🔴 Shutting down...")
    os.system("shutdown /s /t 5")

def restart():
    print("🔄 Restarting...")
    os.system("shutdown /r /t 5")

def lock():
    print("🔒 Locking system...")
    os.system("rundll32.exe user32.dll,LockWorkStation")
