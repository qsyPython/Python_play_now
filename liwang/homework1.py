# -*- coding: UTF-8 -*-

import random

# 随机生成红球并排序
def randRed():
    redBall=[]
    # 6个数字且在1-33之间
    while len(redBall)<6:
        randBall=random.randint(1,33)
        if (randBall in redBall)==False :
            redBall.append(randBall)
    # 排序
    redBall.sort()
    return redBall

# 随机生成蓝球
def randBlue():
    # 1个数字且在1-16之间
    blueBall=random.randint(1,16)
    return blueBall

# 红球获取自定义输入并排序
def customRedBall(userBall):
    is_ok=True
    userBall_list=userBall.split(',')
    # 判断输入长度
    if len(userBall_list)!=6:is_ok=False;
    # 判断是否有重复值
    cf = [i for i in userBall_list if userBall.count(i) > 1]
    if len(cf) > 0: is_ok = False;
    #判断是否为整数，并且在1-33之间
    for x in userBall_list:
        if x.isdigit()==False or int(x)>33 or int(x)<1:
            is_ok=False
    # 通过检查后排序
    if is_ok:
        userBall_list = userBall_list.sort()
        return userBall_list
    else:
        return False


# 蓝球获取自定义输入
def customBlueBall(userBall):
    # 判断是否为整数并且在1-16之间
    if int(userBall)<1 or int(userBall)>16:
        return False
    else:
        return userBall

# 定义变量
redBall_list=[] # 红球
blueBall_list=[] # 蓝球
num=1 # 方案注数,默认为1

# 获取键盘输入
is_rand = input("本期双色球投注方案是否全部随机生成？（y/n）")
if(is_rand=='y'):# 随机生成
    is_num =input("请输入随机注数：")
    if is_num.isdigit() and int(is_num)>0:
        num = int(is_num)
        for x in range(0,int(is_num)):
            print("红球：", randRed(), "蓝球：", randBlue(),"\n")
else:# 手动输入
    xcall=False
    while xcall==False:
        is_user_red=input("请输入红球方案(用英文逗号隔开)：")
        xcall=customRedBall(is_user_red)
    ycall=False
    while ycall==False:
        is_user_blue = input("请输入蓝球方案：")
        ycall=customBlueBall(is_user_blue)

is_double=input("请输入投注倍数：")
if is_double.isdigit():
    print("共花费",int(is_double)*2*num,"元")
