import pyjokes

def tell_joke():
    joke = pyjokes.get_joke()
    print(f"😂 {joke}")
    return joke  # ✅ Now the function returns the joke text
