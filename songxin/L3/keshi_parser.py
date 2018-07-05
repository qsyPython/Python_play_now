import random
import requests
from songxin.L3.url_manager import UrlManager
from songxin.L3.proxys_list import ProxysList
from songxin.L3.header_list import HeaderList
from bs4 import BeautifulSoup
import time
class KeShiParser(object):
    def keshi_parser(self,url):
        target_header = HeaderList()
        # proxys_list = ProxysList()
        try:
            # request = requests.get(url, proxies={"http": random.choice(proxys_list.get_proxys_list())},
            #                        headers=target_header.header)
            request = requests.get(url, headers=target_header.header)
            request.encoding = request.apparent_encoding  # 设置编码 encoding 返回的是请求头编码  apparent_encoding 是从内容网页中分析出的响应内容编码方式
            request.close()
            # 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
            soup = BeautifulSoup(request.text, 'lxml')
            # 以格式化的形式打印html
            return soup
        except Exception as e:
            print(e)
            time.sleep(1)
