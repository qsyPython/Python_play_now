# JetBrains PyCharm 简单的配置使用，git的链接配置，如何更便捷的管理代码
# .gitgnore的配置

# 这一行是注释 //
print("HelloWorld")

#  Numbers（数字）
#  String（字符串）
#  List（列表）
#  Tuple（元组）
#  Dictionary（字典）
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
name = "tom"
# 在"""中的为原始格式
string = """
mmo
   mmm
      ddd     dfffd
         fff
"""
print(string)
# 字符 输出可以带颜色
print("\033[0;31m%s\033[0m" % "输出红色字符")
# 选择位置打印
print(name[2])
print(name[0:3])  # range 区间
# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（所谓嵌套）。
# 列表用[ ]标识。是python最通用的复合数据类型。看这段代码就明白。
# 列表中的值得分割也可以用到变量[头下标:尾下标]，就可以截取相应的列表，从左到右索引默认0开始的，从右到左索引默认-1开始，下标可以为空表示取到头或尾。
list = [1, 2, 4, "555", 1.0, ["ssddd"]]
listB = ["45566", "3333"]
print(list[0])
print(list[1:4])
print(list + listB)

# python 元祖 tuple,元组用"()"标识。内部元素用逗号隔开。但是元素不能二次赋值，相当于只读列表
# 元组是不允许更新的。而列表是允许更新的
tuple = (1, 4, 3, 5, "222", 12.0)
print(tuple[2])
# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
# 类似于java中的map
dict = {}
dict[1] = "ssssss"
dict["two"] = 2
print(dict.keys())
print(dict.values())
print(dict[1])
print(dict["two"])

# int(x[, base])将x转换为一个整数
# long(x[, base] )将x转换为一个长整数
# float(x)将x转换到一个浮点数
# complex(real[, imag])创建一个复数
# str(x)将对象x转换为字符串
# repr(x)将对象x转换为表达式字符串
# eval(str)用来计算在字符串中的有效Python表达式, 并返回一个对象
# tuple(s)将序列s转换为一个元组
# list(s)将序列s转换为一个列表
# set(s)转换为可变集合
# dict(d)创建一个字典。必须是一个序列(key, value)元组。
# frozenset(s)转换为不可变集合
# chr(x)将一个整数转换为一个字符
# unichr(x)将一个整数转换为Unicode字符
# ord(x)将一个字符转换为它的整数值
# hex(x)将一个整数转换为一个十六进制字符串
# oct(x)将一个整数转换为一个八进制字符串
print(str(dict["two"]))


# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
a = 21
b = 10
c = 0
if a == b:
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")
if a != b:
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")
if a < b:
    print("4 - a 小于 b")
else:
    print("4 - a 大于等于 b")
if a > b:
    print("5 - a 大于 b")
else:
    print("5 - a 小于等于 b")
if a <= b:
    print("6 - a 小于等于 b")
else:
    print("6 - a 大于  b")
if b >= a:
    print("7 - b 大于等于 a")
else:
    print("7 - b 小于 a")

# or and not 与 或 非
# in / not in 在 不在
x = 5
string =[1,2,3,45,"dfdfdfaaaaa"]
string2 = [1,"ddd","3dfda",34445]
if(x in string or x == 4):
   print(x)
elif(x not in string):
    for y in string:
        print(y)
else:
    print(string)

name = "12334"
if name == "444333":
    print("True")
elif name == "2455":
    print("True")
else:
    print("False")

a = 5
if a > 4 and a < 10:
    print("Ture1111")
else:
    print("False2222")

i = 0
while i < 10:
    print("this is", i);i = i + 1
else:
    print("is ok")

list = [1, 2, 4, "555", 1.0]
for x in list:
    if x == 2:
        print("2222222")
    else:
        print(x)

for x in range(10, 20):
    print(x)

for x in "3545349xdd":
    if x == "x":
        print("is over")
        break
    else:
        print("conutine")
# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
list = [1, 2, 3, 4, 5, 56, 733, 744, 88,"sss",'ddd']
it = iter(list)
print(next(it))

for x in it:
    print(x)

# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
# 调用一个生成器函数，返回的是一个迭代器对象。
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


# def 函数名（参数列表）:
#    函数体
def hello():
    print("hello")

def area(str, width, height):
    print(str, width * height)
    return width * height


# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
# 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
# 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
# python 函数的参数传递：
# 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
# 可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

def changeList(aList):
    aList.append([1, 2, 3, 4, 5])
    print("list", aList)
    print("lsit[0]---->", aList[0])
    print("alist[1]----->", aList[1])
    print("alist[2]------>", aList[2])


# 不定长参数
def printinfo(*value):
    for val in value:
        print(val)


# python 使用 lambda 来创建匿名函数。
# 所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
# lambda 只是一个表达式，函数体比 def 简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
# 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

# 实际上意思是arg1 + arg2  前面是传入参数，后面是返回值
sum = lambda arg1, arg2: (arg1 + arg2) * arg1

def sum(arg1,arg2):
    return arg1 + arg2
# python map()函数：map()是python内置的高阶函数，
# 它接收一个函数f和一个list，并且把函数f依次作用在list的每个元素上，
# 返回一个iterators，可以这样处理list(map())变成list
def fn(x):
    return x * x


mylist = map(fn, [1, 2, 3, 4])
for each in mylist:
    print(each)

# python reduce()函数:
# reduce()函数是python内置的一个高阶函数。reduce()函数和map()类似，一个函数f，一个list，但行为和map()不同，reduce传入的函数f必须接收两个参数，
# reduce对list的每个元素反复调用函数f，并返回结果

from functools import reduce


def fn(x, y):
    return x + y


ans = reduce(fn, [1, 2, 3, 4])
print("songxin",ans)


# filter函数接收一个函数f和一个list，
# 函数f的作用是对每个元素进行判断，返回True或者False，
# filter()根据判断结果自动过滤掉不符合条件的元素，
# 返回符合要求的元素组成的list
def deleteNone(s):
    return s and len(s.strip()) > 0


mylist = filter(deleteNone, ['test', None, '', 'str', ' ', 'END'])

for each in mylist:
    print(each)

if __name__ == '__main__':
    hello()
    area("width * height = ", 2, 3)
    changeList(["dfdfd", "sadffsf"])
    printinfo(1, 2, 3, 4, 5, "sdsds", [3, "dddd", ], 'ddddffff')
    print(sum(1, 2))
    fn(3, 2)

mlist = map(lambda x: x, [1,2,3])
for x in mlist:
    print(x)