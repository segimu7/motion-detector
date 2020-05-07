import requests
from bs4 import BeautifulSoup

r = requests.get(r"https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone&_sacat=0&_ipg=25")
c = r.content
soup = BeautifulSoup(c,"html.parser")


sub = soup.find_all("div",{"class":"s-item__subtitle"})
    
price = soup.find_all("span",{"class":"s-item__price"})

for i in price:
    print(i.text)
    