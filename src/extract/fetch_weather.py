from .openweather_client import OpenWeatherClient
from ..config.settings import OPENWEATHER_API_KEY

def fetch_weather_city(city):
    client = OpenWeatherClient(api_key=OPENWEATHER_API_KEY)
    weather_info = client.get_current_weather(lat=city.get("lat"), lon=city.get("lon"))
    current = weather_info.get("current", {})
    current["city"] = city["name"]
    return current