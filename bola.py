import os
import lxml
import requests
import csv
import smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup
from datetime import date

today = date.today()
d1 = today.strftime("%m-%d-%Y")
webpage = requests.get('https://www.amazon.com/FOREO-Facial-Cleansing-Exfoliation-Fuchsia/dp/B018T7DI4A')
soup = BeautifulSoup(webpage.text, 'lxml')
price = soup.find('td', class_='a-span12')
our_price = soup.find('tr', id='priceblock_ourprice_row').span.text
#our_price = '$30.00'

def tracking():
    track_list = []
    with open('/Users/lemuel4/APIs/shopping/bola_tracker.csv') as tracker:
        reader = csv.reader(tracker)
        for row in reader:
            track_list.append(row)
    
    last_price = track_list[-1]
    print(last_price, our_price)
    if our_price < last_price[0]:

        str_output = f'The price changed from {last_price[0]} to {our_price}'

        EMAIL_ADDRESS = os.environ.get('GMAIL')
        EMAIL_PASS = os.environ.get('GMAIL_PASS')

        msg = EmailMessage()
        msg['Subject'] = 'Bolas Price Update'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = 'marifer0203@hotmail.com'
        msg.set_content(str_output)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
            smtp.send_message(msg)
    else:
        pass

tracking()
with open('/Users/lemuel4/APIs/shopping/bola_tracker.csv', 'a') as output_csv:    
    output_writer = csv.writer(output_csv)
    output_writer.writerow([our_price, d1])


        


