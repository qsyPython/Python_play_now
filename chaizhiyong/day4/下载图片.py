from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pythonscraping.com")
bs = BeautifulSoup(r.text,'html.parser')
image = bs.find("a", {"id": "logo"}).find("img")["src"]
#urlretrieve(image, "logo.jpg")

ir = requests.get(image, stream=True)
if ir.status_code == 200:
    with open('logo.jpg', 'wb') as f:
        for chunk in ir:
            f.write(chunk)

