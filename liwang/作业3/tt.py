import requests
from bs4 import BeautifulSoup

url = 'http://pm25.in/'
content = requests.get(url).content
soup = BeautifulSoup(content,'lxml')

print(soup)
