print("==================python的注释")
#我是一个注释

"我也是一个注释"

'''
多行
注释
'''

"""
我也是
多行注释
"""

# _*_ coding:utf-8 _*_   解决python2.0中文支持的注释

print("==================python的变量")
#方式1:
a = 2
b = 3

#方式2
a1,b1 = 2, 3

#方式3
a2 = b2 = 3

print("==================python的数据类型")
print(6+6) #12
print("6" + "6") #66
#查看类型
print(type(6))
print(type("6"))

print("==================python的数据类型的转换")
a = "6"
# print(4+num) #会报错,类型不一致
print(4 + int(a))
print(str(4) + a)
#静态类型:类型是编译的时候确定的,后期无法修改
#动态类型:类型是运行时进行判定的, 可以动态修改

#强类型:类型比较强势, 不轻易随着环境的变化而变化 eg:  'a' + 1   会报错
#弱类型:类型比较柔弱, 不同的环境下, 很容易被改变 eg: 'a' + 1  输出a1
#结论:Python是属于, 强类型的, 动态类型的语言

print("==================python的算术运算符")
#加法运算符
print(1+2)
print("1"+"2")
print([1,2]+[3,4])

#减法运算符
print(4-12)

#乘法运算符
print(2 * 3)

#幂运算符
print(3 ** 5)

#除法运算符
print(5 / 2)
# print(5 / 0)  #会报错,被除数不能是0

#整除运算符
print(5.2 // 2)  #注意,结果不是四舍五入 ,只是直接取整数部分

#求模运算符
print(5 % 2)  #1  其实就是求余数

#优先级问题
print((1+2) * 3 / 4)

#整除求余的应用场景  九宫格的计算
#一个九宫格有4列,计算某个数字的位置
weizhi = 6  #计算6是几行几列
row = weizhi // 4
col = weizhi % 4

print("==================python的逻辑运算符")
b = True
# not 取反操作
print(not b)

#and 并且的意思  and 的两边 必须都是真 才能为真
print(True and  False)

#or or两边 一个为真就是真
print(True or False)

#bool 非0即真  非空即真
print(bool(1))
print(bool(0))
print(bool("")) #False

print("==================python的比较运算符")
print(10 > 2)
print(10 != 10)
print(10 == 10) #比较的是值

#is  比较唯一标识(即内存)
ten = 10
print(id(ten))

aa = 10
bb = 10
print(aa is bb) #True

aaa = [1]
bbb = [1]
print(aaa == bbb) #Ture
print(aaa is bbb) #Flase  内存空间是不一样的

#链式比较运算符
number = 10
print(5 < number < 20)

print("==================python复合运算符")
nn = 10
nn += 5
print(nn)

print(nn * 20)

print("==================python的输出")
#输出一个变量
num = 55
print(num)

#输出多个变量
num2 = 44
print(num,num2)

#格式化输出
name = 'wfh'
age = 18
print("我的名字是%s,年龄是%d"%(name,age))
print("我的名字是{0},年龄是{1}".format(name,age))

#输出到文件中
# f = open("text.txt","w")
# print("xxxxx",file=f)

#输出不自动换行
print("abc",end="")

#输出的各个数据,使用分隔符分割
print("1","2","3",sep="&&&")

#flush参数的说明:清空缓存,马上输出的控制台
print("请输入账号",end="",flush=True)

print("==================python的输入")
content = input("请输入内容: ")
result = eval(content)
print(type(result))
print(result)

