import requests
from bs4 import BeautifulSoup
import smtplib
originmail = 'origin@gmail.com'
password = 'password'
targetmail = 'target@domain.com'

URL = 'https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_3?keywords=sony+a7&qid-1561393494&s=gateway&sr-8-3'

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                        'AppleWebKit/537.36 (KHTML, like Gecko)'
                        'Chrome/89.0.4389.105 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=header)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    # print(converted_price)
    # print(title.strip())

    if(converted_price < 1.800):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(originmail, password)

    subject = 'PRICE FELL DOWN'
    body = f"Check the amazon link\n {URL}"

    message = "Subject:" + subject + " \n\n" + body

    server.sendmail(
        originmail,
        targetmail,
        message
    )

    print('HEY EMAIL HAS BEEN SEND')

    server.quit()


check_price()
