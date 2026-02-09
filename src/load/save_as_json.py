import json
from datetime import datetime
from pathlib import Path

def save_raw_weather(data: dict, city: str) -> None:
    now = datetime.now()

    base_path = Path("data/raw") / \
        f"{now.year}" / \
        f"{now.month:02d}" / \
        f"{now.day:02d}"

    base_path.mkdir(parents=True, exist_ok=True)

    file_name = city.lower().replace(" ", "_") + ".json"
    file_path = base_path / file_name

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)