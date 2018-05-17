# 第3期的python作业：
# 做一个简单的网络爬虫demo，爬取一下空气质量指数的网站(http://pm25.in/)的数据
# 然后处理数据做成如下的图表（x坐标为城市名称，y坐标为对应城市的AQI，
# title为：空气质量最好的50个城市，对应的更新时间为网页的 数据更新时间）

import requests
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup

r = requests.get('http://pm25.in/rank')

s = BeautifulSoup(r.text,'html.parser')

c = s.select('.table-striped a')

tr = s.select('.table-striped tbody tr ')

#获取tdlist
td = []

#城市名字列表
cityList = []

for i in range(50):

    h = tr[i].select('td:nth-of-type(3)')

    td.append(h[0].text)

    cityList.append(c[i].text)

print(cityList)

print(td)

plt.rcParams['font.sans-serif']=['SimHei']

plt.rcParams['axes.unicode_minus']=False

v = np.arange(50)

colors = np.random.rand(7 * 3).reshape(7, -1)

plt.title("全国空气质量排名")

plt.xlabel('X坐标')

plt.ylabel('Y坐标')

plt.xticks(fontsize = 5)

plt.xticks(range(len(cityList)),rotation = 90)

plt.bar(v,td,alpha = 0.8, color = colors,tick_label = cityList)

plt.show()

plt.savefig('lhw.png')
