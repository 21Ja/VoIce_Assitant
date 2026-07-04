import pyautogui
import datetime
import os

def take_screenshot():
    # Screenshot filename with timestamp
    filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    
    # Save in the current project directory
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"✅ Screenshot saved as {filename}")
