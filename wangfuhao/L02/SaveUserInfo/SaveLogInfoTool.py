import time,platform
if __name__ == '__main__':
    from CheckPhoneNumberTool import *
else:
    from SaveUserInfo.CheckPhoneNumberTool import *

class SaveLogInfoTool():
    def __init__(self,account):
        self.account = account
        self.sysInfo = platform.system()
        self.startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.stopTime = None

    def writeInfo(self):
        try:
            f = open("logInfo.txt","a+",encoding="utf-8")
            self.stopTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            info = ('账号:{0},开始时间{1},结束时间{2},使用系统:{3}\n'.format(self.account , self.startTime, self.stopTime , self.sysInfo))
            f.writelines(info)
        except Exception as e:
            print(e)
        finally:
            f.close()

def main():
    while True:
        account = input("请输入账号(电话号码):")
        check = CheckPhoneNumber(account)
        try:
            isNumber = check.checkNumber()
            break
        except NumberError as error:
            print(error)

    pwd = input("请输入密码:")
    log_info = SaveLogInfoTool(account)
    while True:
        log_out = input('请使用该系统.....(按e退出):')
        if log_out == "e":
            log_info.writeInfo()
            break

if __name__ == '__main__':
    main()
