# API Findings (Day 1)

City: Islamabad (33.6844, 73.0479)

## Connection tests (all run on 2026-11-20)

| Source | Result | Notes |
|---|---|---|
| OpenWeather current weather | 200 OK | temp, humidity, pressure |
| AQICN (live) | 200 OK | AQI 44 at test time |
| Open-Meteo weather archive | 200 OK | temperature_2m, relative_humidity_2m, precipitation, wind_speed_10m, wind_direction_10m (hourly) |
| Open-Meteo air quality | 200 OK | pm2_5, pm10, us_aqi, uv_index (hourly, past_days works) |
| Groq | OK | model: openai/gpt-oss-20b |
| Hopsworks | not tested yet | account/key pending |

## Variable sources

| Variable | Live source | Historical source | Status |
|---|---|---|---|
| Temperature | OpenWeather | Open-Meteo archive | tested |
| Humidity | OpenWeather | Open-Meteo archive | tested |
| Rain (mm) | OpenWeather | Open-Meteo archive (precipitation) | historical tested |
| Rain probability | OpenWeather forecast (pop), to verify | none: use binary "rained in next 24h" target | to verify |
| UV Index | to verify | Open-Meteo air quality (uv_index) | historical tested |
| Wind speed/direction | OpenWeather | Open-Meteo archive | historical tested |
| AQI | AQICN | Open-Meteo air quality (us_aqi) | tested |
| Pollutants (PM2.5, PM10) | AQICN | Open-Meteo air quality | tested |

## To check in Day 2
- Does OpenWeather free plan give hourly history? (assumed no, Open-Meteo is the backup)
- Which OpenWeather endpoint gives rain probability and UV on the free plan?
- API rate limits (calls/day)
- Whether AQICN station near Islamabad is stable

## Decisions
- Forecast target: t+24 point forecast (to confirm)
- Rain probability target: binary (rain in next 24h) + classifier