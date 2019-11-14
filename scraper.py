import requests 
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4R8QGM/ref=sr_1_4?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+a7iii&qid=1573749047&sr=8-4'
headers = {
    "User Agent": 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)


    soup = BeautifulSoup(page.content, 'html.parser')


    title = soup.find(id ="productTitle").get_text()
    price =soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price > 1.700):
        send_mail()

# print(converted_price)
# print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('zafin.hassan@gmail.com', 'bqkicdbbwqzpmjyv')

    subject ='Price fell down!'
    body = 'Check the amazon link https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4R8QGM/ref=sr_1_4?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+a7iii&qid=1573749047&sr=8-4'

    msg  = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'zafin.hassan@gmail.com',

        'mz2hassa@edu.uwaterloo.ca',
        msg
    )

    print('HEY, EMAIL HAS BEEN SENT!')


    server.quit()

while(True):
    check_price()
    time.sleep(60*60)

