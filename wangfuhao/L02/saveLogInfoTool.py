import time,platform

class saveLogInfoTool():
    def __init__(self):
        self.account = None;
        self.startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.stopTime = None

    def writeInfo(self):
        try:
            f = open("logInfo.txt","a+",encoding="utf-8")
            sysInfo = platform.system()
            info = ('账号:{0},开始时间{1},结束时间{2},使用系统:{3}\n'.format(self.account , self.startTime, self.stopTime , sysInfo))
            f.writelines(info)
        except Exception as e:
            print(e)
        finally:
            f.close()

    def userLogOut(self):
        self.stopTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def main(self):
        account = input("请输入登录名:")
        pwd = input("请输入密码:")
        log_info = saveLogInfoTool()
        log_info.account = account
        while True:
            log_out = input('请使用该系统.....(按e退出):')
            if log_out == "e":
                log_info.userLogOut()
                log_info.writeInfo()
                break

if __name__ == '__main__':
    s = saveLogInfoTool()
    s.main()
