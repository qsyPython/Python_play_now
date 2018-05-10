#!/usr/bin/env python3
# -*- coding: utf-8 -*-

while True:
    try:
        iI = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Try again   ")

print(iI)


'''
raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。

如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
'''
try:
    raise NameError('Tuyile')
except NameError:
    print('An exception flew by!')
    raise


# 用户自定义异常
# 异常应该继承自 Exception 类，或者直接继承，或者间接继承
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2 * 2)
except MyError as e:
    print('My exception occurred, value:', e.value)
