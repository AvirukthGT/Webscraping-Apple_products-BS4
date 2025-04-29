# Amazon Product Scraper (Practice Project)

This is a simple Python project using **BeautifulSoup** and **requests** to scrape product details from an [Amazon Australia](https://www.amazon.com.au) product page. The script extracts key information such as:

- Product Title  
- Price  
- Availability  
- Customer Rating  
- Bullet Points (short descriptions)  
- Customer Reviews  

## Purpose

This was a **practice project** to get hands-on experience with:
- HTML parsing using `BeautifulSoup`
- Sending HTTP requests using `requests`
- Handling encoding issues
- Writing scraped data to CSV using Python's `csv` module

## Technologies Used

- Python 3.11  
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- `requests` library  
- CSV writing

## How It Works

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com.au/..."
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

# Extract title, price, etc.
product_title = soup.find("span", id="productTitle").text.strip()
# ... more fields

# Save to CSV
with open("amazon_airpods.csv", mode="w", newline="", encoding="utf-8") as file:
    ...

```

*This project is for educational purposes only. Web scraping Amazon violates their Terms of Service. Please do not use this script for commercial or frequent scraping.*
