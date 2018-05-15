#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
数据类型转换
'''

iA = 123
sB = 'abc'

# 将x转换为一个整数
# int(x [,base])
print('int :', int('123'))

# 将x转换到一个浮点数
# float(x)
print('float :', float('321'))

# 创建一个复数
# complex(real [,imag])
print('complex :', complex(1))

# 将对象 x 转换为字符串
# str(x)
print('str :', str('str'))

# 将对象 x 转换为表达式字符串
# repr(x)
print('repr :', repr('reg'))

# 用来计算在字符串中的有效Python表达式,并返回一个对象
# eval(str)
print('eval :', eval('1+2'))

# 将序列 s 转换为一个元组
# tuple(s)
print('tuple :', tuple('12'))

# 将序列 s 转换为一个列表
# list(s)
print('list :', list('12'))

# 转换为可变集合
# set(s)
print('set :', set('12'))

# 创建一个字典。d 必须是一个序列 (key,value)元组。
# dict(d)
print('dict :', dict(('12', 'ab')))

# 转换为不可变集合
# frozenset(s)
print('frozenset :', frozenset('12'))

# 将一个整数转换为一个字符
# chr(x)
print('chr :', chr(63))

# 将一个字符转换为它的整数值
# ord(x)
print('ord :', ord('a'))

# 将一个整数转换为一个十六进制字符串
# hex(x)
print('hex :', hex(63))

# 将一个整数转换为一个八进制字符串
# oct(x)
print('oct :', oct(63))
