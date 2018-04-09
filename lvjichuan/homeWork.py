# 模块2：(自学时间: 1周，分享人：待定)
# 模块和文件处理（系统模块和第3方模块使用，文件I/O和序列化）；
# 类和实例（创建、使用、面向对象的特性详解、枚举类；多重继承和元类）
# 异常处理和代码测试（python的异常处理，函数和类的测试）；


import os
import sys
import platform
from Testlib import *

# r 读、指针在开始
# r+ 读、写、指针在开始
# w 写、创建、覆盖、指针在开始
# w+ 读、写、创建、覆盖、指针在开始
# a 写、创建、指针在结尾
# a+ 读、写、创建、指针在结尾
print("······欢迎使用简易记事本······")

print("检查操作系统信息······",platform.uname())
print("检查当前python版本······",platform.python_version())

# os.F_OK: 作为access()的mode参数，测试path是否存在。
# os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
# os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
# os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。

ret = os.access("homework.txt", os.F_OK)
print("检查文件path是否存在······",ret)

str=input("请输入想要保存的文字······")

note=Testlib()
note.say(str)

