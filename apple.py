from bs4 import BeautifulSoup

import csv

# Path to the local HTML file
html_path = 'apple_store.html'

# Read the HTML file with UTF-8 encoding
with open(html_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract and print the page header (e.g., "Apple Store")
header = soup.find('h1').text.strip()
print(f"Header: {header}")

# Extract and print all menu items (anchor tags)
menus = soup.find_all('a')
print("Menu Items:")
for menu in menus:
    print(menu.text.strip())

# Extract all product divs
product_divs = soup.find_all('div', class_='product')

# Dictionary to store parsed product data
product_parsed = {}

# Loop through each product div and extract its details
for product in product_divs:
    product_soup = BeautifulSoup(str(product), 'html.parser')

    title = product_soup.find('h3').text.strip()
    price = product_soup.find_all('p')[0].text.replace('Price: ', '').strip()
    quantity = product_soup.find_all('p')[1].text.replace('Quantity Available: ', '').strip()
    rating = product_soup.find('p', class_='rating').text.strip()
    shipping = product_soup.find_all('p')[3].text.replace('Estimated Shipping: ', '').strip()

    product_details = {
        'Title': title,
        'Price': price,
        'Quantity': quantity,
        'Rating': rating,
        'Shipping': shipping
    }

    # Use product title as the key
    product_parsed[title] = product_details

# Optional: Print the parsed product data
print("\nParsed Product Data:")
for title, details in product_parsed.items():
    print(f"{title}: {details}")

# Save the parsed product data to a CSV file
with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write CSV header
    writer.writerow(['Title', 'Price', 'Quantity', 'Rating', 'Shipping'])

    # Write product rows
    for product in product_parsed.values():
        writer.writerow([
            product['Title'],
            product['Price'],
            product['Quantity'],
            product['Rating'],
            product['Shipping']
        ])

print("\nData successfully written to 'products.csv'")
