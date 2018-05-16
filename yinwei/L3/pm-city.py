#先爬取所有城市以及对应城市的空气质量指标，然后做一个top50的图表
#http://pm25.in/

import  requests
import re
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False # 处理- 显示问题

r = requests.get('http://pm25.in/rank')
soup = BeautifulSoup(r.text, 'html.parser')

city = soup.select('.table-striped a')
#获取城市姓名
trList = soup.select('.table-striped tbody tr ')
#获取tr列表

index = 0
tdList = []
#获取tdlist
cityNameList = []
#城市名字列表
apiTextList = []
#api指数列表
while(index<50):
    t = trList[index].select('td:nth-of-type(3)')
    tdList.append(t[0].text)
    cityNameList.append(city[index].text)
    index = index+1

print(tdList)

N = 7
x = np.arange(50)
plt.xlabel("city")
plt.ylabel("api")
plt.title("空气质量指标图")
colors = np.random.rand(N * 3).reshape(7, -1)
plt.figure(figsize=(18,6), facecolor="white")
plt.xticks(rotation=90)#设置时间标签显示格式
plt.bar(x,tdList,alpha=0.8, color=colors, tick_label=cityNameList)
plt.savefig('test.png')
plt.show()











