import requests
from bs4 import BeautifulSoup

URL="https://www.amazon.in/Axabyte-Laptop-DDR3-12800-1600-Memory/dp/B07S6SZK1Z/ref=sr_1_2_sspa?keywords=8gb+ram&qid=1562607258&s=gateway&sr=8-2-spons&psc=1"

headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

page=requests.get(URL,headers=headers)
soup=BeautifulSoup(page.content,"html.parser")

price_tag=soup.find(id="priceblock_ourprice")
price=price_tag.text
price=price[2:-3].replace(",","")
price=float(price)
if(price<1000):
   print("You can buy this alarm start")
