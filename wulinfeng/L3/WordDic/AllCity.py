import requests # 导入requests 库
from bs4 import BeautifulSoup

class AllCityName(object):
      allcityName = []

      def Proxies(self):
          proxies = {
              "http": "http://127.0.0.1:9999",
              "https": "http://127.0.0.1:8888"
          }
          return proxies

#头部header信息
      def headers(self):
          # 模拟成浏览器
          headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                     "Accept-Encoding": "gbk,utf-8,gb2312",
                     "Accept-Language": "zh-CN,zh;q=0.8",
                     "User-Agent": "Mozilla/5.0(iPhone; CPU iPhone OS 11_0 like Mac OS X)  AppleWebKit/537.36(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
                     "Connection": "keep-alive"}

          return headers
# 获取网址内所有城市的信息
      def getCityName(self,url):
          try:
               head = self.headers()
               prox = self.Proxies()
               r = requests.get(url,head)
          except ConnectionError:
              print('网络连接失败')
          except HTTPError as e:
              print('错误码',r.status_code)

          resp = BeautifulSoup(r.text, 'html.parser')
          # print(resp)
          all_li = []
          for tag in resp.find_all('div', class_='all'):
              all_li = tag.findAll('li')
          for li in all_li:
              # cityName = li.find('a').get('href') 取 a 标签中的超链接内容
              value = li.a.get_text() # 取a 标签中文字内容
              self.allcityName.append(value)

          return self.allcityName
