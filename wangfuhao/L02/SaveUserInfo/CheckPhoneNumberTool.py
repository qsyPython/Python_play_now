import re

__all__ = ["CheckPhoneNumber","NumberError"]

class CheckPhoneNumber:
    def __init__(self,phoneNumebr):
        self.phoneNumber = phoneNumebr

    def checkNumber(self):
        p2 = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
        phonematch = p2.match(self.phoneNumber)
        if phonematch:
            return True
        else:
            raise NumberError("请输入正确的电话号码")

class NumberError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

def main():
    phone = input('请输入电话号码:')
    c = CheckPhoneNumber(phone)
    try:
        isNumber = c.checkNumber()
    except NumberError as error:
        print(error)

if __name__ == '__main__':
    main()
