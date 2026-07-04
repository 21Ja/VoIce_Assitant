import os

def list_running_processes():
    try:
        os.system("tasklist")  # This will display running processes
        print("Processes listed successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")
