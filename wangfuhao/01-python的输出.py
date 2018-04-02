#我是一个注释

"我也是一个注释"

#输出一个变量
num = 55
print(num)

num2 = 44
print(num,num2)

#格式化输出
name = 'wfh'
age = 18
print("我的名字是%s,年龄是%d"%(name,age))
print("我的名字是{0},年龄是{1}".format(name,age))

#输出不自动换行
print("abc",end="")

#输出的各个数据,使用分隔符分割
print("1","2","3",sep="&&&")

#flush参数的说明
print("请输入账号",end="",flush=True)


#python的输入
content = input("请输入内容: ")
result = eval(content)
print(type(result))
print(result)

