import requests # 导入requests 库
from bs4 import BeautifulSoup
import urllib.error
import re

class AQICityClass(object):

      def cityAQI(self,url,cityName,header={}):

          try:
              urlName = url + cityName + '.html'
              r = requests.get(urlName, header)
          except urllib.error.URLError as e:
              print("获取空气质量数据请求出错")
          except Exception as e:
              print('获取空气质量数据函数出现异常')

          resp = BeautifulSoup(r.text, 'html.parser')
          all_div = []
          for tag in resp.find_all('div', class_='span12 data'):
              all_div = tag.findAll('div')
          all_divValues = []
          for div in all_div:
              value = div.find('div', class_='value')
              if value != None:
                  title = value.text.strip()  #取第一个<a>的文本数据
                  print(title.replace("\n", ""))
                  return title.replace("\n", "")
                  break