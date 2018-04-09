#双色球
#功能需求：
# 1.红球区6个，闭区间1-33,蓝色球1个，闭区间1-16，一共7个
# 2.需要满足条件：①能够随机输出7个在区间内的数字，6个红球1个蓝球，6个红球不能重复，蓝球可以和前面有重复
# 例如：在控制台上输出结果：[1,3,5,17,26,33 5]
# ②能够随机N注N倍，例如随机1注5倍，2注每注5倍
# 例如：在控制台输出结果：[1,3,5,17,26,33 5]*5
# [1,5,8,15,20,26  9]*5
# ③能够手动输入6个红球，1个蓝球，并且可以乘以倍数
# 例如：[1,5,8,15,20,26  9]*5
# 3.除了满足以上要求，还要能够做好边界检查，保证函数传入非法参数能够正常反应
# 例如：输入了不满足格式的，输入了非整数类型等等
# 4.会的多的可以用input，不会使用可以直接方法调用的形式，可传不同参数实现

import  random

# 定义带范围的随机数生成器，传入数组，生成所需数字号码，满足需求一。
# x 为左边界， y 为 右边界，m为数组
def wlfRandom(x,y,m = []):
    w = random.randint(x,y)#定义一个函数，递归循环判断，产生不重复函数
    if w in m:
        return  wlfRandom(x,y,m)
    return  w

# 输入购买注数
def wlfZuNum():
    x = input("请输入购买的注数：")
    try:
        num = int(x)
        if num == 0:
            print("购买至少一注，请重新输入")
            return wlfZuNum()
        return num
    except:
        print("输入不合法，请重新输入")
        return wlfZuNum()

# 输入购买倍数
def wlfBeiNum():
    x = input("请输入购买的倍数：")
    try:
        num = int(x)
        if num == 0:
            print("购买至少一倍，请重新输入")
            return wlfBeiNum()
        return num
    except:
        print("输入不合法，请重新输入")
        return wlfBeiNum()
# 产生机选
def wlfJxNumber():
    x = wlfZuNum()
    y = wlfBeiNum()
    for t in range(x):
        strArr = []
        for i in range(7):
            if i == 6:
                strArr.append(wlfRandom(1,16,[]))
            else:
                strArr.append(wlfRandom(1,33,strArr))
        print("机选",(t+1),"注号码为：----\t",strArr,y,"倍")

# 输入 x 左边界，y 右边界，i 第几个，m数组
def wlfsetNumBySelf(x,y,t,i,m = []):
    print("请输入第",(t+1),"注","第",(i+1),"个号码")
    suggest = input()
    try:
        num = int(suggest)
        if num in range(x, y):
            if num in m:
                print("输入号码不能重复，请重新输入！")
                return  wlfsetNumBySelf(x,y,t,i,m)
            else:
                return num
        else:
            print("输入的数字范围不对，请重新输入！")
            return wlfsetNumBySelf(x,y,t,i,m)

    except:
        print("输入不合法，请重新输入！")
        return wlfsetNumBySelf(x,y,t,i,m)


# 产生人选
def wlfRxNumber():
    x = wlfZuNum()
    y = wlfBeiNum()
    for t in range(x):
        strArr = []
        for i in range(7):
            if i == 6:
                strArr.append(wlfsetNumBySelf(1,17,t,i,strArr))
            else:
                strArr.append(wlfsetNumBySelf(1,34,t,i,strArr))
        print("人选", (t + 1), "注号码为：----\t", strArr, y, "倍")


# 开始函数,启动控制台输入
def selectMath():
    suggest = input("欢迎来到双色球，输入1 机选号码，输入2 自选号码")
    try:
        num = int(suggest)
        if num in range(1,3):
            if num == 1:
                    print("下面将进行机选")
                    wlfJxNumber()
            else:
                    print("下面将进行人工选择")
                    wlfRxNumber()
        else:
            print("数字范围不对")
            selectMath()

    except:
        print("输入不合法，程序异常，程序将重新运行")
        selectMath()

# 启动程序
selectMath()




