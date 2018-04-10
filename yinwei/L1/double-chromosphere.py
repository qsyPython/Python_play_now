#!/usr/bin/python
# -*- coding: UTF-8 -*-
#双色球
# 目标：在控制台打印符合要求的数字，输出7个数字即可，不需要带颜色
# 具体细节：
# 1.红球区6个，闭区间1-33,蓝色球1个，闭区间1-16，一共7个
# 2.需要满足条件：①能够随机输出7个在区间内的数字，6个红球1个蓝球，6个红球不能重复，蓝球可以和前面有重复
# 例如：在控制台上输出结果：[1,3,5,17,26,33 5]
# ②能够随机N注N倍，例如随机1注5倍，2注每注5倍
# 例如：在控制台输出结果：[1,3,5,17,26,33 5]*3
# [1,5,8,15,20,26  9]*5
# ③能够手动输入6个红球，1个蓝球，并且可以乘以倍数
# 例如：[1,5,8,15,20,26  9]*5
# 3.除了满足以上要求，还要能够做好边界检查，保证函数传入非法参数能够正常反应
# 例如：输入了不满足格式的，输入了非整数类型等等
# 4.会的多的可以用input，不会使用可以直接方法调用的形式，可传不同参数实现

import re
import random

print('这是一个双色球游戏')
print('输入1代表的是机器出现双色球号码')
print('输入2代表的是自己输入双色球号码')
# number = input('请输入:')

def outputNumber():
    index = 0
    listNumber = []
    while index <6:
        index+=1
        listNumber.append(random.randint(1,33))
    listNumber = list(set(listNumber))

    if len(listNumber) == 6:
        listNumber.append(random.randint(1, 16))
    else:
        listNumber.append(random.randint(1, 33))
        listNumber.append(random.randint(1,16))
    print('本期双色球为：',listNumber,'随机',random.randint(1,100),'注',random.randint(1,100),'倍')

def inputNumber():
    iList = []
    while True:
        iList.append(int(input('请输入你心中的红色球：')))
        iList = list(set(iList))
        if len(iList) == 6:
            iList.append(int(input('请输入篮色球:')))
            if len(iList)==7:
                num = int(input('请输入您要加注的倍数:'))
                print('您的双色球号码是:', iList,'倍数:',num)
                break
        else:
            print(' 请继续输入')

num = 10
while num > 0:
    number = input('请输入数字1或者数字2:')
    num = num - 1
    if not re.findall('^[0-9]+$', number):
        number = input('输入的内容只能是数字，请重新输入：')
    if number == None:
        print('请输入内容')
    if float(number) == 1:
        outputNumber()#调用函数
        break
    elif float(number) == 2:
        inputNumber()
        break
    else:
        continue
print('游戏结束！')

