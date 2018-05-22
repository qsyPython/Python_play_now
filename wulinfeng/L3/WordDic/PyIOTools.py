# from pylab import *
# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

class PyIOToolClass(object):
    def drawChat(self,xlist = [],ylist = []):
        # mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
        # mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
        # plt.bar(range(len(xlist)), xlist, color='rgb', tick_label=ylist)
        # plt.xticks(range(len(ylist)),rotation=90)
        # # plt.show()
        # plt.xticks(fontsize=10)
        # plt.tight_layout() #显示全
        # plt.savefig("examples.pdf")
        # plt.close()

        mpl.rcParams['font.sans-serif'] = ['FangSong']
        mpl.rcParams['axes.unicode_minus'] = False
        plt.bar(range(len(xlist)), xlist, color='rgb', tick_label=ylist)
        # plt.bar(ylist,xlist)
        plt.xticks(range(len(ylist)), rotation=90,fontsize=7)
        # plt.xticks(fontsize=7)
        plt.yticks(fontsize=15)
        plt.title("全国空气质量柱状图",fontsize = 15)
        plt.tight_layout() #显示全
        plt.savefig("examples.pdf")
        plt.close()
