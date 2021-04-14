import requests
import smtplib
from bs4 import BeautifulSoup
import time
print("Enter the no of items in the list: ")
url_list=list()
price_list=list()
n=int(input())
n1=n
while n>0:
    print("enter the url and the price")
    url,price=input().split()
    price=float(price)
    url_list.append(url)
    price_list.append(price)
    n=n-1

def send_mail(url):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('@gmail.com','')
    subject='Price fell down!'
    body='Check your product!'
    message=f"Subject:{subject}\n\n{body}\n{url}"
    server.sendmail("@gmail.com","@gmail.com",message)
    print("mail sent!!")
    server.quit()
while True:
    for i in range(n1):
        url=url_list[i]
        price_old=price_list[i]
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        }
        page=requests.get(url,headers=headers)
        soup=BeautifulSoup(page.content,"html.parser")
        title=(soup.find(id="productTitle").get_text()).strip()
        price=soup.find(id="priceblock_ourprice").get_text()
        #print(price_new)
        price_new=""
        for alpha in price:
            if alpha.isnumeric() or alpha==".":
                price_new=price_new+alpha
        price_new=float(price_new)
        if price_old-price_new>50:
            send_mail(url)
        else:
            print('no')
    time.sleep(60)
