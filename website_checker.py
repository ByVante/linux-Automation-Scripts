import requests

# List of websites to check
websites = [
    "https://www.google.com",
    "https://www.amazon.com",
    "https://www.github.com",
    "https://www.thiswebsitedoesnotexist12345.com"
]

for site in websites:
    try:
        response = requests.get(site, timeout=5)
        if response.status_code == 200:
            print(f"✅ {site} is UP")
        else:
            print(f"⚠️ {site} returned status {response.status_code}")
    except requests.RequestException:
        print(f"❌ {site} is DOWN or unreachable")
