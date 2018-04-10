print("===================分支")
age = 17
if age > 18:
    print("您已经成年,可以上网")
else:
    print("未成年,快回家")

print("===================分支练习")
score = 100
if 90 <= score <= 100:
    print("优秀")
elif 80 <= score < 90:
    print("良好")
elif 60 <= score <80:
    print("及格")
elif 0 <= score < 60:
    print("不及格")
else:
    print("未知成绩")

print("===================while循环")
#打印十遍 社会我豪哥,人狠话不多
count = 10
while count > 0:
    print("社会我豪哥,人狠话不多")
    count -= 1

print("===================while练习")
number = 0
result = 0
while number < 100:
    number += 1
    result += number
print(result)

print("===================for循环")
notice = "社会我豪哥,人狠话不多"
for c in notice:
    print(c)

pets = ["小花","小黑","小红"]
for name in pets:
    print(name)

print("===================for反转字符串")
info = "社会我豪哥,人狠话不多"
result1 = ""
for c in info:
    result1 = c + result1
print(result1)

print("===================for练习")
#打印1-100之间的偶数
#  [1,100)  range是半开半闭区间
for i in range(1,101):
    if i % 2 == 0:
        print(i)

print("===================循环打断break")
for i in range(1,11):
    if i == 6:
        break
    print(i) # 1,2 3,4,5
print("===================循环打断continue")
for i in range(1,11):
    if i == 6:
        continue
    print(i) # 1,2 3,4,5,7,8,9,10

print("===================循环打断continue练习")
while True:
    num1 = 22
    num2 = 33

    if num1 > 100 or num2 > 100:
        print("你输入的数据有问题, 请重新输入")
        continue


    # 2. 计算两个数值的和
    result = num1 + num2

    # 3. 输出数值
    print("你计算的结果是:", result)
    break

print("===================99乘法表")
for num in range(1, 10):
    # 1. 造一个集合
    nums = range(1, num + 1)
    # 2. 遍历这个集合
    for n in nums:
        print("%d * %d = %d" % (n, num, n * num), end="\t")
    print("")

print("===================pass语句")
#在不知道具体的逻辑写什么时,使用pass,保持程序的完整性
age = 18
if age > 18:
    pass
else:
    pass

print("===================案例: 水仙花数")
num = 153
if not (100 <= num <= 999):
    print("你输入的数据无效, 直接退出程序")
    exit()

# 2.1 分解数值 -> 百位, 十位, 个位
# 123 = 1, 2, 3
baiwei = num // 100
shiwei = num % 100 // 10
gewei = num % 10

# 2.2 直接套入公式, 判定,是否是水仙花数
result = (baiwei ** 3 + shiwei ** 3 + gewei ** 3 == num)

# 3. 打印结果
# 直接打印, 判定好的结果
if result:
    print("%d, 是水仙花数" % num)
else:
    print("%d, 不是水仙花数" % num)

print("===================案例: 猜数字")
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