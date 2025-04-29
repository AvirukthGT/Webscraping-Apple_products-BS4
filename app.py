# This app scrapes product details from a specific Amazon product page

from bs4 import BeautifulSoup
import requests
import csv

# Target Amazon URL
url = 'https://www.amazon.com.au/Apple-AirPods-Generation-MagSafe-USB%E2%80%91C/dp/B0CHXDW3SX/...'

# Required headers to mimic a real browser (avoid bot detection)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

# Send GET request
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    html_content = response.text
    print("Request successful:", response.status_code)
else:
    print("Failed to fetch page:", response.status_code)
    exit()

# Parse the HTML using BeautifulSoup and lxml parser
soup = BeautifulSoup(html_content, 'lxml')

# --- Extract product information ---
try:
    product_title = soup.find("span", id="productTitle").text.strip()
except:
    product_title = "N/A"

try:
    product_price = soup.find("span", class_="a-price-fraction").text.strip()
except:
    product_price = "N/A"

try:
    product_availability = soup.find("div", id="availability").text.strip()
except:
    product_availability = "N/A"

try:
    product_rating = soup.find("span", id="acrPopover").text.strip()
except:
    product_rating = "N/A"

try:
    product_bp = soup.find("ul", class_="a-unordered-list a-vertical a-spacing-mini").text.strip()
except:
    product_bp = "N/A"

try:
    product_review = soup.find("ul", id="cm-cr-dp-review-list").text.strip()
except:
    product_review = "N/A"

# --- Save extracted data to CSV ---
with open('amazon_airpods.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write header row
    writer.writerow(['product_title', 'product_price', 'product_availability', 
                     'product_rating', 'product_bp', 'product_review'])
    
    # Write product details
    writer.writerow([product_title, product_price, product_availability,
                     product_rating, product_bp, product_review])

print("Data exported to 'amazon_airpods.csv'")
