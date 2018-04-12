# 模块就是一个保存了Python代码的文件。模块能定义函数，类和变量。模块里也能包含可执行的代码

# import 语句
# 想使用Python源文件，只需在另一个源文件里执行import语句
# import module1, module2,... moduleN
import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world---------------------------!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

test()

# From…import 语句
# Python的from语句让你从模块中导入一个指定的部分到当前命名空间中
# from modname import name1, name2, ... nameN

from io import StringIO,BufferedReader


# From…import* 语句
# 把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：

from sys import *


# 作用域
# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。
# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，我们自己的变量一般不要用这种变量名；
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。


# 安装第三方模块，是通过包管理工具pip完成的
# pip3 install Pillow
# 在使用Python时，我们经常需要用到很多第三方库，例如，上Pillow，以及MySQL驱动程序，Web框架Flask，科学计算Numpy等。用pip一个一个安装费时费力，还需要考虑兼容性。
# 我们推荐直接使用Anaconda，这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库，我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用。可以从Anaconda官网下载GUI安装包，安装包有500~600M
# 下载后直接安装，Anaconda会把系统Path中的python指向自己自带的Python，并且，Anaconda安装的第三方模块会安装在Anaconda自己的路径下，不影响系统已安装的Python目录。




# File对象的属性
# file.closed	返回true如果文件已被关闭，否则返回false。
# file.mode	返回被打开文件的访问模式。
# file.name	返回文件的名称。


# 打开一个文件
fo = open("D:/note.txt", "r")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)
print(fo.read()) # read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
fo.close() # 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源
print("\n")


# Write()方法
# Write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。'w'或者'wb'表示写文本文件或写二进制文件
# 可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了
# 以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾可以传入'a'以追加（append）模式写入。
f = open("D:/note.txt", "a")
f.write("Python is a great language.\n")
f.close()


# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
try:
    f = open('D:/note.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()
# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

with open('D:/note.txt', 'r') as f:
    print(f.read())
    # print("\n")


# 二进制文件
# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可


# 很多时候，数据读写不一定是文件，也可以在内存中读写。StringIO顾名思义就是在内存中读写str
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：getvalue()方法用于获得写入后的str

from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())
print("\n")
# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：

from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())# 把末尾的'\n'删掉
print("\n")

# BytesIO
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
print("\n")


# 读取的话和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()


# 要在Python程序中执行这些目录和文件的操作,Python内置的os模块直接调用操作系统提供的接口函数
import os
print(os.name) # 操作系统类型 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统


# 要获取详细的系统信息，可以调用uname()函数：
# print(os.uname())  # 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的


# 环境变量
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
print(os.environ)
print("\n")

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：


# 查看当前目录的绝对路径:
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



# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling

# Python提供了pickle模块来实现序列化
import pickle
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象

f = open('dump.txt', 'rb')
d = pickle.load(f)
print(d)
print("\n")
f.close()


# try...except...finally...的错误处理机制

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print("\n")
# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
# 执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕
# 如果发生了不同类型的错误，应该由不同的except语句块处理,可以有多个except来捕获不同类型的错误;如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print("\n")

# 调用栈
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

#main()

# logging
# 既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
# Python内置的logging模块可以非常容易地记录错误信息：

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
#main()

# 抛出错误
# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
# 只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
# foo('0')



# 调试
# 第一种方法用print()把可能有问题的变量打印出来  第二种方法断言凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
def foo(s):
    n = int(s)
    # print('>>> n = %d' % n)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

# main()

# 第3种方式把print()替换为logging
# logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。
# 同理，指定level=WARNING后，debug和info就不起作用了
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
# print(10 / n)






