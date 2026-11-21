import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

LAT = os.getenv("CITY_LAT")
LON = os.getenv("CITY_LON")
API_KEY = os.getenv("OPENWEATHER_API_KEY")
RAW_DIR = Path("data/raw/openweather")


def fetch_with_retry(url, params, retries=3, wait=5):
    """Call an API with timeout and simple retry."""
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(url, params=params, timeout=15)
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            print(f"Attempt {attempt}/{retries} failed: {e}")
            if attempt == retries:
                raise
            time.sleep(wait)


def fetch_current_weather():
    return fetch_with_retry(
        "https://api.openweathermap.org/data/2.5/weather",
        {"lat": LAT, "lon": LON, "units": "metric", "appid": API_KEY},
    )


def save_raw(data):
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    path = RAW_DIR / f"current_{stamp}.json"
    path.write_text(json.dumps(data, indent=2))
    return path


def extract_record(data):
    """Pick only the fields we need from the raw response."""
    return {
        "timestamp_utc": datetime.fromtimestamp(data["dt"], tz=timezone.utc).isoformat(),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "wind_direction": data["wind"].get("deg"),
        "rain_1h_mm": data.get("rain", {}).get("1h", 0.0),
    }


if __name__ == "__main__":
    raw = fetch_current_weather()
    print("Saved raw:", save_raw(raw))
    print(extract_record(raw))