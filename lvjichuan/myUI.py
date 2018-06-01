# 第4期作业：用python实现一个ui页面，如下图。页面中有一个输入框，实现输入城市名称（全拼或者汉字）点击搜索，展示这个城市7天之内的天气情况。
# 包括天气、温度、风向 、污染指数、限号等。在展示列表的最下方可输入邮箱地址 点击发送按钮可将上面获取到的城市天气信息发送到邮箱中。
# Tips： 1、邮箱地址需要验证 2、做好输入内容异常的处理 3、参考网站：http://www.weather.com.cn/

import wx
from pyquery import PyQuery as pq



#爬取页面中全国城市代码
def crawlWeb():
    d=pq(url="https://www.cnblogs.com/oucbl/p/6138963.html")
    p=d('code')
    fo = open("citycode.txt", "a+", encoding='utf-8')
    for i in range(2,p.length):
        v=p.eq(i)
        fo.write(v.text() + "\n")
    fo.close()
    print("爬取完成")

# 整理城市代码
# 忽略掉文件中除utf8之外的文件编码
# 将文件中多余城市去除
def sortCode():
    file = open("citycode.txt",encoding='utf-8',errors='ignore')
    nfile = open("citycode_sort.txt", "a+", encoding='utf-8')
    #按行读取
    lines = file.readlines()
    for num in range(len(lines)):
        list = lines[num].split()
        olist = []
        #丢弃相邻字城市名中前一个城市名称
        for index in range(len(list)):
            if(list[index].isdigit()):
                olist.append(list[index])
            if(list[index].isdigit()==False):
                if(list[index -1].isdigit() == False):
                    olist.pop(int(len(olist)-1))
                    olist.append(list[index])
                else:
                    olist.append(list[index])
        nfile.write(" ".join(olist) + "\n")
    file.close()
    nfile.close()

#搜索城市代码
def searchCity(str):
    sfile = open("citycode_sort.txt",encoding='utf-8',errors='ignore')
    lines = sfile.readlines()
    for index in range(len(lines)):
        list = lines[index].split()
        for num in range(len(list)):
            if(list[num]==str):
                return(list[num+1])
                break
    sfile.close()

#根据代码抓取页面
def crawlPage(citycode):
    d = pq(url="http://www.weather.com.cn/weather/"+citycode+".shtml",encoding="utf-8")
    p=d('ul.t').find("li")
    alist=[]
    for i in range(7):
        v = p.eq(i)
        olist=[]
        olist.append(v.find("h1").text())
        olist.append(v.find("p.wea").text())
        olist.append(v.find("p.tem").text())
        alist.append(olist)
    print("打印完成")
    print(alist)
    return alist;


#点击动作
def onClicked(self):
    print("hello")
    clist=crawlPage("101010100")
    str=""
    for i in range(7):
        str+=",".join(clist[i])+"\n"
    label.SetLabel(str)

# 创建UI页面
app = wx.App()
window = wx.Frame(None, title="查询天气", size=(400, 300))
panel = wx.Panel(window)
label = wx.StaticText(panel, label="Hello World", pos=(10, 10))
butt=wx.Button(panel,label="查询",pos=(150,150))
butt.Bind(wx.EVT_BUTTON,onClicked)
window.Show(True)
app.MainLoop()



#crawlPage("101010100")


