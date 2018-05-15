#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用from语句可以把模块直接导入当前命名空间，from语句并不引用导入对象的命名空间，而是将被导入对象直接引入当前命名空间。

# 将模块package.calculator导入全局命名空间，例如访问calculator中属性时用package.calculator.sum
# import package.calculator

# 　将模块calculator导入全局命名空间，例如访问calculator中属性时用calculator.sum
# from package import calculator

# 将模块calculator的属性直接导入到命名空间中，例如访问calculator中属性时直接用sum
# from package.calculator import sum

import package.calculator

iSum = package.calculator.sum(1, 2, 3)
print('sum :', iSum)

iAvg = package.calculator.avg(12, 5, 8)
print('avg :', iAvg)

import package.http.ip

sIP = '192.168.1.1'
bRes = package.http.ip.isIP(sIP)
print(sIP, 'is IP :', bRes)

print(package.re)
