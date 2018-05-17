#列表解析
import re

# squares = [value**2 for value in range(1,11)]
# print(squares)
#
# rnum = random.randint(1, nmax)

# pattern = re.compile(^[1-9]|)
# match = pattern.match('hello,world!')
# if match:
#     # 使用Match获得分组信息
#     print(match.group(['hello',"world"]))






import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

X = [0, 1, 2, 3, 4, 5]
Y = [222, 42, 455, 664, 454, 334]
fig = plt.figure()
plt.bar(X, Y, 0.4, color="green")

plt.title("空气质量最好的50个城市(当前时间：" +  + ")")

plt.show()
plt.savefig("barChart.jpg")