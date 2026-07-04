import psutil

def detect_keylogger():
    """Check for suspicious keylogging processes."""
    keylogger_signatures = ["keylog", "hook", "keyboard", "log"]

    print("🔍 Scanning for keyloggers...")
    
    for process in psutil.process_iter(attrs=['pid', 'name']):
        process_name = process.info['name'].lower()
        if any(keyword in process_name for keyword in keylogger_signatures):
            print(f"⚠️ Suspicious Keylogger Detected: {process_name} (PID: {process.info['pid']})")

if __name__ == "__main__":
    detect_keylogger()
