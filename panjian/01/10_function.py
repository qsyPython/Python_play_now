#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None
'''


def function_name(ParamA):
    pass


function_name('12')


def function_A(ParamA, ParamB):
    return ParamA + ParamB


iResult = function_A(1, 10)
print(function_A(1, 10))

'''
trings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象
'''
# 不可变对象实力
print('\n不可变对象实力')
sStr = 'abc'


def function_B(ParamA):
    print(ParamA)
    ParamA = '123'
    return


function_B(sStr)
print(sStr)

# 可变对象实力
print('\n可变对象实力')
lList = ['a', 'b', 'c']


def function_C(ParamA):
    print(ParamA)
    ParamA.append([1, 2])
    return


function_C(lList)
print(lList)

'''
关键字参数
'''
print('\n关键字参数')


def function_D(ParamA, ParamB):
    print(ParamA, ParamB)
    return


function_D(12, 34)
function_D(ParamB=1, ParamA='a')

'''
不定长参数
'''
print('\n不定长参数')


def function_E(ParamA, *Params):
    print(ParamA)
    print(Params)
    for Param in Params:
        print(Param)
    return


function_E(1)
function_E(1, 2, 3, 4)

'''
匿名函数
使用 lambda 来创建匿名函数
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数
'''
print('\n匿名函数')
sum = lambda iA, iB: iA + iB
print("%d + %d =" % (1, 3), sum(1, 3))

'''
变量作用域
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域
'''
B = int(2.9)  # 内建作用域

G = 0  # 全局作用域


def function_F():
    E = 1  # 闭包函数外的函数中

    def inner():
        L = 2  # 局部作用域


'''
只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的
也就是说这些语句内定义的变量，外部也可以访问
'''

'''
global 和 nonlocal关键字
当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字
'''
print('\nglobal关键字')
GA = 1


def function_G():
    global GA  # 需要使用 global 关键字声明
    print('函数内：', GA)
    GA = 123
    print('函数内，赋值后：', GA)


function_G()
print('函数外：', GA)

print('\nnonlocal关键字')


def function_H():
    HA = 10

    def inner():
        nonlocal HA  # nonlocal关键字声明
        print('方法内：', HA)
        HA = 11
        print('方法内，赋值后：', HA)

    inner()
    print('函数内：', HA)


function_H()
