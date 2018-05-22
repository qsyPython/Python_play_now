#coding:utf-8
# import matplotlib
# matplotlib.use('qt4agg')
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

from cuiyiran.L3.Parser import Parser

#定义自定义字体，文件名从1.b查看系统中文字体中来
# myfont = FontProperties(fname='/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc')
# #解决负号'-'显示为方块的问题
# matplotlib.rcParams['axes.unicode_minus']=False
# # plt.plot([-1,2,-5,3])



p = Parser()

X = p.cities
Y = p.aqis
fig = plt.figure()
plt.bar(X, Y, 0.4, color="green")

plt.title("空气质量最好的50个城市(当前时间：" + p.getTime() + ")")

plt.show()
plt.savefig("barChart.jpg")


