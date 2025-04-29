#this app scrapes data from amazon


from bs4 import BeautifulSoup
import requests
import csv


url='https://www.amazon.com.au/Apple-AirPods-Generation-MagSafe-USB%E2%80%91C/dp/B0CHXDW3SX/ref=sr_1_5?crid=F9QH8GK8ZFN4&dib=eyJ2IjoiMSJ9.k1UsxOjMUF1v5GnqGAkeLX6fg66zhI9PHBxAK4pDBnCzyDRjMoqz_nxl4BJ27KTNc4ECW8wLtojNvJlEjQaRfEf1C6A9JPrFQUDli9e2yV4j_PXDSO2PWhbjlZimMT5C2VF73vPxFlE99gneAO1fZ6oz36Ak6wm89ObeyljUiKmxFzge438l6Wlokl2UzWWvdDeTugov4C69CE1uBB39AmW875gzS8vdSg27c7I5L7JsVUSjQYBKf1KU3qPbNk5ps2Al6vgwNxKcKUBQZWFxcLEDROtu_zxMCN-_ynj7uQU.YOKlkRNa_X9k__qo2j7Ch-JbhV485vOa5VPfMkjO5uo&dib_tag=se&keywords=airpods&qid=1745910666&sprefix=aairpods+%2Caps%2C395&sr=8-5'

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

response=requests.get(url,headers=headers)

if response.status_code==200:
    print(response.status_code)
    html_content=response.text
else:
    print("Fetching error:",response.status_code)


soup=BeautifulSoup(html_content,'lxml')

# print(soup.prettify())

product_title= soup.find("span",id="productTitle").text.strip()

product_price=soup.find("span",class_="a-price-fraction").text.strip()

product_availability=soup.find("div",id="availability").text.strip()

product_rating=soup.find("span",id="acrPopover").text.strip()

product_bp=soup.find("ul",class_="a-unordered-list a-vertical a-spacing-mini").text.strip()

product_review=soup.find("ul",id="cm-cr-dp-review-list").text.strip()



#Saving the file
with open('amazon_airpods.csv',mode='w',newline='',encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerow(['product_title','product_price','product_availability','product_rating','product_bp','product_review'])
    writer.writerow([product_title,product_price,product_availability,product_rating,product_bp,product_review])

print("Data Exported")




