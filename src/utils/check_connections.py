import os
import requests
from dotenv import load_dotenv

load_dotenv()

LAT = os.getenv("CITY_LAT")
LON = os.getenv("CITY_LON")


def test_openweather():
    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"lat": LAT, "lon": LON, "units": "metric",
                "appid": os.getenv("OPENWEATHER_API_KEY")},
        timeout=15,
    )
    print("OpenWeather:", r.status_code, r.json().get("main"))


def test_aqicn():
    r = requests.get(
        f"https://api.waqi.info/feed/geo:{LAT};{LON}/",
        params={"token": os.getenv("AQICN_API_KEY")},
        timeout=15,
    )
    data = r.json()
    print("AQICN:", r.status_code, data.get("status"), data.get("data", {}).get("aqi"))


def test_open_meteo_weather_history():
    r = requests.get(
        "https://archive-api.open-meteo.com/v1/archive",
        params={"latitude": LAT, "longitude": LON,
                "start_date": "2026-11-01", "end_date": "2026-11-02",
                "hourly": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m,wind_direction_10m"},
        timeout=15,
    )
    print("Open-Meteo weather history:", r.status_code, list(r.json().get("hourly", {}).keys()))


def test_open_meteo_air_quality():
    r = requests.get(
        "https://air-quality-api.open-meteo.com/v1/air-quality",
        params={"latitude": LAT, "longitude": LON, "past_days": 3,
                "hourly": "pm2_5,pm10,us_aqi,uv_index"},
        timeout=15,
    )
    print("Open-Meteo air quality:", r.status_code, list(r.json().get("hourly", {}).keys()))


def test_groq():
    from groq import Groq
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    out = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": "Say OK"}],
    )
    print("Groq:", out.choices[0].message.content)


for test in [test_openweather, test_aqicn, test_open_meteo_weather_history,
             test_open_meteo_air_quality, test_groq]:
    try:
        test()
    except Exception as e:
        print(f"{test.__name__} FAILED:", e)