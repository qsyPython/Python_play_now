#bool
print(False + 2) #2

#前边一个类型是不是后边类型的子类
result = issubclass(bool,int)
print(result) #0

#if True:
 #   print("这里是真的")

#while True:
#    print("xx")

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


result = "wfh" + "fh"
print(result)#wfhfh

result = "wangfh"      "fh"
print("111%s"%(result))#111wangfhfh

restult = "我是%s,%d"%("123",123)
print(restult)

print("fh\t"*10)

# ----------------------字符串切片操作------------------------------
print("----------------------字符串切片操作------------------------------")
name  = "abcdefg"
print(name[3])#d
print(name)#abcdefg
print(name[-4])#倒着数 d

print(name[::])#默认是0 步长是1   abcdefg
print(len(name))#7

#name[起始:结束:步长]  步长小于0 从右往左
print(name[0:len(name):-1])#不能从头部跳到尾部, 或者从尾部跳到头部

print(name[::-1])#字符串反转
print(name[4:1:-1])  #从第四个位置,朝第一个位置,往左移动#edc
print(name[-1:4:-1])#步长小于0  从右到左   gf