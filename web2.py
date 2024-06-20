# web2.py 
#웹서버와 통신
import requests 
#크롤링
from bs4 import BeautifulSoup


url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#파일로 저장(append, read, write) a+, wt 
f = open("daangn.txt", "wt", encoding="utf-8")
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts: 
    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    addrElem = post.find("div", attrs={"class":"card-region-name"})
    title = titleElem.text.strip()
    price = priceElem.text.strip()
    addr = addrElem.text.strip() 
    #파이썬 3.6 f-string문법 
    print(f"{title}, {price}, {addr}")
    f.write(f"{title}, {price}, {addr}\n")

f.close() 
