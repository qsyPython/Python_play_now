import random

while True:
    isRand = input("手选还是机选(s/r):")
    if isRand == 's' or isRand == 'r':
        break
    else:
        print("输入有误,请重新输入")

while True:
    number = input("您需要购买几注双色球:")
    if number.isdigit():
        break
    else:
        print("输入有误,请输入数字")
while True:
    beishu = input("请输入投注的倍数:")
    if beishu.isdigit():
        break
    else:
        print("输入有误,请输入数字")

totalArray = []

for i in range(1,int(number)+1):#购买几注
    numbers = []
    dicNumber = {}
    j = 1
    while j < 7:#生成红球
        if isRand == "r":
            redBall = random.randint(0,34)
            if  redBall in numbers:
                continue
            else:
                numbers.append(redBall)
                j += 1
        else:
            redBall = input("请输入第%d注第%d个红球的号码(1-33之间):" % (i, j))
            if  redBall in numbers:
                print("您输入有重复")
                continue
            elif redBall.isdigit() and int(redBall) > 0 and int(redBall) < 34:
                j += 1
                numbers.append(redBall)
            else:
                print("您输入的有误")
                continue

    while True:#生成蓝球
        if isRand == "r":
            blueBall = random.randint(0,17)
            dicNumber = {"red": numbers, "blue": blueBall}
            break
        else:
            blueBall = input("请输入蓝色球的号码:")
            if blueBall.isdigit() and int(blueBall) > 0 and int(blueBall) < 17:
                dicNumber = {"red" : numbers,"blue" : blueBall}
                break
            else:
                print("您输入的有误")
                continue

    totalArray.append(dicNumber)

for i in totalArray:
    print("{0} * {1}".format(i["red"],i["blue"]))



