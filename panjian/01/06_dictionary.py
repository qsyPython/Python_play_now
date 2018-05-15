#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
字典（dictionary）是Python中另一个非常有用的内置数据类型

字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取

字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合

键(key)必须使用不可变类型

在同一个字典中，键(key)必须是唯一的
'''

# dDict = {}
dDict = {'1': 'abcd', 'a': 786, 'b': 2.23, 'c': 'tuyile', '2': 70.2}

print(dDict)
# print(dDict[1]) # 错误
print(dDict['a'])

print(dDict.keys())  # 输出所有键
print(dDict.values())  # 输出所有值

del dDict['a']  # 删除键 'a'
dDict.clear()  # 清空字典
del dDict  # 删除字典

'''
遍历
在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
'''
print('\n遍历')
for Key, Val in dDict.items():
    print(Key, Val)
