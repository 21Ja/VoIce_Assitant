import pywhatkit

def send_message():
    number = input("Enter phone number (without +91): ")
    message = input("Enter message: ")
    pywhatkit.sendwhatmsg_instantly(f"+91{number}", message)
    print("📩 Message Sent!")
