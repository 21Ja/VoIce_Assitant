import requests
WEATHER_API = "4142082b8bf9f563561a4ce0e6fcf2f2"

def get_weather(city="Delhi"):
    """
    Fetch current weather details for a given city using OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and "main" in data:
            temp = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"].capitalize()
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            return (f"🌍 City: {city}\n"
                    f"🌡 Temperature: {temp}°C\n"
                    f"☁ Weather: {weather_desc}\n"
                    f"💧 Humidity: {humidity}%\n"
                    f"🌬 Wind Speed: {wind_speed} m/s")

        else:
            return f"❌ Error: {data.get('message', 'Unable to fetch weather.')}"

    except requests.exceptions.RequestException as e:
        return f"❌ Network error: {e}"

