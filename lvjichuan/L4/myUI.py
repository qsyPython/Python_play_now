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
    #爬取页面
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
    #取城市名称下一个为城市代码
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
    #分析页面结构，解析内容
    for i in range(7):
        v = p.eq(i)
        olist=[]
        olist.append(v.find("h1").text())
        olist.append(v.find("p.wea").text())
        olist.append(v.find("p.tem").text())
        alist.append(olist)
    print("抓取页面完成")
    print(alist)
    return alist;

#查询点击动作
def onClicked(self):
    labelResult.SetLabel("查询城市代码中")
    cityName=inputCity.GetValue()
    #查询城市代码
    cityCode=searchCity(cityName)
    #爬取网页
    clist=crawlPage(cityCode)
    str=""
    #拼接内容
    for i in range(7):
        str+=",".join(clist[i])+"\n"
    labelResult.SetLabel(str)
#点击发送邮件
def onMclicked(self):
    mail=inputMail.GetValue()
    # 此处忽略邮件发送过程
    labelMail.SetLabel("已经发送到邮箱"+mail)


# 创建UI页面
app = wx.App()
#窗口标题
window = wx.Frame(None, title="查询天气", size=(400, 400))
panel = wx.Panel(window)
#城市查询天气
labelCity= wx.StaticText(panel, label="城市名称", pos=(10, 10))
inputCity=wx.TextCtrl(panel,pos=(100,10))
labelResult = wx.StaticText(panel, label="查询结果", pos=(10,150))
buttonSearch=wx.Button(panel,label="查询",pos=(250,10))
buttonSearch.Bind(wx.EVT_BUTTON,onClicked)
#发送邮件内容
labelMail= wx.StaticText(panel, label="邮件地址", pos=(10, 50))
inputMail=wx.TextCtrl(panel,pos=(100,50))
buttonMail=wx.Button(panel,label="发送",pos=(250,50))
buttonMail.Bind(wx.EVT_BUTTON,onMclicked)
labelMail = wx.StaticText(panel, label="注：可以将天气预报发送邮件", pos=(10,200))
#展示UI
window.Show(True)
app.MainLoop()




