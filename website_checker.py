import requests
from datetime import datetime
import time

def check_website(url, retries=3, delay=2):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return f"✅ {url} is UP (attempt {attempt})"
            else:
                return f"⚠️ {url} returned status {response.status_code} (attempt {attempt})"
        except requests.exceptions.RequestException:
            if attempt < retries:
                time.sleep(delay)  # wait before retry
            else:
                return f"❌ {url} is DOWN after {retries} attempts"

# Read websites from file
with open("websites.txt", "r") as file:
    websites = [line.strip() for line in file if line.strip()]

# Open a log file in append mode
with open("website_checker.log", "a") as log:
    for site in websites:
        result = check_website(site)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {result}"
        print(log_entry)
        log.write(log_entry + "\n")
