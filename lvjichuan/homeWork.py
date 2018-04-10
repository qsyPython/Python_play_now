# 模块2：(自学时间: 1周，分享人：待定)
# 模块和文件处理（系统模块和第3方模块使用，文件I/O和序列化）；
# 类和实例（创建、使用、面向对象的特性详解、枚举类；多重继承和元类）
# 异常处理和代码测试（python的异常处理，函数和类的测试）；


import os
import sys
# os 提供了一种方便的使用操作系统函数的方法，负责程序与操作系统的交互，提供了访问操作系统底层的接口。例如对于文件的操作
# sys 可供访问由解释器使用或维护的变量和与解释器进行交互的函数，负责程序与python解释器的交互，提供了一系列的函数和变量，用于操控python的运行时环境。例如对于程序标准输出的操作

import platform
# 获取操作系统信息

from Testlib import *
from MJlib import *

print("······欢迎使用简易记事本······")
# sys.setdefaultencoding('utf8')
print("当前系统编码：",sys.getdefaultencoding())
print(sys.argv[0])
# print(sys.argv[1]) 从外部获取参数

print("检查操作系统信息······",platform.uname())
print("检查当前python版本······",platform.python_version())

# os.F_OK: 作为access()的mode参数，测试path是否存在。
# os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
# os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
# os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。

ret = os.access("homework.txt", os.F_OK)
print("检查文件path是否存在······",ret)

str=input("请输入想要保存的文字······")

note=Testlib('Testlib')
note.say(str)

inote=TestlibB('TestlibB')


# 采用枚举类
color=MJlib.blue.value
print("温馨提示：今天你的幸运颜色数字：",color)

# 元类
# 元类的主要使用场景是创建一个API。99%的场景，其实并不需要元类。
# 除了type,一切皆对象，不是类的实体，就是元类的实体。
# type可以接受一个类的描述作为参数，然后返回一个类。
# ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

def fn(self, name='主人'):  # 假如有一个函数叫fn
    print('感谢使用, %s.' % name,'再见')

appEnd = type('appEnd', (object,), dict(say_bye=fn))  # 创建 appEnd class
# 从Hello类创建一个实例hello
hello = appEnd()
# 使用hello调用方法say_hello
hello.say_bye()