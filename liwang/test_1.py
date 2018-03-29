#!/usr/bin/python3
# encoding: utf-8
import sys
from Carbon.Aliases import true


print("Hello, World!");

#python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。缩进的空格数是可变的，
# 但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：

# if True:
#     print ("true")
# else:
#     print("false")
# # 以下代码最后一行语句缩进数的空格数不一致，会导致运行错误：
#
# if True:
#     print ("Answer")
#     print ("True")
# else:
#     print ("Answer")
#     print ("False")    # 缩进不一致，会导致运行错误
#
# #python中的中括号[ ]：代表list列表数据类型，列表是一种可变的序列。其创建方法即简单又特别，像下面一样：
# total = ['item_one', 'item_two', 'item_three',
#         'item_four', 'item_five']
# print(list(total))
#
# #python大括号{ }花括号：代表dict字典数据类型，字典是由键对值组组成。冒号':'分开键和值，逗号','隔开组。用大括号创建的方法如下：
# total = {'item_one', 'item_two', 'item_three',
#         'item_four', 'item_five'}
# print(total)
#
# #python中的小括号( )：代表tuple元组数据类型，元组是一种不可变序列。创建方法很简单，大多时候都是用小括号括起来的。
# total = ('item_one', 'item_two', 'item_three',
#         'item_four', 'item_five')
# print(total)
#
#
#
# """
# Python3 中有六个标准的数据类型：
#
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Sets（集合）
# Dictionary
# """
#
# '''
# 数字(Number)类型
# python中数字有四种类型：整数、布尔型、浮点数和复数。
#
# int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# bool (布尔),如 true。
# float (浮点数), 如 1.23、3E-2
# complex (复数), 如 1 + 2j、 1.1 + 2.2j
# '''
#
# print(1,100000000000000000000299999338882)
#
# s = true
# print('%02d'%1)
# print("%d" % s)
#
# print(1.23)
# print complex (1 , 2)
#
# """
# 字符串(String)
# python中单引号和双引号使用完全相同。
# 使用三引号(\'''或\""")可以指定一个多行字符串。
# 转义符 '\'
# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
# 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python中的字符串不能改变。
# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
# 字符串的截取的语法格式如下：变量[头下标:尾下标]
#
# 英文字母：
# 字节数 : 1;编码：UTF-8
# 字节数 : 4;编码：UTF-16
# 中文：
# 字节数 : 3;编码：UTF-8
# 字节数 : 4;编码：UTF-16
#
# """
#
# print "_this\n""_is\n""_string"
# str = '请送到望京南 谢谢'
# print str
#
# #元素个数
# print( str.__len__())
# print(len(str))
#
# #字符读取
# str = 'abcdefghm'
# print(str[2:])
# print(str[2:5])# 不报错
# print(str[1:-1])
# print(str[0])
# print str * 2
# print( str + "_nihao")

"""
空行
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。
但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

记住：空行也是程序代码的一部分。

# Python允许你同时为多个变量赋值。
a = b = c =  1 #创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。
a, b, c = 1, 2, "runoob"  #两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。

（字典）
"""


"""
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Sets（集合）
Dictionary
"""

"""
一、Number（数字）
Python3 支持 int、float、bool、complex（复数）。

在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。

像大多数语言一样，数值类型的赋值和计算都是很直观的。

内置的 type() 函数可以用来查询变量所指的对象类型。
"""
# a, b, c, d = 20, 5.5, True, 4+3j
#
# print(type(a), type(b), type(c), type(d))
#
# print isinstance(a, int)

# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。

# var1 = 1
# var2 = 10
#
# print(var1,var2)
# del var1
# print(var1)

""" 对于加减乘除运算  注意点
1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。
4、在混合计算时，Python会把整型转换成为浮点数。
"""

# String Python中的字符串用单引号(')或双引号(")括起来，同时使用反斜杠(\)转义特殊字符。

# str = 'Runoob'
#
# print (str)  # 输出字符串
# print (str[0:-1])  # 输出第一个到倒数第二个的所有字符
# print (str[0])  # 输出字符串第一个字符
# print (str[2:5])  # 输出从第三个开始到第五个的字符
# print (str[2:])  # 输出从第三个开始的后的所有字符
# print (str * 2)  # 输出字符串两次
# print (str + "TEST")  # 连接字符串

"""
List（列表）
List（列表） 是 Python 中使用最频繁的数据类型。

列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

列表是写在方括号([])之间、用逗号分隔开的元素列表。

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

列表截取的语法格式如下：
变量[头下标:尾下标]
"""

# list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
# tinylist = [123, 'runoob']
#
# print (list)
# print (list[0])
# print (list + tinylist)

"""
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开。

元组中的元素类型也可以不相同：

"""

# tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
# tinytuple = (123, 'runoob')
#
# print (tuple)
# print (tuple[0])
# print (tuple + tinytuple)

"""
Set（集合）
集合（set）是一个无序不重复元素的序列。

基本功能是进行成员关系测试和删除重复元素。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

创建格式：
parame = {value01,value02,...}
或者
set(value)
"""

# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
#
# print(student)  # 输出集合，重复的元素被自动去掉
# # 成员测试
# if ('Rose' in student):
#     print('Rose 在集合中')
# else:
#     print('Rose 不在集合中')
#
# # set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
#
# print(a)
#
# print(a - b)  # a和b的差集
#
# print(a | b)  # a和b的并集
#
# print(a & b)  # a和b的交集
#
# print(a ^ b)  # a和b中不同时存在的元素

"""
Dictionary（字典）
字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。
"""

# tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
#
# print (tinydict)
# print (tinydict['name'])



"""
int(x [,base]) 将x转换为一个整数

float(x)  将x转换到一个浮点数

complex(real [,imag]) 创建一个复数

str(x) 将对象 x 转换为字符串

repr(x) 将对象 x 转换为表达式字符串

eval(str)  用来计算在字符串中的有效Python表达式,并返回一个对象

tuple(s) 将序列 s 转换为一个元组

list(s) 将序列 s 转换为一个列表

set(s) 转换为可变集合

dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组。

frozenset(s)  转换为不可变集合

chr(x) 将一个整数转换为一个字符

ord(x) 将一个字符转换为它的整数值

hex(x) 将一个整数转换为一个十六进制字符串

oct(x) 将一个整数转换为一个八进制字符串
"""

# if 函数

# age = int(input("请输入你家狗狗的年龄: "))
#
# print("")
# if age < 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age - 2) * 5
#     print("对应人类年龄: ", human)

# 循环语句
# var = 1
# while var == 1:  # 表达式永远为 true
#     num = int(input("输入一个数字  :"))
#     print ("你输入的数字是: ", num)
#
# print ("Good bye!")

# while 循环使用 else 语句
# count = 0
# while count < 5:
#    print (count, " 小于 5")
#    count = count + 1
# else:
#    print (count, " 大于或等于 5")

# 简单语句组
# //死循环 你妹的
# flag = 1
#
# while (flag): print ('12345678')
#
# print ("Good bye!")

# for 语句
# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟!")
#         break
#     print("循环数据 " + site)
# else:
#     print("没有循环数据!")
# print("完成循环!")

# range()函数
# for i in range(5,9) :
#     print(i)


# break和continue语句及循环中的else子句
# for letter in 'Runoob':  # 第一个实例
#     if letter == 'u':
#         break
#     print ( letter)
#
# var = 10  # 第二个实例
# while var > 0:
#     print ( var)
#     var = var - 1
#     if var == 5:
#         continue


# Python pass是空语句

# while True:
#     pass  # 等待键盘中断 (Ctrl+C)

# for letter in 'Runoob':
#     if letter == 'o':
#         pass
#         print ('pass')
#     print ( letter)

'''
迭代是Python最强大的功能之一，是访问集合元素的一种方式。

迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：iter() 和 next()。

字符串，列表或元组对象都可用于创建迭代器：
'''
# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# print(next(it))
#
# for x in it:
#     print ("x:",x)

"""
生成器
在 Python 中，使用了 yield 的函数被称为生成器（generator）。

跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

调用一个生成器函数，返回的是一个迭代器对象。

"""
# 以下实例使用 yield 实现斐波那契数列：

# import sys
#
#
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#        print next(f), ' '
#     except StopIteration:
#         sys.exit()

"""
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

def 函数名（参数列表）:
    函数体
"""

# 计算面积函数
# def area(width, height):
#     return width * height
#
# print area(10,10)


# 定义函数
# def printme(str):
#     "打印任何传入的字符串"
#     print (str);
#     return;
#
#
# # 调用函数
# printme("我要调用用户自定义函数!");
# printme("再次调用同一函数");

# 可更改(mutable)与不可更改(immutable)对象

"""
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，
只是修改另一个复制的对象，不会影响 a 本身。

可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
"""
# def ChangeInt( a ):
#     a = 10
#
# b = 2
# ChangeInt(b)
# print( b ) # 结果是 2

# 可写函数说明
# def changeme(mylist):
#     "修改传入的列表"
#     mylist.append([1, 2, 3, 4]);
#     print ("函数内取值: ", mylist)
#     return
#
#
# # 调用changeme函数
# mylist = [10, 20, 30];
# changeme(mylist);
# print ("函数外取值: ", mylist)


#数据结构
# list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
# list.extend(L)	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
# list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，
# 例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
# list.remove(x)	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
# list.pop([i])	从列表的指定位置删除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。
# 元素随即从列表中被删除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
# list.clear()	移除列表中的所有项，等于del a[:]。
# list.index(x)	返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
# list.count(x)	返回 x 在列表中出现的次数。
# list.sort()	对列表中的元素进行排序。
# list.reverse()	倒排列表中的元素。

# list.copy()	返回列表的浅复制，等于a[:]。

# 将列表当做堆栈使用
# 列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。
# 用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。

# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack)


# ①从参数方面来讲：
#
# map()函数：
#
# map()包含两个参数，第一个是参数是一个函数，第二个是序列（列表或元组）。其中，函数（即map的第一个参数位置的函数）可以接收一个或多个参数。
#
# reduce()函数：
#
# reduce() 第一个参数是函数，第二个是 序列（列表或元组）。但是，其函数必须接收两个参数。
#
#
#
# ②从对传进去的数值作用来讲：
#
# map()是将传入的函数依次作用到序列的每个元素，每个元素都是独自被函数“作用”一次；（请看下面的栗子）
#
# reduce()是将传人的函数作用在序列的第一个元素得到结果后，把这个结果继续与下一个元素作用（累积计算），

# 最终结果是所有的元素相互作用的结果。

# 传入一个参数
# def one_p(x):
#     return x * x
#
#
# print 'map1.1:', map(one_p, range(1, 5))
# # 结果：map1.1: [1, 4, 9, 16]
# print 'map1.2:', map(one_p, [1, 2, 3, 4, 5, 6])
# # 结果：map1.2: [1, 4, 9, 16, 25, 36]
#
# # 传入多个参数
# a = [1, 2, 3, 4, 5]
# b = [1, 1, 6, 2, 3]
# c = [1, 2, 3, 4, 5]
# s = map(lambda (x, y, z): x * y * z, zip(a, b, c))
# print 'map2:', s
# 结果：map2: [1, 4, 54, 32, 75]

# r1 = reduce(lambda x, y: x * y, (2, 2, 6, 2))  # 运算过程：(((2*2)*6)*2)
# r2 = reduce(lambda x, y: x * y, (2, 2, 6),
#             2)  # <span style="font-family: Arial, Helvetica, sans-serif;">运算过程：(((2*2)*6)*2)</span>
#
# print 'r1:', r1  # 结果：r1: 48
# print 'r2:', r2  # 结果：r2: 48


# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
#
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

# !/usr/bin/python
# -*- coding: UTF-8 -*-

# def is_odd(n):
#     return n % 2 == 1
#
#
# newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(newlist)


# sort 与 sorted 区别：
#
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
#
# list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。


#  a [5, 7, 6, 3, 4, 1, 2]
# b [1, 2, 3, 4, 5, 6, 7]
# L = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
# sorted(L, cmp=lambda x, y: cmp(x[1], y[1]))  # 利用cmp函数
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
#  sorted(L, key=lambda x: x[1])  # 利用key
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]


# 作业：
# 写一个简单的demo 尽量使用所有的基本数据语法和函数 例如解析一篇歌词