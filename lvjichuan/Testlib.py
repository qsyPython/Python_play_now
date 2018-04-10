# -*- coding: UTF-8 -*-

class Testlib(object):
    def __init__(self,a):# 类初始化调用
        print("准备就绪······")
        self.a = a
    def say(self,str):
        print("开始写入日志······")

        # r 读、指针在开始
        # r+ 读、写、指针在开始
        # w 写、创建、覆盖、指针在开始
        # w+ 读、写、创建、覆盖、指针在开始
        # a 写、创建、指针在结尾
        # a+ 读、写、创建、指针在结尾

        fo = open("homework.txt", "a+",encoding='utf-8')# 这里和2.7有区别
        print("文件名: ", fo.name)
        fo.write(str+"\n")
        fo.close()

# 多重继承通过 super()调用__init__()方法时，虽然被继承了两次，但__init__()只调用一次
class TestlibB(Testlib):
    def __init__(self,a):
        super(TestlibB, self).__init__(a)
        print("处理完毕了")