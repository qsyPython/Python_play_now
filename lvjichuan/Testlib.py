# -*- coding: UTF-8 -*-

class Testlib:
    def __init__(self):# 类初始化调用
        print("准备就绪······")
    def say(self,str):
        print("开始写入日志······")
        fo = open("homework.txt", "a+",encoding='utf-8')# 这里和2.7有区别
        print("文件名: ", fo.name)
        fo.write(str+"\n")
        fo.close()