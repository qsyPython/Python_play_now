
# 第1期作业：双色球
# 目标：在控制台打印符合要求的数字，输出7个数字即可，不需要带颜色
# 具体细节：  1.红球区6个，闭区间1-33,蓝色球1个，闭区间1-16，一共7个
#           2.需要满足条件：①能够随机输出7个在区间内的数字，6个红球1个蓝球，6个红球不能重复，蓝球可以和前面有重复
#           例如：在控制台上输出结果：[1,3,5,17,26,33 5]
#           ②能够随机N注N倍，例如随机1注5倍，2注每注5倍
#           例如：在控制台输出结果：[1,3,5,17,26,33 5]*3
#           [1,5,8,15,20,26  9]*5
#           ③能够手动输入6个红球，1个蓝球，并且可以乘以倍数
#           例如：[1,5,8,15,20,26  9]*5
#           3.除了满足以上要求，还要能够做好边界检查，保证函数传入非法参数能够正常反应
#           例如：输入了不满足格式的，输入了非整数类型等等
#           4.会的多的可以用input，不会使用可以直接方法调用的形式，可传不同参数实现
#生成某区间内不重复的N个随机数的方法

import random

def DoubleBallControl():
    print('请按顺序输入6个红球1个篮球还有倍数：\n')
    tempNumber = 0
    inputList = [];
    for i in range(8):
        while True:
            if (i < 6):
                print("请输入第", i + 1, "个红球(1~33之间)，谢谢")
            elif (i == 6):
                print("请输入蓝球(1~16之间)，谢谢")
            else:
                print("请输入倍数，谢谢")
            tempNumber = input()
            if (tempNumber.isdigit()):
                countNum = int(tempNumber);
                if (i < 6):
                    if (countNum not in inputList) and (
                            countNum >= 1 and countNum <= 33):
                        inputList.append(countNum)
                        break
                    else:
                        print("您输入有误，请重新输入")
                elif (i == 6):
                    if (countNum >= 1 and countNum <= 16):
                        inputList.append(countNum)
                        break
                    else:
                        print("您输入有误，请重新输入")
                else:
                    inputList.append(countNum)
                    break
            else:
                print("请输入整数，谢谢")
    print(inputList[:7],'*',inputList[7])

def DoubleBallRandom(notenum,multiple):
    countRed = 6 #红球总数
    tempInt= 0  #临时数
    resultList = [] #存放的数组
    while(len(resultList)<countRed):
        tempInt = random.randint(1, 33)
        if(tempInt not in resultList):#判断随机数是否存在于这个数组
            resultList.append(tempInt)

    tempInt =random.randint(1, 16)
    resultList.append(tempInt) #随机添加一个篮球
    print('结果',resultList,'*',multiple)

print('请输入双色球随机生成的注数和倍数')
print('请输入注数：')
while True:
    noteNumber = input()
    if(noteNumber.isdigit()):
        break
    else:
        print("请输入整型数字，谢谢")

print('请输入倍数')
while True:
    multiple = input()
    if(multiple.isdigit()):
        break
    else:
        print("请输入整型数字，谢谢")

DoubleBallRandom(noteNumber,multiple)

print('\n\n\n')
#自主输入
DoubleBallControl()