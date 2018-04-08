print("====================数值,进制的转换")
#进制
'''
二进制:0b
八进制:0/0o
十六进制:0x
'''

'''
二转十
1101
1*2^3 + 1*2^2 + 0*2^1 + 1*2^0  
8        4       0       1  = 13 
'''
print(0b1101)
'''
八转十
34
3*8^1 + 4*8^0  
4       24       4  = 28 
'''
print(0o34)

'''
十转其他进制
整除倒取余数
十转二
18/ 2 = 9 余 0
9/2 = 4 余 1
4/2 = 2 余 0
2/2 = 1 余 0
从最后一个结果开始取,就是10010
'''
print(bin(18))#0b10010

'''
十转其他进制
整除倒取余数
十转8
18/ 8 = 2 余 2
从最后一个结果开始取,就是22
'''
print(oct(18))#0o22
#十转16
print(hex(18))#12

'''
二转八
整合3位为一位
10010

010 010
2    2
'''

'''
二转十六
整合4位为一位
10010

0001 0010
1     2
'''
print("====================数学函数")
#内建函数
# 绝对值
print(abs(-10))
#最大值
print(max(1,2,3,4,5))
#最小值
print(min(1,12,3,5))

print(min([1,3,5,2]))

#四舍五入
#round[,n] n表示保留几位小数,可以省略
print(round(3.14,2))#这个2就是保留2位小数

#pow(x,y) 返回x的y次幂 相当于**
print(pow(2,4))
print(2 ** 4)

#math模块函数
#导入模块
import math
#上取整
print(math.ceil(3.4))
#下取整
print(math.floor(3.8))
#开平方
print(math.sqrt(16))
#求对数
math.log(10000,10)  #10的多少次方等于10000

#随机函数
import random
#random [0,1)
print(random.random())

#choice 从序列中,随机挑选一个数值
print(random.choice([1,3,4,5,7,8]))

#uniform(x,y)   [x,y]范围内的随机小数
print(random.uniform(1, 3))

#randint(x,y) [x,y]范围内的随机整数
print(random.randint(1,3))

#randrange(star,stop,step) [start,stop) 第三个参数是步长的意思  randint,不包含结束点  相当于半开半闭 [)
print(random.randrange(1,4,2))  #步长的意思,从1开始,每次随机产生的数是在1的基础上加上步长 eg: 能随机出 1 3

#三角函数
'''
sin(x) 正弦  
cos(x) 余弦
tan(x) 正切
asin(x) 反正弦
acos(x) 反余弦
atan(x) 反正切
degress(x) 弧度 -> 角度
radians(x) 角度 -> 弧度

pi  3.14.....
'''
#sin(x) x,参数 所接收的是一个弧度  要转弧度
#例如  30度 ->弧度   30 /180 * pi
print(math.sin(30 / 180 * math.pi))
print(math.sin(math.radians(30)))

print("====================bool")
#bool
print(True + 2) #3
print(False + 2) #2

#前边一个类型是不是后边类型的子类
result = issubclass(bool,int)
print(result) #0

#if True:
 #   print("这里是真的")

#while True:
#    print("xx")

print("====================字符串")
#字符串
str1 = 'aaa'
print(str1,type(str1))

str1 = "abc"
print(str1,type(str1))

str1 = '''111'''
print(str1,type(str1))

str1 = """222"""
print(str1,type(str1))

str1 = """a\taa"""
print(str1, type(str1))

#转意符
print("我是\"wfh\"")
#或者
print('wo shi "wfh" ')

#原始字符串 前边加r即可
print(r"hello \n world") #hello \n world

result = ("he"
          "zi")
print(result)

result = """
nishi shui
ni buyong guan 
"""
print(result)

#"----------------------字符串拼接------------------------------")
#方式1
result = "wfh" + "fh"
print(result)#wfhfh

#方式2
result = "wangfh"      "fh"
print("我是%s"%(result))#我是wangfhfh

#方式3
restult = "我是%s,%d"%("123",123)
print(restult)

#方式4 字符串的乘法
print("fh\t"*10)

#"----------------------字符串切片操作------------------------------")
name  = "0123456"
print(name)#0123456
print(name[3])#3
# print(name[7])#错误 下标越界
print(name[-4])#倒着数 3

print(name[::])#默认是0 步长是1  0123456
print(len(name))#7

#name[起始:结束:步长]  步长小于0 从右往左
print(name[0:len(name):-1])#不能从头部跳到尾部, 或者从尾部跳到头部

print(name[0:2])# 0 1

#获取范围[起始,结束) 起始包含,结束不包含
print(name[0:len(name):-1])#不能从头部跳到尾部, 或者从尾部跳到头部  错误的情况

print(name[::-1])#字符串反转  6543210
print(name[4:1:-1])  #从第四个位置,朝第一个位置,往左移动#432
print(name[-1:4:-1])# 起始位置-1  就已经定位到最后了  步长小于0  从右到左   65

#"----------------------字符串函数操作------------------------------")
