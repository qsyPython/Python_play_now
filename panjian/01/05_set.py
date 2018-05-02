#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
集合（set）是一个无序不重复元素的序列。

基本功能是进行成员关系测试和删除重复元素。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''

sSet = {'abcd', 786, 2.23, 'tuyile', 70.2}
sF = {123, 'test'}

print(sSet)

if ('abcd' in sSet):
    print('True')
else:
    print('False')

sJ = set('abcd12')
sK = set('abcd123')
print(sJ)
print(sK)
print(sJ - sK)
print(sK - sJ)  # 差集
print(sK | sJ)  # 并集
print(sK & sJ)  # 交集
print(sK ^ sJ)  # 不同时存在的元素
