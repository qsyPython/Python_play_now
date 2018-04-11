import random
import re

import array

ntroducei= "请输入以下任一数字进行双色球选号：1（单注）、2（N注N倍）、3（手动输入号码和N注N倍）："

# 随机生成7位数字，输出格式：[1,3,5,17,26,33 5]
def sevenNum ():
    numLists = []
    point = 0
    while point < 33:
        point = point + 1
        numLists.append(point)
    # 从numLists中，随机获取6个元素，生成一个新序列
    pLists = random.sample(numLists, 6)

    resutlstr = "["+ str(pLists[0])+ "," +str(pLists[1])+ ","+ str(pLists[2])+ ","+ str(pLists[3])+ ","+ str(pLists[4])+ ","+ str(pLists[5])+ " "+ str(random.randint(1, 16)) +"]"
    return resutlstr




name = True
while name:
    message = input(ntroducei)
    message = int(message)
    if message == 1:
        print(sevenNum())
    elif message == 2:
        pstr = ""
        nrandom = random.randint(1, 5)
        while nrandom > 0:
            nrandom = nrandom - 1
            pstr = sevenNum() + "*" + str(random.randint(1, 5))
            print(pstr)
    elif message == 3:
        message1 = input("请输入7个号码，中间用逗号隔开,并按回车键继续：")
        while True :
            s = ""
            charArray = array.array(',', message1)
            for arr in charArray:
                if int (charArray):
                range(1, 33)


            if m:
                print("true")
            # for a in charArray:
            #     m = pattern.match(pattern)
            #     if  m:
            #         s = s+ m
            #     else :
            #         message1 =  input("输入格式有误，请重新输入：")
            #         s = ""
            #         break;
            # if s:
            #     message2 = input("请输入倍数（1-5）,并按回车键继续：")
            #     pattern = re.compile("[1-5]")
            #     m = pattern.match(pattern)
            #     if m:
            #         s = s + + "*" + m
            #     else:
            #         message1 = input("输入格式有误，请重新输入：")
            #
            #
            # message = input("您投注的号码是:" + message1 + message2)








    else:
        m = input(ntroducei)
        if m !=1 and m !=2 and m !=3:
            name = False


    msg = input("是否继续？yes/no\n")
    if msg == "yes":
        name = True
    else:
        if msg == "no":
            name = False
        else:
            p = True
            while p:
                m =  input("输入有误，请重新输入:\n")
                if m == "yes" or m == "no":
                    p = False
                    if m == "no":
                        name = False







