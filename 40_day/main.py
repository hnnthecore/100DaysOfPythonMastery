import requests
from bs4 import BeautifulSoup


LOGIN_URL = "https://quotes.toscrape.com/login"
BASE_URL = "https://quotes.toscrape.com"


def get_csrf_token(session):
    """Fetch login page and extract CSRF token."""
    response = session.get(LOGIN_URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    token = soup.find("input", {"name": "csrf_token"})["value"]
    return token


def login(session, username, password):
    """Login using session + CSRF token."""
    csrf_token = get_csrf_token(session)

    payload = {
        "csrf_token": csrf_token,
        "username": username,
        "password": password
    }

    response = session.post(LOGIN_URL, data=payload)
    response.raise_for_status()

    # Check if login was successful
    return "Logout" in response.text


def scrape_private_quotes(session):
    """Scrape quotes available only after login."""
    response = session.get(BASE_URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    results = []
    for q in quotes:
        text = q.find("span", class_="text").get_text(strip=True)
        author = q.find("small", class_="author").get_text(strip=True)
        results.append({"quote": text, "author": author})

    return results


def main():
    session = requests.Session()

    print("FormBot – Demo Website Login Scraper")
    print("----------------------------------")
    username = input("Enter username: ")
    password = input("Enter password: ")

    print("Logging in...")
    if login(session, username, password):
        print("Login successful.\n")
    else:
        print("Login failed. Check credentials.")
        return

    print("Scraping private quotes...")
    quotes = scrape_private_quotes(session)

    print(f"Found {len(quotes)} quotes.\n")
    for i, q in enumerate(quotes[:10], start=1):
        print(f"{i}. {q['quote']} — {q['author']}")


if __name__ == "__main__":
    main()
