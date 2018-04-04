import random

#1.准备数据
num = random.randint(1,500)
count = 0

while True:
    #2.数据处理
    count += 1
    #2.1 让用户输入一个结果
    result = input("请输入结果")
    result = int(result)

    if result == num:
        print("恭喜你,猜对了,答案是%d,猜了%d次"%(num,count))
        break
    if result > num:
        print("你猜的数字, 太大了, 应该小一点")
    else:
        print("你猜的数字, 太小了, 应该大一点")