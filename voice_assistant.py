import speech_recognition as sr
import pyttsx3
import google_search
import system_control
import weather_news
import network_scan
import ip_changer
import whatsapp
import jokes
import screenshot
import webbrowser
import os

# New Features
import ip_checker
import mac_finder
import port_scanner
import ping_test
import network_intrusion
import keylogger_protection
import process_monitor
import task_manager

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"👤 You said: {command}")
            return command
        except:
            print("🔇 Couldn't recognize, please try again.")
            return ""

def execute_command(command):
    if "scan network" in command:
        devices = network_scan.scan_network()
        print(devices)
        speak("Network scanning completed.")
    
    elif "change ip" in command:
        ip_changer.change_ip()

    elif "show my ip" in command:
        local_ip = ip_checker.get_local_ip()
        public_ip = ip_checker.get_public_ip()
        speak(f"Your local IP is {local_ip} and public IP is {public_ip}.")


    elif "what is my mac address" in command:
        mac_address = mac_finder.get_mac_address()
        speak(f"Your MAC address is {mac_address}.")

    elif "scan ports" in command:
        target_ip = input("Enter target IP: ")
        open_ports = port_scanner.scan_ports(target_ip)
        speak(f"Open ports on {target_ip}: {open_ports}")

    elif "check internet" in command:
        ping_test.ping_test()

    elif "scan network for intruders" in command:
        network_intrusion.detect_intruders()

    elif "detect keylogger" in command:
        keylogger_protection.detect_keylogger()

    # Check for running processes
    if "show running process" in command or "list running processes" in command:
        process_monitor.list_running_processes()
        speak("Showing running processes.")

    elif "open task manager" in command:
        task_manager.open_task_manager()

    elif "search" in command:
        query = command.replace("search", "").strip()
        google_search.google_search(query)

    elif "shutdown" in command:
        system_control.shutdown()
    elif "restart" in command:
        system_control.restart()

    elif "weather" in command:
        city_name = command.replace("weather of", "").strip()
        weather_report = weather_news.get_weather(city_name)
        print(weather_report)
        speak(weather_report)

    elif "send message" in command:
        whatsapp.send_message()

    elif "joke" in command:
        jokes.tell_joke()

    elif "screenshot" in command:
        screenshot.take_screenshot()

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    
    elif "play music" in command:
        webbrowser.open("https://www.youtube.com/results?search_query=music")
        speak("Playing music.")

    elif "exit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Command not recognized. Please try again.")

def start_assistant():
    while True:
        command = listen()
        if command:
            execute_command(command)
import speech_recognition as sr
import pyttsx3
import google_search
import system_control
import weather_news
import network_scan
import ip_changer
import whatsapp
import jokes
import screenshot
import webbrowser
import os

# New Features
import ip_checker
import mac_finder
import port_scanner
import ping_test
import network_intrusion
import keylogger_protection
import process_monitor
import task_manager

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"👤 You said: {command}")
            return command
        except:
            print("🔇 Couldn't recognize, please try again.")
            return ""

def execute_command(command):
    if "scan network" in command:
        devices = network_scan.scan_network()
        print(devices)
        speak("Network scanning completed.")
    
    elif "change ip" in command:
        ip_changer.change_ip()

    elif "show my ip" in command:
        local_ip = ip_checker.get_local_ip()
        public_ip = ip_checker.get_public_ip()
        speak(f"Your local IP is {local_ip} and public IP is {public_ip}.")


    elif "what is my mac address" in command:
        mac_address = mac_finder.get_mac_address()
        speak(f"Your MAC address is {mac_address}.")

    elif "scan ports" in command:
        target_ip = input("Enter target IP: ")
        open_ports = port_scanner.scan_ports(target_ip)
        speak(f"Open ports on {target_ip}: {open_ports}")

    elif "check internet" in command:
        ping_test.ping_test()

    elif "scan network for intruders" in command:
        network_intrusion.detect_intruders()

    elif "detect keylogger" in command:
        keylogger_protection.detect_keylogger()

    # Check for running processes
    if "show running process" in command or "list running processes" in command:
        process_monitor.list_running_processes()
        speak("Showing running processes.")

    elif "open task manager" in command:
        task_manager.open_task_manager()

    elif "search" in command:
        query = command.replace("search", "").strip()
        google_search.google_search(query)

    elif "shutdown" in command:
        system_control.shutdown()
    elif "restart" in command:
        system_control.restart()

    elif "weather" in command:
        city_name = command.replace("weather of", "").strip()
        weather_report = weather_news.get_weather(city_name)
        print(weather_report)
        speak(weather_report)

    elif "send message" in command:
        whatsapp.send_message()

    elif "joke" in command:
        jokes.tell_joke()

    elif "screenshot" in command:
        screenshot.take_screenshot()

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    
    elif "play music" in command:
        webbrowser.open("https://www.youtube.com/results?search_query=music")
        speak("Playing music.")

    elif "exit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Command not recognized. Please try again.")

def start_assistant():
    while True:
        command = listen()
        if command:
            execute_command(command)
