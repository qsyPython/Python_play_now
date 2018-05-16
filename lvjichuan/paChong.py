# 第3期的python作业：
# 做一个简单的网络爬虫demo，
# 爬取一下空气质量指数的网站(http://pm25.in/)的数据，
# 然后处理数据做成如下的图表（x坐标为城市名称，y坐标为对应城市的AQI，
# title为：空气质量最好的50个城市，对应的更新时间为网页的 数据更新时间）

import urllib3
from pyquery import PyQuery as pq
import matplotlib.pyplot as plt
import numpy as np

# http = urllib3.PoolManager()
# r = http.request('GET', 'http://pm25.in/')
# print(r.data)

d=pq(url="http://pm25.in/rank")
p=d('.table').find("tbody")
list=[]
list2=[]
for i in range(50):
    v=p.find("tr").eq(i)
    list.append(v.find("td").eq(1).text())
    list2.append(int(v.find("td").eq(2).text()))
print("打印完成")

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

N = 50
x = np.arange(N)
data = list2
colors = np.random.rand(N * 3).reshape(N, -1)
labels = list

plt.title(u"全国空气质量排名")
plt.bar(x, data, alpha=0.8, color=colors, tick_label=labels)
plt.show()