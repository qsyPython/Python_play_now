

# 第1期作业：双色球
# 目标：在控制台打印符合要求的数字，输出7个数字即可，不需要带颜色
# 具体细节：1.红球区6个，闭区间1-33,蓝色球1个，闭区间1-16，一共7个
#           2.需要满足条件：①能够随机输出7个在区间内的数字，6个红球1个蓝球，6个红球不能重复，蓝球可以和前面有重复
#           例如：在控制台上输出结果：[1,3,5,17,26,33 5]
#           ②能够随机N注N倍，例如随机1注5倍，2注每注5倍
#           例如：在控制台输出结果：[1,3,5,17,26,33 5]*3
#           [1,5,8,15,20,26  9]*5
#           ③能够手动输入6个红球，1个蓝球，并且可以乘以倍数
#           例如：[1,5,8,15,20,26  9]*5
#           3.除了满足以上要求，还要能够做好边界检查，保证函数传入非法参数能够正常反应
#           例如：输入了不满足格式的，输入了非整数类型等等
#           4.会的多的可以用input，不会使用可以直接方法调用的形式，可传不同参数实现

import random


def union_lotto_test():
    flag = input("输入购买双色球选项 1/2/3 ：")
    if flag == "1":
        judge_one()
    if flag == "2":
        judge_two()
    if flag == "3":
        judge_input()

#选项1
def judge_one():
    print("①能够随机输出7个在区间内的数字，6个红球1个蓝球，6个红球不能重复，蓝球可以和前面有重复")
    red,blue = randint_red_and_blue()
    red_and_blue = [red,blue]
    print('输出双色球%s'%red_and_blue )

#选项2
def judge_two():
    print('②能够随机N注N倍')
    for i in range(0,random.randint(1,9)):
        multiple_num = random.randint(1,9)    #随机倍数
        red,blue = randint_red_and_blue()
        red_and_blue = [red,blue]
        print('N注N倍双色球%s'%red_and_blue+"*%d"%multiple_num)

# 判断输入的选项
def judge_input():

    inputName = input('输入红色球(用逗号隔开,)：').split(','or '，')
    inputlist = []
    if inputName.__len__() == 6:
        # 判断是否重复 和范围
        boo = judge_repetition(inputName)
        if boo:
            #判断是否是整数
            for i in range(0,inputName.__len__()):
                if inputName[i].isdigit():
                    inputlist.append(inputName[i])
                    if inputlist.__len__() == 6:
                        print("%s"%inputlist)
                        # 输入蓝色球
                        input_blue = input('输入蓝色球一个：').split(',' or '')
                        if  input_blue[0].isdigit():
                            if input_blue.__len__() == 1 and int(input_blue[0]) in range(0, 17):
                                red_and_blue_list = [inputlist, input_blue]
                                multiple = input("请输入倍数：")
                                print("%s" % red_and_blue_list + "*" + multiple)
                            else:
                                print('蓝色球输入错误请重新开始')
                else:print('请输入整数')

        else:
            print('输入的数据重复 或者是超出输入范围')
    else:
        print('必须输入六个数字')



def judge_repetition(testlist):
    only_list = []
    for i in range(0,testlist.__len__()):
        if  testlist[i].isdigit:
            if testlist[i] not in only_list and int(testlist[i]) in range(0,34):
                only_list.append(testlist[i])
                if only_list.__len__() == 6:
                    return True
            else:
                return False


def  randint_red_and_blue():
    # 红色球
    list_red_num = []
    while True:
        random_num = random.randint(1, 34)
        if random_num in list_red_num:
            continue
        elif list_red_num.__len__() == 0:
            list_red_num.append(random_num)
        elif random_num not in list_red_num:
            list_red_num.append(random_num)
        if list_red_num.__len__()== 6:
            break
    # 蓝色球
    random_blue_num = random.randint(1, 17)

    return list_red_num,random_blue_num


union_lotto_test()



