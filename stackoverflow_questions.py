import requests
from bs4 import BeautifulSoup

# Define custom headers to simulate a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
}

# URL to scrape
url = "https://stackoverflow.com/questions"

# Send GET request
response = requests.get(url, headers=headers)
response.encoding = "utf-8"

# Parse HTML response with BeautifulSoup using lxml parser
soup = BeautifulSoup(response.text, "lxml")

# Select all question containers
question_containers = soup.select("div.s-post-summary")

# Extract and print question titles
for container in question_containers:
    title_element = container.select_one("h3 a")
    if title_element:
        print(title_element.text.strip())