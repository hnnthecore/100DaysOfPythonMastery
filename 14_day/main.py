# Day 14 - DataPulse: Live Weather & Stats Dashboard
# Project: Fetch and display live weather data using Open-Meteo API.

import requests
import time
import datetime
import json

LOG_FILE = "weather_log.json"

def slow_print(text, delay=0.03):
    """Print text with typing animation."""
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def get_weather(city):
    """Fetch weather data from Open-Meteo API for the given city."""
    city = city.strip().capitalize()

    # Simple dictionary for a few popular locations (you can expand)
    city_coords = {
        "zurich": (47.3769, 8.5417),
        "geneva": (46.2044, 6.1432),
        "bern": (46.9480, 7.4474),
        "basel": (47.5596, 7.5886),
        "lausanne": (46.5197, 6.6323),
        "london": (51.5072, -0.1276),
        "new york": (40.7128, -74.0060),
        "tokyo": (35.6895, 139.6917)
    }

    if city.lower() not in city_coords:
        print("⚠️ City not found in database. Try Zurich, Geneva, Bern, etc.")
        return None

    lat, lon = city_coords[city.lower()]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["current_weather"]
    except requests.exceptions.RequestException:
        print("❌ Network error! Please check your internet connection.")
        return None

def display_weather(city, weather):
    """Display weather details in a neat format."""
    temp = weather["temperature"]
    wind = weather["windspeed"]
    code = weather["weathercode"]

    # Map weather codes to emojis (simplified)
    codes = {
        0: "☀️ Clear sky",
        1: "🌤️ Mostly clear",
        2: "⛅ Partly cloudy",
        3: "☁️ Overcast",
        45: "🌫️ Fog",
        51: "🌦️ Light rain",
        61: "🌧️ Rain",
        71: "🌨️ Snow",
        95: "⛈️ Thunderstorm"
    }

    condition = codes.get(code, "🌍 Unknown condition")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n" + "=" * 50)
    print(f"🌤️  LIVE WEATHER REPORT - {city.upper()}  🌤️")
    print("=" * 50)
    print(f"🕒 Time: {now}")
    print(f"🌡️ Temperature: {temp}°C")
    print(f"💨 Wind Speed: {wind} km/h")
    print(f"☁️ Condition: {condition}")
    print("=" * 50)
    print("📊 Data provided by Open-Meteo (Free API)\n")

def log_weather(city, weather):
    """Save weather data with timestamp in JSON file."""
    entry = {
        "city": city.capitalize(),
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"],
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        # Load existing data
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)
        except FileNotFoundError:
            logs = []

        logs.append(entry)

        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=4)

        print("💾 Weather data saved to weather_log.json\n")
    except Exception as e:
        print(f"⚠️ Error saving data: {e}")

def show_recent_logs():
    """Display the last 5 weather logs."""
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)
            print("\n📘 Recent Weather Logs:")
            print("-" * 50)
            for entry in logs[-5:]:
                print(f"{entry['timestamp']} - {entry['city']}: {entry['temperature']}°C, {entry['windspeed']} km/h")
            print("-" * 50)
    except FileNotFoundError:
        print("\n⚠️ No previous logs found.")
    except Exception:
        print("\n⚠️ Could not read log file.")

def main():
    print("=" * 50)
    print("🌍 DATAPULSE – LIVE WEATHER & STATS DASHBOARD 🌍")
    print("=" * 50)

    city = input("Enter city name (e.g., Zurich, Geneva, Tokyo): ").strip()
    if not city:
        print("⚠️ No city entered. Exiting.")
        return

    slow_print("\nFetching live data from Open-Meteo servers...\n", 0.02)
    time.sleep(1)

    weather = get_weather(city)
    if weather:
        display_weather(city, weather)
        log_weather(city, weather)
        show_recent_logs()
    else:
        print("❌ Unable to fetch weather data.\n")

    print("🌦️ Thank you for using DataPulse!")

if __name__ == "__main__":
    main()
