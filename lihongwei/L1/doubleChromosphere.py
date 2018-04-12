#第1期作业：双色球
# 目标：在控制台打印符合要求的数字，输出7个数字即可，不需要带颜色
# 具体细节：1.红球区6个，闭区间1-33,蓝色球1个，闭区间1-16，一共7个
#           2.需要满足条件：①能够随机输出7个在区间内的数字，6个红球1个蓝球，6个红球不能重复，蓝球可以和前面有重复
#           例如：在控制台上输出结果：[1,3,5,17,26,33 5]
#           ②能够随机N注N倍，例如随机1注5倍，2注每注5倍
#           例如：在控制台输出结果：[1,3,5,17,26,33 5]*3
#           [1,5,8,15,20,26  9]*5
#           ③能够手动输入6个红球，1个蓝球，并且可以乘以倍数
#           例如：[1,5,8,15,20,26  9]*5
#           3.除了满足以上要求，还要能够做好边界检查，保证函数传入非法参数能够正常反应
#           例如：输入了不满足格式的，输入了非整数类型等等



import random

def DoubleChromosphereTask():

    random.randint(0,9) #制定随机数0到9

    doubleChromosphere = random.sample(range(1,34),6) #输出6个随机数，1到34

    doubleChromosphere.sort() #无返回值

    sorted(doubleChromosphere) #排序函数，不影响原数组，产生新排序后数据

    print('用以上的随机数做一个双色球')

    chromosphere = random.sample(range(1,34),6)

    print(chromosphere,random.randint(1,16))

DoubleChromosphereTask()

#1.红球区6个，闭区间1-33,蓝色球1个，闭区间1-16，一共7个

def hongwei(red,blue,arr = []):

    doubleChromosphere = random.randint(red,blue)

    if doubleChromosphere in arr:

        return hongwei(red,blue,arr)

    return doubleChromosphere


#输入倍数
def multiple():

    red = input('亲爱的，请输入倍数：')

    try:
        number = int(red)

        if number == 0:

            print('亲爱的，最少要输入一倍')

            return multiple()

        return number

    except:

        print('亲爱的，输入不正确')

        return multiple()

#输入注数
def noteTheNumberOf():

    red = input('亲爱的，请输入注数：')

    try:
        number = int(red)

        if number == 0:

            print('亲爱的，最少要输入一注')

            return noteTheNumberOf()

        return number

    except:

        print('亲爱的，输入不正确')

        return noteTheNumberOf()

#手动选
def manualSelection():

    red = noteTheNumberOf()

    blue = multiple()

    for random in range(red):

        str = []

        for i in range(7):

            if i == 6:

                str.append(aboutManyAr(1,17,random,i,str))

            else:

                str.append(aboutManyAr(1,34,random,i,str))

        print('手选',(random+1),'注号码为：',str,blue,'倍')


#随机数
def randomNumber():

    red = noteTheNumberOf()

    blue = multiple()

    for random in range(red):

        str = []

        for i in range(7):

            if i == 6:

                str.append(hongwei(1,16,[]))

            else:

                str.append(hongwei(1,33,str))

        print("随机",(random + 1),"注号码为：",str, blue,"倍")


def aboutManyAr(red,blue,random,i,arr=[]):

    print("输入第",(random+1),"注","第",(i+1),"个号码")

    boundary = input()

    try:
        number = int(boundary)

        if number in range(red,blue):

            if number in random:

                print('亲爱的，输入不能重复')

                return aboutManyAr(red,blue,random,i,arr)

            else:

                return number

        else:

            print('亲爱的，输入数字范围不对')

            return aboutManyAr(red,blue,random,i,arr)

    except:

            print('亲爱的，输入不合法')

            return aboutManyAr(red,blue,random,i,arr)

#启动控制台
def startDefaultConsole():

    boundary = input('www.不坑你坑谁.com，输入1 随机号，输入2 自选号')

    try:

        numbre = int(boundary)

        if numbre in range(1,3):

            if numbre == 1:

                print('将进行随机选')

                randomNumber()

            else:

                print('将进行自选')

                manualSelection()

        else:

            print('你是猪吗？输入的数字范围肯定不对')

            startDefaultConsole()

    except:

        print('你是不是傻，输入不合法了，程序要重新启动')

        startDefaultConsole()


startDefaultConsole()
