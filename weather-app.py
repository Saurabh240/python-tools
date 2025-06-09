# Fetches current weather using an API like OpenWeatherMap.

import requests

city = "London"
api_key = "your_api_key"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
data = requests.get(url).json()
print(f"{city}: {data['main']['temp']}°C, {data['weather'][0]['description']}")
