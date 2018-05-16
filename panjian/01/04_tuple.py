#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
string、list和tuple都属于sequence（序列）
元组
元组中的元素值是不允许修改的
'''

tTuple = ('abcd', 786, 2.23, 'tuyile', 70.2)
tB = (123, 'test')

print(tTuple)  # 输出完整列表
print(tTuple[0])  # 输出列表第一个元素
print(tTuple[1:3])  # 从第二个开始输出到第三个元素
print(tTuple[2:])  # 输出从第三个元素开始的所有元素

print(tB * 2)  # 输出两次列表
print(tTuple + tB)  # 连接列表

# tTuple[1] = 21  # 修改元组元素的操作是非法的

print()

tC = ()  # 空元组
tD = (20,)  # 一个元素，需要在元素后添加逗号
tE = (20)  # 不加逗号，类型为整型

print(tC, tD)

'''
元组运算符
len((1, 2, 3))	                3	计算元素个数
(1, 2, 3) + (4, 5, 6)	        (1, 2, 3, 4, 5, 6)	连接
('Hi!',) * 4	                ('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
3 in (1, 2, 3)	                True	元素是否存在
for x in (1, 2, 3): print (x,)	1 2 3	迭代
'''

'''
元组索引&截取
L[2]	'Runoob'	读取第三个元素
L[-2]	'Taobao'	反向读取；读取倒数第二个元素
L[1:]	('Taobao', 'Runoob')	截取元素，从第二个开始后的所有元素。
'''
