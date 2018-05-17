from lxml.html import HtmlElement
from pyquery import PyQuery as pq, PyQuery
from requests import request


class Parser:

    #抓取的html
    d = ""

    # 城市名
    cities = []
    # #aqi值
    aqis = []

    def __init__(self):
        # 空气质量最好的50个城市
        self.d = pq(url='http://pm25.in/rank')

        #每个城市的数据所在的tr标签
        elements = self.d('.table').find('tbody').find('tr')

        #获取每个数据的城市和aqi值
        for i in range(0, 50):
            self.cities.append(elements.eq(i).children().eq(1)('a').html())
            self.aqis.append(elements.eq(i).children().eq(2).html())

        #赋值


    def getTime(self):
        return  self.d('.time')('p').html()









