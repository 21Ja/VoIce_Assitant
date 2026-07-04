import webbrowser

def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    print(f"🔎 Searching: {query}")
    webbrowser.open(url)
