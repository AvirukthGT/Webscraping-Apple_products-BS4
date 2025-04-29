from bs4 import BeautifulSoup
import requests
import csv

html_path='apple_store.html'

with open(html_path,'r',encoding='utf-8') as html_file:
    html_content=html_file.read()

soup=BeautifulSoup(html_content,'html.parser')

header=soup.find('h1').text.strip()

menus=soup.find_all('a')

for menu in menus:
    print(menu.text)
print(menus)

product_divs=soup.find_all('div',class_='product')
product_parsed={}
product_details={}

for product in product_divs:
    soup=BeautifulSoup(str(product),'html.parser')
    title = soup.find('h3').text
    price = soup.find_all('p')[0].text.replace('Price: ', '')
    quantity = soup.find_all('p')[1].text.replace('Quantity Available: ', '')
    rating = soup.find('p', class_='rating').text
    shipping = soup.find_all('p')[3].text.replace('Estimated Shipping: ', '')
    product_details={
        'Title':title,
        'Price':price,
        'Quantity':quantity,
        'Rating':rating,
        'Shipping':shipping
    }

    product_parsed[title]=product_details

print(product_parsed)


with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(['Title', 'Price', 'Quantity', 'Rating', 'Shipping'])
    
    # Write each product's data
    for product in product_parsed.values():
        writer.writerow([
            product['Title'],
            product['Price'],
            product['Quantity'],
            product['Rating'],
            product['Shipping']
        ])


