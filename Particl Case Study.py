# Particl Case Study
# by Boston McClary

import requests
from bs4 import BeautifulSoup
import json
import csv

URL = "https://us.shop.gymshark.com/products/gymshark-crest-sweatshirt-persimmon-red-ss23"
response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

# Get the product title
title = soup.find('h1', class_='product-information_title__Wx52B').get_text()

# Get the product description
description = soup.find('div', class_='accordion_accordion-content__qZ83F', attrs={"data-locator-id": "pdp-accordionContent-DESCRIPTION-read"}).get_text().replace('\n', ' ')

# Get the product price
price = soup.find('span', class_='product-information_price__6g6xM', attrs={"data-locator-id": "pdp-totalValue-read"}).get_text()

# Get the available sizes
sizes_div = soup.find('div', class_='add-to-cart_sizes__qtfGR')
sizes = [button.get_text() for button in sizes_div.find_all('button', class_='size_size__zRXlq')]

# Uncomment this section to save the scraped data to a CSV file
# with open('product_data.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Product Title', 'Product Description', 'Price', 'Available Sizes'])
#     writer.writerow([title, description, price, ', '.join(sizes)])
# print("Data saved to product_data.csv")

# Uncomment this section to save the scraped data to a JSON file
data = {
    'Product Title': title,
    'Product Description': description,
    'Price': price,
    'Available Sizes': sizes
}

with open('product_data.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

print(data)