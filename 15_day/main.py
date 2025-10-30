# Day 15 - CryptoPulse: Live Cryptocurrency Tracker
# Project: Fetch and display live cryptocurrency prices using the CoinGecko API.

import requests
import datetime
import json
import time

LOG_FILE = "crypto_log.json"

def slow_print(text, delay=0.03):
    """Smooth printing animation."""
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def get_crypto_data(coin_ids):
    """Fetch live crypto data from CoinGecko API."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coin_ids)}&vs_currencies=usd,chf,eur,inr&include_market_cap=true&include_24hr_change=true"
    try:
        response = requests.get(url, timeout=8)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        print("❌ Failed to fetch live data. Check your internet connection.")
        return None

def display_data(data):
    """Display formatted crypto data."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n" + "=" * 65)
    print(f"💹 CRYPTOPULSE – LIVE CRYPTO DASHBOARD ({now})")
    print("=" * 65)
    print(f"{'Coin':<15}{'USD($)':<12}{'CHF(₣)':<12}{'24h Change(%)':<15}{'Market Cap(USD)'}")
    print("-" * 65)

    for coin, info in data.items():
        usd = info["usd"]
        chf = info["chf"]
        change = info.get("usd_24h_change", 0)
        mcap = info.get("usd_market_cap", 0)
        change_icon = "📈" if change > 0 else "📉"
        print(f"{coin.capitalize():<15}{usd:<12.2f}{chf:<12.2f}{change_icon} {change:<13.2f}{mcap:,.0f}")
    print("=" * 65)

def log_data(data):
    """Save snapshot to a JSON log."""
    entry = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data": data
    }
    try:
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)
        except FileNotFoundError:
            logs = []

        logs.append(entry)
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=4)
        print("💾 Snapshot saved to crypto_log.json\n")
    except Exception as e:
        print(f"⚠️ Error saving log: {e}")

def show_recent_logs():
    """Show last 3 log entries."""
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)
            print("\n📘 Recent Snapshots:")
            print("-" * 65)
            for entry in logs[-3:]:
                print(f"{entry['timestamp']} – {', '.join(entry['data'].keys())}")
            print("-" * 65)
    except FileNotFoundError:
        print("\n⚠️ No previous logs found.")

def main():
    print("=" * 65)
    print("💰 CRYPTOPULSE – REAL-TIME CRYPTOCURRENCY TRACKER 💰")
    print("=" * 65)
    print("Available Coins: bitcoin, ethereum, solana, dogecoin, cardano, litecoin\n")

    user_input = input("Enter coins to track (comma-separated): ").strip()
    coin_ids = [c.strip().lower() for c in user_input.split(",") if c.strip()]
    if not coin_ids:
        print("⚠️ No coins entered. Exiting.")
        return

    slow_print("\nFetching data from CoinGecko...\n", 0.02)
    data = get_crypto_data(coin_ids)
    if not data:
        return

    display_data(data)
    log_data(data)
    show_recent_logs()
    print("✅ Data fetched successfully! Stay informed with CryptoPulse.\n")

if __name__ == "__main__":
    main()
