from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup

def yunsite():
    'url'
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch, br',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Connection': 'keep-alive',
               'Host': 'pan.baidu.com',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    url = 'https://pan.baidu.com/s/1c0rjnbi'
    html = requests.get(url, headers=headers, allow_redirects=False)
    return html.headers['Location']

print(yunsite())