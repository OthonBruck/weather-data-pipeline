from .openweather_client import OpenWeatherClient
from ..config.settings import OPENWEATHER_API_KEY

def fetch_weather_city(country):
    client = OpenWeatherClient(api_key=OPENWEATHER_API_KEY)
    weather_info = client.get_current_weather(lat=country.get("lat"), lon=country.get("lon"))
    return weather_info.get("current", {})