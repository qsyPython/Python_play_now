print("------------------------函数的参数-------------------------------")
#多个参数
def sum(num1,num2):
    print(num1+num2)

sum(4,5)

#不定长参数  方式1: 加*号 传过来的是个元祖
def mySum(*t):
    print(t,type(t))
    result = 0
    for v in t:
        print(v)
        result += v
    print(result)

mySum(1,2,3,100)

#不定长参数  方式2: 加**号 传递参数的时候可以指定一个关键字
def mySum1(**k):
    print(k,type(k))
mySum1(name="wfh",age = 18)

#不定长参数 参数的拆包和装包
def mySum2(a, b, c, d):
    print(a + b + c + d)

def test(*args):
    print(args)

    # 拆包
    print(*args)
    #拆包进行调用
    mySum2(*args)

test(1, 2, 3, 4)#这一句其实相当于装包

#不定长参数,拆包装包方式2
def mySum4(a,b):
     print(a)
     print(b)

def test1(**kwargs):
    print(kwargs)

    # 拆包操作
    # 应该使用 ** 进行拆包操作
    # print(**kwargs)
    # a=1, b=2
    mySum4(**kwargs)
    # mySum(a=1, b=2)

test1(a=1, b=2)

#不定长参数-缺省参数
def hit(somebody="豆豆"):
    print("我想打", somebody)
hit("zhangsan")
hit()

#函数的注意事项
#注意,python中所有的传递都是地址传递
def change(num):
    print(id(num))
    # print(num)
    num = 666 #因为num是不可变的,系统会自动开辟一个空间,去存储,可以打印下前后的地址看下就明白了
    print(id(num))


b = 10
print(id(b))#相当于打印地址
change(b)
print(b)


def change1(num):
    print(id(num))
    num.append(666)
    print(id(num))


b = [1, 2, 3]
print(id(b))
change1(b)
print(b)


print("------------------------函数的返回值-------------------------------")
#直接函数内加return就行了
def caculate(a, b=1):
    """
    计算两个数据的和, 以及差
    :param a: 数值1, 数值类型, 不可选, 没有默认值
    :param b: 数值2, 数值类型, 可选, 默认值: 1
    :return: 返回的是计算的结果, 元组 : (和, 差)
    """
    he = a + b
    cha = a - b
    return (he, cha)

res = caculate(6, 7)
print(res)
he, cha = caculate(6, 7)
print(he)
print(cha)

print("------------------------偏函数-------------------------------")
#自己的理解就是偏爱的喜欢某个值,比如函数可以指定默认参数,在调用的时候可以不传递某个值
#但有的场景下想更换
#这时我们就可以使用偏函数对于这个默认值就行修改成自己喜欢的
def test(a, b, c, d=1):
    print(a + b + c + d)

import functools
newFunc = functools.partial(test, c=5)#修改了test函数的c的默认值是5
print(newFunc, type(newFunc))

newFunc(1, 2)

print("------------------------高阶函数-------------------------------")
#函数中的一个参数是函数,就是高阶函数,例如系统提供的sort函数
l = [{"name": "fh", "age": 18}, {"name": "fh1", "age": 19}, {"name": "fh2", "age": 18.5}]

def getKey(x):
    return x["name"]

result = sorted(l, key=getKey)
print(result)

#实现一个高阶函数
def caculate(num1, num2, caculateFunc):
    result = caculateFunc(num1, num2)
    print(result)

def sum(a, b):
    return  a + b

def jianfa(a, b):
    return  a - b

caculate(6, 2, jianfa)

print("------------------------返回函数-------------------------------")
#函数内部也可以返回函数
def getFunc(flag):
    # 1. 再次定义几个函数
    def sum(a, b, c):
        return a + b + c
    def jian(a, b, c):
        return a - b - c

    # 2. 根据不同的flag值, 来返回不同的操作函数
    if flag == "+":
        return sum
    elif flag == "-":
        return jian



result = getFunc("-")
# print(result, type(result))
res = result(1, 3, 5)
print(res)

print("------------------------匿名函数-------------------------------")

result = (lambda x, y : x + y)(1, 2)
print(result)

newFunc = lambda x, y : x + y
print(newFunc(4, 5))



l = [{"name": "sz", "age": 18}, {"name": "sz2", "age": 19}, {"name": "sz3", "age": 18.5}]

# def getKey(x):
#     return x["name"]

# result = sorted(l, key=getKey)
result = sorted(l, key=lambda x: x["age"])
print(result)


print("------------------------闭包-------------------------------")
#这就是一个简单的闭包
def test():
    a = 10
    def test2():
        print(a)

    return test2

newFunc = test()
newFunc()

#闭包案例,动态打印"-"的个数和----中间的文字
def line_config(content, length):
    def line():
        print("-"*(length // 2) + content + "-"*(length // 2)) #   //是整除运算符
    return line

line1 =  line_config("闭包", 40)
line1()
line1()
line1()
line1()

line2 = line_config("xxxx", 80)
line2()
line2()
line2()

#闭包的注意事项,如果用到外边的变量 需要加nonlocal
def test():
    num = 10
    def test2():
        nonlocal num
        num = 666
        # print(a)
        print(num)

    print(num)
    test2()
    print(num)

    return test2

result = test()

result()

#闭包的注意事项2:
def test():
    funcs = []
    for i in range(1, 4):
        def test2():
            print(i)
        funcs.append(test2)
    return funcs

newFuncs = test()

print(newFuncs)

newFuncs[0]()#3
newFuncs[1]()#3
newFuncs[2]()#3

#如果上述例子想打印1 2 3 则需要这样改造

def test():
    funcs = []
    for i in range(1, 4):
        def test2(num):
            def inner():
                print(num)
            return inner
        funcs.append(test2(i))
    return funcs

newFuncs = test()

print(newFuncs)

newFuncs[0]()
newFuncs[1]()
newFuncs[2]()

