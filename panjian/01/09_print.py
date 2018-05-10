#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print(123)

lA = [123, 'test']
print(lA)

print('换行')
for iI in range(0, 3):
    print(iI)

print('不换行')
for iI in range(0, 3):
    print(iI, end='')
print()

'''
转换类型          含义
d,i             带符号的十进制整数
o               不带符号的八进制
u               不带符号的十进制
x               不带符号的十六进制（小写）
X               不带符号的十六进制（大写）
e               科学计数法表示的浮点数（小写）
E               科学计数法表示的浮点数（大写）
f,F             十进制浮点数
g               如果指数大于-4或者小于精度值则和e相同，其他情况和f相同
G               如果指数大于-4或者小于精度值则和E相同，其他情况和F相同
C               单字符（接受整数或者单字符字符串）
r               字符串（使用repr转换任意python对象)
s               字符串（使用str转换任意python对象）
'''

'''
字符串格式化符号:
符号	 描述
c	 格式化字符及其ASCII码
s	 格式化字符串
d	 格式化整数
u	 格式化无符号整型
o	 格式化无符号八进制数
x	 格式化无符号十六进制数
X	 格式化无符号十六进制数（大写）
f	 格式化浮点数字，可指定小数点后的精度
e	 用科学计数法格式化浮点数
E	 作用同%e，用科学计数法格式化浮点数
g	 %f和%e的简写
G	 %f 和 %E 的简写
p	 用十六进制数格式化变量的地址
'''

sStr = 'abcdef'
iStrLen = len(sStr)
print("The length of %s is %d" % (sStr, iStrLen))

fPI = 3.141592653
print('%10.3f' % fPI)  # 字段宽10，精度3

print('%010.3f' % fPI)  # 用0填充空白

print("PI = %.*f" % (3, fPI))  # 用*从后面的元组中读取字段宽度或精度

'''
格式化操作符辅助指令:
符号	    功能
*	    定义宽度或者小数点精度
-	    用做左对齐
+	    在正数前面显示加号( + )
<sp>	在正数前面显示空格
#	    在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0	    显示的数字前面填充'0'而不是默认的空格
%	    '%%'输出一个单一的'%'
(var)	映射变量(字典参数)
m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
'''

print('%-10.3f' % fPI)  # 左对齐
print('%+f' % fPI)  # 显示正负号

'''
格式化输出16进制，十进制，八进制整数
#%x --- hex 十六进制
#%d --- dec 十进制
#%o --- oct 八进制
'''

hHex = 0xFF
print("Hex = %x,Dec = %d,Oct = %o" % (hHex, hHex, hHex))

'''
格式：
开头部分：\033[显示方式;前景色;背景色m + 结尾部分：\033[0m

注意：
开头部分的三个参数：显示方式，前景色，背景色是可选参数，可以只写其中的某一个；
另外由于表示三个参数不同含义的数值都是唯一的没有重复的，所以三个参数的书写先后顺序没有固定要求，系统都能识别；
但是，建议按照默认的格式规范书写。
'''

'''
字体色     |       背景色     |      颜色描述
30        |        40       |       黑色
31        |        41       |       红色
32        |        42       |       绿色
33        |        43       |       黃色
34        |        44       |       蓝色
35        |        45       |       紫红色
36        |        46       |       青蓝色
37        |        47       |       白色
-------------------------------
显示方式     |      效果
0           |     终端默认设置
1           |     高亮显示
4           |     使用下划线
5           |     闪烁
7           |     反白显示
8           |     不可见

22           |     非粗体
24           |     非下划线
25           |     非闪烁
27           |     非反显
'''
print('This is a \033[1;35m Color \033[0m!')
print('This is a \033[1;32;43m Color \033[0m!')
print('\033[1;33;44mThis is a Color !\033[0m')
