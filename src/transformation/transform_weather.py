def transform_weather_info(weather_info):
    transformed_info = {
        "city": weather_info.get("name"),
        "temperature": weather_info.get("temp"),
        "humidity": weather_info.get("humidity"),
        "weather_description": weather_info.get("weather")[0].get("description"),
        "timestamp": weather_info.get("dt")
    }
    return transformed_info