from ..extract.fetch_weather import fetch_weather_city
from ..transformation.transform_weather import transform_weather_info
from ..load.save_as_json import save_raw_weather

CITIES =[{
    "name": "London",
    "lat": 51.5073219,
    "lon":0.1276474
}]

def run():
    transformed_data = []

    for city in CITIES:
        raw = fetch_weather_city(city)
        clean = transform_weather_info(raw)
        transformed_data.append(clean)

    print(transformed_data)
    save_raw_weather(transformed_data, "London")

if __name__ == "__main__":
    run()