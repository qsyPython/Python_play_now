# -*- coding: utf-8 -*-
# 第3期的python作业：
# 做一个简单的网络爬虫demo，
# 爬取一下空气质量指数的网站(http://pm25.in/)的数据，
# 然后处理数据做成如下的图表（x坐标为城市名称，y坐标为对应城市的AQI，title为：空气质量最好的50个城市，
# 对应的更新时间为网页的 数据更新时间）
from pyquery import PyQuery as pq
import matplotlib.pyplot as plt

d = pq("http://pm25.in/rank",encoding="utf-8")
t = d(".time").text()
print(t)
f = d(".table").find("tbody")
city_list = []
aoi_list = []
for i in range(50):
    city_list.append(f.find("tr").eq(i).find("td").eq(1).text())
    aoi_list.append(f.find("tr").eq(i).find("td").eq(2).text())

plt.bar(range(50),aoi_list,color='y',tick_label = city_list)
plt.show()