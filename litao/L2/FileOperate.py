import os
import re
from urllib.request import urlopen
local_path = 'C:/Users/andro/python_test.txt'

def write_text(phon_num):
    with open(local_path, 'a') as write:
        write.write(phon_num+'\n')


# 文件的内容读取    #内容比较少 所以直接用read方法   read(size)用来获取未知的大小的文件比较稳妥
def read_text():
    with open(local_path, 'r')as read:
        str = read.read()
        if str.__len__() > 0:
            print(str)
        else:
            print('没有数据')


# 判断文件是否存在
def create_text(addnum):
    if os.path.exists(local_path):
        read_text(addnum)
    else:
        write_text(addnum)

def getPageCode(url):
    file = urlopen(url)
    text = file.read()
    file.close()
    text = text.decode("utf-8")
    return text



class File_utils:
    def __index__(self,addnum):
        self.__addnum = addnum

    def __set__(self,value):
        self.__addnum = value

    def __get__(self, instance, owner):
        return self.__addnum

    def select_phone(self):
        phone_num2 = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
        phone_num3 = phone_num2.match(self.__addnum)
        if phone_num3:

            url = "http://www.sjgsd.com/n/?q=" + phone_num3.group()
            text = getPageCode(url)
            pat = []
            pat.append('(?<=归属地：</span>).+(?=<br />)')
            pat.append('(?<=卡类型：</span>).+(?=<br />)')
            pat.append('(?<=运营商：</span>).+(?=<br />)')
            pat.append('(?<=区号：</span>).+(?=<br />)')
            pat.append('(?<=邮编：</span>).+(?=<br />)')

            for i in range(len(pat)):
                m = re.search(pat[i], text)
                if m:
                    v = m.group(0)
                    write_text(phone_num3.group()+'======'+pat[i]+'======'+v)
                    print(v)
            # 读取文件内数据
            # read_text()
        else:
            print('手机号有误')






