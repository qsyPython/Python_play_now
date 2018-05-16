#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
string、list和tuple都属于sequence（序列）
列表
变量[头下标:尾下标]

索引值以 0 为开始值，-1 为从末尾的开始位置

加号（+）是列表连接运算符，星号（*）是重复操作
'''

lList = ['abcd', 786, 2.23, 'tuyile', 70.2]
lA = [123, 'test']

print(lList)  # 输出完整列表
print(lList[0])  # 输出列表第一个元素
print(lList[1:3])  # 从第二个开始输出到第三个元素
print(lList[2:])  # 输出从第三个元素开始的所有元素

print(lA * 2)  # 输出两次列表
print(lList + lA)  # 连接列表

print()

# 列表中元素的改变
lList[0] = 'xyz987654321'
lList[2:6] = [2, 3, 'A', 12]
print(lList)

lList[2:3] = []
print(lList)

'''
列表脚本操作符
列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
len([1, 2, 3])	                        3	长度
[1, 2, 3] + [4, 5, 6]	                [1, 2, 3, 4, 5, 6]	组合
['Hi!'] * 4	                            ['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
3 in [1, 2, 3]	                        True	元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")	1 2 3	迭代
'''

L = ['Google', 'Runoob', 'Taobao']
'''
列表截取与拼接
L[2]	'Taobao'	读取第三个元素
L[-2]	'Runoob'	从右侧开始读取倒数第二个元素: count from the right
L[1:]	['Runoob', 'Taobao']	输出从第二个元素开始后的所有元素
'''

'''
遍历
在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
'''
print('\n遍历')
for Index, Val in enumerate(L):
    print(Index, Val)

'''
要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
'''
print('\n反向遍历')
for Val in reversed(range(1, 5)):
    print(Val)

'''
同时遍历两个或更多的序列，可以使用 zip() 组合
'''
print('\n同时遍历两个')
for A, B in zip(lList, L):
    print('lList {0} - L {1}.'.format(A, B))

'''
要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值
'''
print('\n按顺序遍历')
for Val in sorted(L):
    print(Val)
