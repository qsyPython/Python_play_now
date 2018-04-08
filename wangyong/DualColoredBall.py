import random


# 手动输入
def inputList():
    while True:
        redball = input("请输入6个红球：")
        mylist = redball.split(",")
        ballList = [];
        if len(mylist) == 6:
            if len(mylist) == len(set(mylist)):
                for num in mylist:
                    if num.isdigit() and int(num) > 0:
                        if int(num) in range(1, 33):
                            ballList.append(int(num))
                        else:
                            print("请输入1~33之间的数字")
                            break
                    else:
                        print("请输入整数")
                        break
                if len(ballList) == 6:
                    break
            else:
                print("请不要输入重复数字")
        else:
            print("输入有误，请重新输入")

    while True:
        input_blue = input("请输入1个蓝球：")
        if int(input_blue) in range(1, 16):
            multiple = input("请输入倍数:")
            if multiple.isdigit():
                ballList.append(int(input_blue))
                print(ballList, '*', multiple)
                break
            else:
                print("请输入整数")
        else:
            print("请输入1~16之间的数字")


# 随机生成
def ballRandom(multiple):
    ballList = []
    while len(ballList) < 6:
        randBall = random.randint(1, 33)
        if randBall not in ballList:
            ballList.append(randBall)

    randblue = random.randint(1, 16)
    ballList.append(randblue)
    print(ballList, '*', multiple)


while True:
    is_num = input("请输入随机注数：")
    if is_num.isdigit() and int(is_num) > 0:
        num = int(is_num)
        ballRandom(num)
        break
    else:
        print("输入有误，请重新输入")

inputList()
