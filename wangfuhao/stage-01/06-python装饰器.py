def checkLogin(func):
    def inner():
        print("登录验证...")
        func()
    return inner

# 定义两个功能函数
@checkLogin
def fss():
    print("发说说")

# 语法糖 写法
@checkLogin
def ftp():
    print("发图片")

# 相关的逻辑代码
btnIndex = 1
if btnIndex == 1:
    fss()
else:
    ftp()


#装饰器的执行顺序
def zhuangshiqi_line(func):
    def inner():
        print("---------------------------")
        func()
    return inner


def zhuangshiqi_star(func):
    def inner():
        print("*" * 30)
        func()
    return inner

@zhuangshiqi_line # == print_content = zhuangshiqi_line(print_content)
@zhuangshiqi_star # == print_content =  zhuangshiqi_star(print_content)
def print_content():
    print("人狠话不多")

print_content()

#装饰器中参数可变
def zsq(func):
    def inner(*args, **kwargs):
        print("_" * 30)
        # print(args, kwargs)
        func(*args, **kwargs)
    return inner


@zsq
def pnum(num, num2, num3):
    print(num, num2, num3)

@zsq
def pnum2(num):
    print(num)


pnum(123, 222, num3=666)
pnum2(999)

#装饰器的类型必须和使用装饰器的函数类型一致
def zsq(func):
    def inner(*args, **kwargs):
        print("_" * 30)
        # print(args, kwargs)
        res = func(*args, **kwargs)
        return res
    return inner

@zsq
def pnum(num, num2, num3):
    print(num, num2, num3)
    return num + num2 + num3


@zsq
def pnum2(num):#类型与装饰器不符合,应为zsq有返回的类型,所以结果会是none
    print(num)

res1 = pnum(123, 222, num3=666)
res2 = pnum2(999)

print(res1, res2)

#获取装饰器,传参数
def getzsq(char):
    def zsq(func):
        def inner():
            print(char * 30)
            func()

        return inner
    return zsq

@getzsq("*")
def f1():
    print("666")

f1()