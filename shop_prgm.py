import lxml
import requests
import csv
from bs4 import BeautifulSoup
webpage = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR11.TRC1.A0.H0.Xsteam+mop.TRS0&_nkw=steam+mop&_sacat=0')
soup = BeautifulSoup(webpage.text, 'lxml')
# for tag in soup.find_all(True):
#     print(tag.name)
#print(soup.prettify())


item_info = soup.find_all('div', class_='s-item__info clearfix')
mop_lst = []
for item in item_info:
    names = item.find('h3').text.strip()
    prices = item.find('span', class_='s-item__price').text.strip()
    #print(names.text.strip(), prices.text.strip())
    mop_lst.append([names, prices])
# names = soup.find_all('h3', class_='s-item__title')
# for name in names:
#     item_name = name.text.strip()

# prices = soup.find_all('span', class_='s-item__price')
# for price in prices:
#     item_price = price.text.strip()

with open('steam_mop.csv', 'w') as output_csv:
    
    fields = ['year', 'name', 'champion']
    output_writer = csv.writer(output_csv)
    for item in mop_lst:
        output_writer.writerow(item)


# page_soup = bs(target, "lxml")
# containers = page_soup.find_all('li')
# for container in containers:
#     item = container.find_all("span", class_= "mp-Listing-seller-name")
#     print(item)


