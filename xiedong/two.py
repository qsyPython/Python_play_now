# 模块2
# 模块和文件处理（系统模块和第3方模块使用，文件I/O和序列化）；
# 类和实例（创建、使用、面向对象的特性详解、枚举类；多重继承和元类）
# 异常处理和代码测试（python的异常处理，函数和类的测试）；

#模块就是一个保存了Python代码的文件。模块能定义函数，类和变量。模块里也能包含可执行的代码
#模块使用import语句  From…import 语句 From…import* 语句
from io import StringIO,BufferedReader

#作用域 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

# 安装第三方模块，是通过包管理工具pip完成的
# pip3 install Pillow
# 在使用Python时，我们经常需要用到很多第三方库，例如，上Pillow，以及MySQL驱动程序，Web框架Flask，科学计算Numpy等。用pip一个一个安装费时费力，还需要考虑兼容性。
# 我们推荐直接使用Anaconda，这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库，我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用。可以从Anaconda官网下载GUI安装包，安装包有500~600M
# 下载后直接安装，Anaconda会把系统Path中的python指向自己自带的Python，并且，Anaconda安装的第三方模块会安装在Anaconda自己的路径下，不影响系统已安装的Python目录。

#文件I/O
#open()函数 read() write() close() with语句来自动帮我们调用close()方法
# try:
#     f = open('D:/note.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
#
# with open('D:/note.txt', 'r') as f:
#     print(f.read())
#     # print("\n")

#StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())# 把末尾的'\n'删掉
print("\n")

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
print("\n")

#Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中
# 查看当前目录的绝对路径:
import os
print(os.getcwd())
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:    把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
print(os.path.join('/Users/michael', 'testdir'))
# 创建一个目录
# os.mkdir('D:/Python_play_now/wangyong/testdir')
# 删掉一个目录:
# os.rmdir('D:/Python_play_now/wangyong/testdir')
# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split('/Users/michael/testdir'))
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print(os.path.splitext('/path/to/file.txt'))

# Python提供了pickle模块来实现序列化
# pickle.dumps()方法把任意对象序列化成一个bytes
# pickle.loads()方法反序列化出对象

#错误
# try...except...finally...的错误处理机制 Python内置的logging模块可以非常容易地记录错误信息
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print("\n")

# 调试
# 第一种方法用print()把可能有问题的变量打印出来  第二种方法断言凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
## 第三种方式把print()替换为logging
# logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
#debug调试

# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

#继承
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# 多态：任何依赖父类作为参数的函数或者方法都可以不加修改地正常运行  由运行时该对象的确切类型决定
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')

# 枚举
# 枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
# @unique装饰器可以帮助我们检查保证没有重复值。

for name, member in Weekday.__members__.items():
    print(name, '=>', member)


#类名应采用驼峰命名法 ， 即将类名中的每个单词的首字母都大写， 而不使用下划线。 实例名和模块名都采用小写格式， 并在单词之间加上下划线。
# 对于每个类， 都应紧跟在类定义后面包含一个文档字符串。
# 这种文档字符串简要地描述类的功能， 并遵循编写函数的文档字符串时采用的格式约定。
# 每个模块也都应包含一个文档字符串， 对其中的类可用于做什么进行描述。
# 可使用空行来组织代码， 但不要滥用。 在类中， 可使用一个空行来分隔方法； 而在模块中， 可使用两个空行来分隔类