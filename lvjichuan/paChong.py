# 第3期的python作业：
# 做一个简单的网络爬虫demo，
# 爬取一下空气质量指数的网站(http://pm25.in/)的数据，
# 然后处理数据做成如下的图表（x坐标为城市名称，y坐标为对应城市的AQI，
# title为：空气质量最好的50个城市，对应的更新时间为网页的 数据更新时间）

import urllib3
from pyquery import PyQuery as pq


http = urllib3.PoolManager()
r = http.request('GET', 'http://pm25.in/')
print(r.data)

d=pq(url="http://pm25.in/")
print(d('title').text())