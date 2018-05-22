# from urllib.request import urlretrieve
#
import requests
# from bs4 import BeautifulSoup
# import ssl
# def yunsite():
#     'url'
#     headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#                'Accept-Encoding': 'gzip, deflate, sdch, br',
#                'Accept-Language': 'zh-CN,zh;q=0.8',
#                'Connection': 'keep-alive',
#                'Host': 'pan.baidu.com',
#                'Upgrade-Insecure-Requests': '1',
#                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
#
#     url = 'https://www.baidu.com'
#     #content = ssl.create_default_context()#忽略安全
#    # html = requests.get(url, headers=headers, verify=True)
#     html = requests.get('https://requestb.in')
#     print(html.text)
#
# print(yunsite())

# from bs4 import BeautifulSoup
#
# url = 'https://inv-veri.chinatax.gov.cn/'
# req = requests.get(url, verify=False)
# req.encoding = 'utf-8'
# soup = BeautifulSoup(req.text, 'lxml')
# print(soup)

import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
req = urllib.request.Request('https://inv-veri.chinatax.gov.cn/')
urllib.request.encoding = 'utf-8'
data = urllib.request.urlopen(req).read()

print(data)

# #判断ssl
# import requests
# import logging
# from requests.packages import urllib3
# #urllib3.disable_warnings() #忽略警告的方式来屏蔽这个警告
# logging.captureWarnings(True) #通过捕获警告到日志的方式忽略警告：
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)



