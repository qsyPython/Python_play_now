for i in range(1,11):
    if i == 6:
        continue
    print(i)



#如何同时输入两个数字
#python中&&和||如何使用
#q怎么判断?直接==?

while True:
    num1 = input("请输入第一个数值:")
    num1 = float(num1)
    num2 = input("请输入第二个数值:")
    num2 = float(num2)

    if num1 > 100 or num2 > 100:
        print("输入的数据有问题,请重新输入")
        continue

    print("你计算的结果是:",num1 + num2)

    isQ = input("输入Q退出,其他键继续")
    if isQ == 'q':
        break