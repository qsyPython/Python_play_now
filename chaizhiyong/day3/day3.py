#while else
# count = 0
# while count < 5:
#     print("{} is less 5".format(count))
#     count += 1
# else:
#     print("is not less 5")
# #printif 奇葩语句
# num = 5
# print("小二" if num > 6 else "world")
#
# #num if
# x = 10
# num = 10 if x > 1 else 20
# print(num)

# import  random
#
# num = random.randrange(1,100,13)
# print(num)
#
# num = random.sample(range(1,100),3)
# print(num)
#
# num = random.randint(1,100)
# print("输了" if num < 80 else "赢了")
#
# #判断回文数
# num = eval(input("输入三位整数"))
# if(num//100 > 0  and num//100 < 10):
#     print("是三位数")
# else:
#     print("不是三位数")
# import time
# import os
# while -1:
#     os.system("start notepad")
#     time.sleep(2)  #挂起

# password=input("请输入密码")
# while "123456" != password:
#     password = input("密码错误，请重新输入")
# else:
# print("密码正确")

#按行显示
count = 1
for i in range(1,1000+1):
    if i%5 == 0 and i % 6 == 0:
        print(i,end="  ")
        if count%12 == 0:
            print("")
        count +=1

#围棋棋盘
# import turtle
# turtle.showturtle()
#
# step = 20
# for i in range(11):
#     turtle.penup()
#     turtle.goto(0,step*i)
#     turtle.pendown()
#     turtle.forward(step*10)
#
# turtle.right(270)
#
# for i in range(11):
#     turtle.penup()
#     turtle.goto(step*i,0)
#     turtle.pendown()
#     turtle.forward(step*10)
#
# turtle.dot(30,"black")
#
# turtle.done()

import turtle
turtle.showturtle()

turtle.penup()

step = 20
turtle.begin_fill()
for k in range(4):
    turtle.forward(step)
    turtle.right(90)

turtle.end_fill()
turtle.pendown()

turtle.done()