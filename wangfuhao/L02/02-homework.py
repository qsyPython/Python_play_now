"""
Python的第2期作业：
写或仿写一个供大家可以import 的类库
要求：1、至少有一个方法和__init__
2、完整易懂的使用方法或注释
3、实现的功能和场景不限（比如手机号码检查，但不能仅限于长度、开头、数字，要丰富更多其他内容，例如归属地等）
"""
#实现一个记录登录信息功能
"""
1.记录用户的账号  登录时间  登录的使用的系统
"""
import time,platform

class saveLogInfoTool():
    def __init__(self,account_temp):
        self.account = account_temp
        self.nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def writeInfo(self,stop_time_temp):
        try:
            f = open("logInfo.txt","a+",encoding="utf-8")
            sysInfo = platform.system()
            info = ('账号:{0},开始时间{1},结束时间{2},使用系统:{3}\n'.format(self.account , self.nowTime, stop_time_temp , sysInfo))
            f.writelines(info)
        except Exception as e:
            print(e)
        finally:
            f.close()

def main():
    account = input("请输入登录名:")
    pwd = input("请输入密码:")
    f = saveLogInfoTool(account)
    while True:
        logout = input('请使用该系统.....(按e退出):')
        if logout == "e":
            stopTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            f.writeInfo(stopTime)
            break

if __name__ == '__main__':
    main()