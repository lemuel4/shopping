import lxml
import requests
import csv
from bs4 import BeautifulSoup
webpage = requests.get('https://www.google.com/shopping/product/14866225283657880226/online?q=steam+mop&biw=885&bih=697&gbv=1&prds=paur:ClkAsKraXxp5A6lfmur-ttdXnkTSa5zY50KTbsDWpgymS9R0jVEbjkISWlfTFx1i7g2mX2JC0rXtchoYuFFTg_B9DUNPOChWz_gpar1VYuRJrgCrZJio9o2u7hIZAFPVH73VchchuZQ1Sa2YHFjnklYAEuiwrQ&sa=X&ved=0ahUKEwj_xtDg9K_kAhUlc98KHdcNANYQ6SQIMA')
soup = BeautifulSoup(webpage.text, 'lxml')

# item = soup.find('div', class_='MCpGKc')
# name = item.find('h3', class_='r').find('a').text
# price = soup.find('div', class_='pslires').find('div', class_='A8OWCb').text


product = soup.find('div', id='product-basic-info').find('h1').text.strip()
product_table = soup.find('table', class_='os-main-table')
product_info = product_table.find_all('tr')
for row in product_info:
    row = row[1:]
    product_name = row.find('td', class_='os-seller-name')
    print(product_name.text)

    # with open('steam_mop.csv', 'a') as output_csv:    
    #     output_writer = csv.writer(output_csv)
    #     output_writer.writerow(product_info_text)
