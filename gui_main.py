import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import sys
import os

# Add the directory containing your scripts to the Python path
# This assumes gui_assistant.py is in the same directory as your other scripts
# If not, adjust the path accordingly.
sys.path.append(os.path.dirname(__file__))

# Import your functional scripts
import voice_assistant  # For the core voice listening and speaking
import google_search
import ip_checker
import mac_finder
import port_scanner
import ping_test
import network_intrusion
import keylogger_protection
import process_monitor
import task_manager
import network_scan
import ip_changer
import jokes
import screenshot
import system_control
import weather_news
import whatsapp

class NetVoiceAssistantGUI:
    def __init__(self, master):
        self.master = master
        master.title("NetVoice Assistant")
        master.geometry("800x600")
        master.configure(bg="#333333")  # Dark background

        # --- Styles ---
        self.label_font = ("Helvetica Neue", 14, "bold")
        self.button_font = ("Helvetica Neue", 12)
        self.text_font = ("Consolas", 10)

        # --- Output Area ---
        self.output_label = tk.Label(master, text="Assistant Output:", font=self.label_font, fg="#00FF00", bg="#333333")
        self.output_label.pack(pady=(10, 5))

        self.output_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=80, height=20,
                                                     font=self.text_font, bg="#1a1a1a", fg="#00FF00", insertbackground="#00FF00")
        self.output_text.pack(pady=(0, 10), padx=10, fill=tk.BOTH, expand=True)
        self.output_text.insert(tk.END, "🎤 NetVoice Assistant GUI is ready. Click a button or speak a command.\n")
        self.output_text.config(state=tk.DISABLED) # Make it read-only

        # --- Command/Status Label ---
        self.status_label = tk.Label(master, text="Status: Ready", font=self.label_font, fg="#FFD700", bg="#333333")
        self.status_label.pack(pady=(5, 10))

        # --- Control Buttons Frame ---
        self.control_frame = tk.Frame(master, bg="#444444", bd=2, relief=tk.GROOVE)
        self.control_frame.pack(pady=(5, 10), padx=10, fill=tk.X)

        self.start_button = tk.Button(self.control_frame, text="Start Listening", command=self.start_listening_thread,
                                      font=self.button_font, bg="#4CAF50", fg="white", activebackground="#45a049", activeforeground="white")
        self.start_button.pack(side=tk.LEFT, padx=10, pady=5, expand=True, fill=tk.X)

        self.stop_button = tk.Button(self.control_frame, text="Stop Listening", command=self.stop_listening,
                                     font=self.button_font, bg="#f44336", fg="white", activebackground="#da190b", activeforeground="white")
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=5, expand=True, fill=tk.X)
        self.stop_button.config(state=tk.DISABLED) # Disable initially

        # --- Functionality Buttons Frame ---
        self.func_frame1 = tk.Frame(master, bg="#333333")
        self.func_frame1.pack(pady=5, padx=10, fill=tk.X)

        self.create_button(self.func_frame1, "Scan Network", self.gui_scan_network)
        self.create_button(self.func_frame1, "Check My IP", self.gui_show_my_ip)
        self.create_button(self.func_frame1, "What's My MAC?", self.gui_get_mac_address)
        self.create_button(self.func_frame1, "Ping Test", self.gui_ping_test)
        self.create_button(self.func_frame1, "Detect Keylogger", self.gui_detect_keylogger)

        self.func_frame2 = tk.Frame(master, bg="#333333")
        self.func_frame2.pack(pady=5, padx=10, fill=tk.X)

        self.create_button(self.func_frame2, "Tell a Joke", self.gui_tell_joke)
        self.create_button(self.func_frame2, "Take Screenshot", self.gui_take_screenshot)
        self.create_button(self.func_frame2, "Show Processes", self.gui_list_running_processes)
        self.create_button(self.func_frame2, "Open Task Manager", self.gui_open_task_manager)
        self.create_button(self.func_frame2, "Shutdown", self.gui_shutdown)

        # --- Input for specific commands ---
        self.input_frame = tk.Frame(master, bg="#333333")
        self.input_frame.pack(pady=5, padx=10, fill=tk.X)

        tk.Label(self.input_frame, text="Target IP (for Port Scan):", font=self.button_font, fg="white", bg="#333333").pack(side=tk.LEFT, padx=5)
        self.target_ip_entry = tk.Entry(self.input_frame, width=20, font=self.text_font, bg="#1a1a1a", fg="#00FF00", insertbackground="#00FF00")
        self.target_ip_entry.pack(side=tk.LEFT, padx=5)
        self.target_ip_entry.insert(0, "192.168.1.1") # Default value
        self.create_button(self.input_frame, "Scan Ports", self.gui_scan_ports)

        tk.Label(self.input_frame, text="City (for Weather):", font=self.button_font, fg="white", bg="#333333").pack(side=tk.LEFT, padx=5)
        self.city_entry = tk.Entry(self.input_frame, width=15, font=self.text_font, bg="#1a1a1a", fg="#00FF00", insertbackground="#00FF00")
        self.city_entry.pack(side=tk.LEFT, padx=5)
        self.city_entry.insert(0, "Delhi") # Default value
        self.create_button(self.input_frame, "Get Weather", self.gui_get_weather)


        self.listening = False
        self.voice_command_thread = None

    def create_button(self, parent_frame, text, command_func):
        button = tk.Button(parent_frame, text=text, command=command_func,
                           font=self.button_font, bg="#555555", fg="white",
                           activebackground="#666666", activeforeground="white",
                           relief=tk.RAISED, bd=2)
        button.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X)

    def update_output(self, text):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, text + "\n")
        self.output_text.see(tk.END) # Scroll to the end
        self.output_text.config(state=tk.DISABLED)

    def set_status(self, text):
        self.status_label.config(text=f"Status: {text}")

    def start_listening_thread(self):
        if not self.listening:
            self.listening = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.set_status("Listening...")
            self.voice_command_thread = threading.Thread(target=self._listen_for_commands)
            self.voice_command_thread.daemon = True # Allow thread to exit with main program
            self.voice_command_thread.start()
            self.update_output("Assistant started listening for voice commands.")

    def stop_listening(self):
        if self.listening:
            self.listening = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.set_status("Ready")
            self.update_output("Assistant stopped listening.")
            # You might need a more robust way to stop speech_recognition's listen()
            # For now, it will just exit the loop after the current listen attempt.

    def _listen_for_commands(self):
        """Internal function to continuously listen for commands."""
        while self.listening:
            command = voice_assistant.listen()
            if command and self.listening: # Ensure we haven't stopped listening while recognition was happening
                self.master.after(0, self.set_status, f"You said: {command}")
                self.master.after(0, self.update_output, f"👤 You said: {command}")
                # Execute command in a separate thread to keep GUI responsive
                threading.Thread(target=self._execute_voice_command, args=(command,), daemon=True).start()
            elif self.listening: # If command is empty (recognition failed) and still listening
                self.master.after(0, self.set_status, "Couldn't recognize, please try again.")

    def _execute_voice_command(self, command):
        """Executes a voice command and updates the GUI."""
        self.master.after(0, self.set_status, f"Executing: {command}...")
        # Redirect stdout to the GUI output_text for functions that print
        old_stdout = sys.stdout
        sys.stdout = TextRedirector(self.output_text, self.master)
        try:
            # This is a simplified version. In a real app, you'd parse the command
            # and call the appropriate function, perhaps with arguments extracted from the command.
            voice_assistant.execute_command(command) # This function already handles many commands
        except Exception as e:
            self.master.after(0, self.update_output, f"Error executing command: {e}")
            messagebox.showerror("Error", f"Error executing command: {e}")
        finally:
            sys.stdout = old_stdout # Restore stdout
            self.master.after(0, self.set_status, "Ready")


    # --- GUI Wrapper Functions for your scripts ---
    # These functions will be called by the GUI buttons.
    # They should call your existing script functions and update the GUI.

    def gui_scan_network(self):
        self.update_output("🔍 Scanning Network...")
        threading.Thread(target=self._scan_network_task, daemon=True).start()

    def _scan_network_task(self):
        try:
            devices = network_scan.scan_network()
            output = "\n📋 Connected Devices:\n"
            output += "{:<20} {:<20} {:<20}\n".format("IP Address", "MAC Address", "Hostname")
            output += "="*60 + "\n"
            for device in devices:
                output += "{:<20} {:<20} {:<20}\n".format(device["ip"], device["mac"], device["hostname"])
            self.master.after(0, self.update_output, output)
            self.master.after(0, voice_assistant.speak, "Network scanning completed.")
        except Exception as e:
            self.master.after(0, self.update_output, f"❌ Error scanning network: {e}")
            self.master.after(0, voice_assistant.speak, f"Error scanning network: {e}")

    def gui_show_my_ip(self):
        self.update_output("📍 Getting IP Addresses...")
        threading.Thread(target=self._show_my_ip_task, daemon=True).start()

    def _show_my_ip_task(self):
        local_ip = ip_checker.get_local_ip()
        public_ip = ip_checker.get_public_ip()
        output = f"📍 Local IP Address: {local_ip}\n"
        output += f"🌍 Public IP Address: {public_ip}"
        self.master.after(0, self.update_output, output)
        self.master.after(0, voice_assistant.speak, f"Your local IP is {local_ip} and public IP is {public_ip}.")

    def gui_get_mac_address(self):
        self.update_output("🔍 Getting MAC Address...")
        threading.Thread(target=self._get_mac_address_task, daemon=True).start()

    def _get_mac_address_task(self):
        mac_address = mac_finder.get_mac_address()
        self.master.after(0, self.update_output, f"🔍 MAC Address: {mac_address}")
        self.master.after(0, voice_assistant.speak, f"Your MAC address is {mac_address}.")

    def gui_ping_test(self):
        self.update_output("🌐 Running Ping Test...")
        threading.Thread(target=self._ping_test_task, daemon=True).start()

    def _ping_test_task(self):
        old_stdout = sys.stdout
        sys.stdout = TextRedirector(self.output_text, self.master)
        try:
            ping_test.ping_test()
        finally:
            sys.stdout = old_stdout
        self.master.after(0, voice_assistant.speak, "Ping test completed.")

    def gui_detect_keylogger(self):
        self.update_output("🔍 Scanning for keyloggers...")
        threading.Thread(target=self._detect_keylogger_task, daemon=True).start()

    def _detect_keylogger_task(self):
        old_stdout = sys.stdout
        sys.stdout = TextRedirector(self.output_text, self.master)
        try:
            keylogger_protection.detect_keylogger()
        finally:
            sys.stdout = old_stdout
        self.master.after(0, voice_assistant.speak, "Keylogger detection completed.")

    def gui_tell_joke(self):
        self.update_output("😂 Telling a joke...")
        threading.Thread(target=self._tell_joke_task, daemon=True).start()

    def _tell_joke_task(self):
        joke = jokes.tell_joke()
        self.master.after(0, self.update_output, f"😂 {joke}")
        self.master.after(0, voice_assistant.speak, joke)

    def gui_take_screenshot(self):
        self.update_output("📸 Taking a screenshot...")
        threading.Thread(target=self._take_screenshot_task, daemon=True).start()

    def _take_screenshot_task(self):
        try:
            screenshot.take_screenshot()
            self.master.after(0, self.update_output, "📸 Screenshot saved successfully!")
            self.master.after(0, voice_assistant.speak, "Screenshot saved successfully.")
        except Exception as e:
            self.master.after(0, self.update_output, f"❌ Error taking screenshot: {e}")
            self.master.after(0, voice_assistant.speak, f"Error taking screenshot: {e}")

    def gui_list_running_processes(self):
        self.update_output("📋 Listing running processes...")
        threading.Thread(target=self._list_running_processes_task, daemon=True).start()

    def _list_running_processes_task(self):
        old_stdout = sys.stdout
        sys.stdout = TextRedirector(self.output_text, self.master)
        try:
            process_monitor.list_running_processes()
        finally:
            sys.stdout = old_stdout
        self.master.after(0, voice_assistant.speak, "Running processes listed.")

    def gui_open_task_manager(self):
        self.update_output("📊 Opening Task Manager...")
        threading.Thread(target=self._open_task_manager_task, daemon=True).start()

    def _open_task_manager_task(self):
        try:
            task_manager.open_task_manager()
            self.master.after(0, self.update_output, "Task Manager opened successfully.")
            self.master.after(0, voice_assistant.speak, "Task Manager opened.")
        except Exception as e:
            self.master.after(0, self.update_output, f"❌ Error opening Task Manager: {e}")
            self.master.after(0, voice_assistant.speak, f"Error opening Task Manager: {e}")

    def gui_shutdown(self):
        if messagebox.askyesno("Shutdown Confirmation", "Are you sure you want to shut down your system?"):
            self.update_output("🔴 Initiating system shutdown...")
            threading.Thread(target=self._shutdown_task, daemon=True).start()

    def _shutdown_task(self):
        system_control.shutdown()
        self.master.after(0, voice_assistant.speak, "Shutting down.")

    def gui_scan_ports(self):
        target_ip = self.target_ip_entry.get().strip()
        if not target_ip:
            messagebox.showwarning("Input Error", "Please enter a target IP address.")
            return
        self.update_output(f"🔍 Scanning open ports on {target_ip}...")
        threading.Thread(target=self._scan_ports_task, args=(target_ip,), daemon=True).start()

    def _scan_ports_task(self, target_ip):
        old_stdout = sys.stdout
        sys.stdout = TextRedirector(self.output_text, self.master)
        try:
            port_scanner.scan_ports(target_ip)
        finally:
            sys.stdout = old_stdout
        self.master.after(0, voice_assistant.speak, f"Port scanning on {target_ip} completed.")

    def gui_get_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return
        self.update_output(f"☁ Fetching weather for {city}...")
        threading.Thread(target=self._get_weather_task, args=(city,), daemon=True).start()

    def _get_weather_task(self, city):
        weather_report = weather_news.get_weather(city)
        self.master.after(0, self.update_output, weather_report)
        self.master.after(0, voice_assistant.speak, weather_report)

# Helper class to redirect print statements to the Tkinter Text widget
class TextRedirector:
    def __init__(self, widget, master):
        self.widget = widget
        self.master = master

    def write(self, text):
        self.master.after(0, lambda: self.widget.config(state=tk.NORMAL))
        self.master.after(0, lambda: self.widget.insert(tk.END, text))
        self.master.after(0, lambda: self.widget.see(tk.END)) # Auto-scroll
        self.master.after(0, lambda: self.widget.config(state=tk.DISABLED))

    def flush(self):
        pass # Required for file-like objects

if __name__ == "__main__":
    root = tk.Tk()
    gui = NetVoiceAssistantGUI(root)
    root.mainloop()