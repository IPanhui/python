from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/page1.html"
html = urlopen(url)
bsObj = BeautifulSoup(html.read())
h1 = bsObj.html.body.h1
print(h1)

