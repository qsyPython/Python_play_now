# -*- coding: utf-8 -*-
# 模块1
# 变量和数据类型（变量、字符串、数字、列表、元组、字典、集合）；
# 常用语句和基础语法（条件语句如if、while、for和python语法格式）；
# 函数(定义、调用、函数的分类及其使用介绍)和高阶函数（map/reduce、filter、sorted等）

# 在Python中，能够直接处理的数据类型有以下几种：整数 浮点数 字符串 布尔值(可以用and、or和not运算) 空值
# 此外，Python还提供了列表、字典等多种数据类型，还允许创建自定义数据类型
# 字符串用“” ‘’表示 转义字符\ Python允许用'''...'''的格式表示多行内容 %运算符就是用来格式化字符串的
# 变量名必须是大小写英文、数字和_的组合，且不能用数字开头
print('I\'m ok.')
# I'm ok.
print('I\'m learning\nPython.')
# I'm learning？
# Python.

# Python内置的一种数据类型是列表：list列表用[ ]标识。list是一种有序的集合，可以随时添加和删除其中的元素
l = [1,45,"wf","dff"]
l.append(23)#将23添加到末尾
l.insert(2,"we")#将“we”插入索引为2的位置
l.pop()#删除l末尾的元素
l.pop(2)#删除指定位置的元素
l.remove(1)#根据值删除元素
len(l)#列表的长度
[x * x for x in range(1, 11)]#列表生成式快速生成list

#tuple和list非常类似，用（）标识，但是tuple一旦初始化就不能修改
t = (2,35,"dflfhi")

#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']#取出key为'Michael'的值

#常用语句int(x[, base])将x转换为一个整数 long(x[, base] )将x转换为一个长整数
# float(x)将x转换到一个浮点 complex(real[, imag])创建一个复数
# str(x)将对象x转换为字符串 repr(x)将对象x转换为表达式字符串
# eval(str)用来计算在字符串中的有效Python表达式, 并返回一个对象
# tuple(s)将序列s转换为一个元组 list(s)将序列s转换为一个列表
# set(s)转换为可变集合 dict(d)创建一个字典。必须是一个序列(key, value)元组。等等


#if条件判断
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
#while循环
num =0
while num<5:
    print(num)
    num +=1

#for循环
for x in range(101):
    sum = sum + x
print(sum)
#break语句可以提前退出循环 continue语句跳过当前的这次循环


#函数
#在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回
#除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#lambda表达式 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
sum = lambda arg1, arg2: arg1 + arg2
def sum(arg1,arg2):
    return arg1 + arg2

#高阶函数
#map()和reduce()
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]) #[1, 4, 9, 16, 25, 36, 49, 64, 81]

from functools import reduce
def fn(x, y):
   return x * 10 + y

reduce(fn, [1, 3, 5, 7, 9])#13579

#filter()函数用于过滤序列
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))# 结果: [1, 5, 9, 15]

#sorted()函数就可以对list进行排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
#['Zoo', 'Credit', 'bob', 'about']