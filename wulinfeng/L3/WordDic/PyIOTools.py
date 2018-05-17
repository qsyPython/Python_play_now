from pylab import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
class PyIOToolClass(object):
    def drawChat(self,xlist = [],ylist = []):
        mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
        mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
        plt.bar(range(len(xlist)), xlist, color='rgb', tick_label=ylist)
        plt.xticks(range(len(ylist)),rotation=90)
        # plt.show()
        plt.figaspect(10)
        plt.figure(figsize=(10,5))
        plt.xticks()
        plt.tight_layout() #显示全
        plt.savefig("examples.pdf")
        plt.close()


