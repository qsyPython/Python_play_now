# 第5期作业内容:
# 通过web框架实现一个手机号的登录注册功能(可以使用html或者GUI搭建登录注册页面)，登陆成功后显示的界面为xxx已登陆成功。
# 要求:
#        1. 输入的手机号做正则校验，如有余力，可以试着做下手机号验证认证
#        2. 密码要求 8位及以上（包含8位），必须包含字母和数字，且第1个必须为字母
#        3. 使用数据库完成账号密码的存取

import wx
import pymysql

#生成登录UI
def createUI():
    # 创建UI页面
    app = wx.App()
    # 窗口标题
    window = wx.Frame(None, title="程序登录窗口", size=(400, 280))
    panel = wx.Panel(window)
    #登录输入
    labelPhone= wx.StaticText(panel, label="手机号", pos=(30, 40))
    inputPhone=wx.TextCtrl(panel,pos=(100,40),size=(180,30))
    labelPWD = wx.StaticText(panel, label="密码", pos=(30,80))
    inputPWD = wx.TextCtrl(panel, pos=(100, 80),size=(180,30),style=wx.TE_PASSWORD)
    buttonSearch=wx.Button(panel,label="立即登录/注册",pos=(140,150))
    buttonSearch.Bind(wx.EVT_BUTTON,onClicked)
    # 展示UI
    window.Show(True)
    app.MainLoop()
#查询点击动作
def onClicked(self):
    checkUser()
#进行数据库查询
def checkUser():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "acms")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print("Database version : %s " % data)
    # 关闭数据库连接
    db.close()



createUI()

