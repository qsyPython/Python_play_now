import random
import re

import array

ntroducei= "请输入以下任一数字进行双色球选号：1（单注）、2（N注N倍）、3（手动输入号码和N注N倍）：\n"

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

    l = True
    while True:
        message = input(ntroducei)
        while int(message) not in [1, 2, 3]:
            message = input("输入有误，请重新输入：\n")

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
            while l:
                message1 = input("请输入7个号码，中间用逗号隔开,并按回车键继续：\n")
                s = ""
                charArray = message1.split(",")
                flag = True;
                for arr in charArray:
                    i = int(arr)
                    if len(charArray) == 7 and arr == charArray[6]:
                        if i in range(1, 16):
                            continue
                        else:
                            flag = False
                            break
                    elif i in range(1, 33):
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    if len(charArray) != 7:
                        print("输入号码个数不对")
                    elif len(set(charArray)) < 7:
                        print("不能有相同号码")
                    else:
                        num = input("请输入注,并按回车键继续：\n")
                        num = int(num)
                        multiple = input("请输入倍,并按回车键继续：\n")
                        while num > 0:
                            num = num - 1
                            resutlstr2 = "[" + str(charArray[0]) + "," + str(charArray[1]) + "," + str(
                                charArray[2]) + "," + str(
                                charArray[3]) + "," + str(charArray[4]) + "," + str(charArray[5]) + " " + str(
                                charArray[6]) + "]" + "*" + multiple
                            print("您选择的号码是：\n"+resutlstr2)
                        l = False
                else:
                    print("输入号码非法")
        # if l == False:
        #     break


    # msg = input("是否继续？yes/no\n")
    # if msg == "yes":
    #     name = True
    # else:
    #     if msg == "no":
    #         name = False
    #     else:
    #         p = True
    #         while p:
    #             m =  input("输入有误，请重新输入:\n")
    #             if m == "yes" or m == "no":
    #                 p = False
    #                 if m == "no":
    #                     name = False







