"""
wikipedia_languages.py

Extracts the list of languages from the Wikipedia homepage using requests and lxml.

Author: Joan Balbin
Based on: Web Scraping course by Leonardo Kuffo
"""

import requests
from lxml import html

# Define custom headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
}

# Wikipedia homepage
url = "https://www.wikipedia.org/"

# Send GET request and set encoding
response = requests.get(url, headers=headers)
response.encoding = "utf-8"

# Parse HTML response
tree = html.fromstring(response.text)

# Extract language names from the main page
languages = tree.xpath('//div[contains(@class, "central-featured-lang")]//strong/text()')

# Print each language found
for lang in languages:
    print(lang)


# ⚠️ Fix for urllib3 SSL warning on macOS:
# urllib3 v2 requires OpenSSL 1.1.1+, but macOS uses LibreSSL by default,
# causing a NotOpenSSLWarning. To fix it without reinstalling Python:

# Run these commands in your terminal:
# pip uninstall urllib3
# pip install "urllib3<2.0"

# This forces urllib3 to use version 1.x, which is compatible with LibreSSL.