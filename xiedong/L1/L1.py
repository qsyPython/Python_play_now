#目标：在控制台打印符合要求的数字，输出7个数字即可，不需要带颜色
#具体细节：1.红球区6个，闭区间1-33,蓝色球1个，闭区间1-16，一共7个
#         2.需要满足条件：①能够随机输出7个在区间内的数字，6个红球1个蓝球，6个红球不能重复，蓝球可以和前面有重复
#          例如：在控制台上输出结果：[1,3,5,17,26,33 5]
#         ②能够随机N注N倍，例如随机1注5倍，2注每注5倍
#          例如：在控制台输出结果：[1,3,5,17,26,33 5]*3
#         [1,5,8,15,20,26  9]*5
#         ③能够手动输入6个红球，1个蓝球，并且可以乘以倍数
#         例如：[1,5,8,15,20,26  9]*5
#         3.除了满足以上要求，还要能够做好边界检查，保证函数传入非法参数能够正常反应
#         例如：输入了不满足格式的，输入了非整数类型等等
#         4.会的多的可以用input，不会使用可以直接方法调用的形式，可传不同参数实现
#我会随机选6个组员来讲自己的代码，也可以让觉得自己写的好的来讲，作业检查和讲解的时间: 下次分享时（考虑下周放假，改为下下周4）
import random as rd

def input_is_random(msg):
    print(msg)
    is_random_input = input("请确定是否机选yes/no: ")
    if "yes" == is_random_input.rstrip().lstrip().lower():
        is_random = True
        input_bet_num(is_random)
    elif "no" == is_random_input.rstrip().lstrip().lower():
        is_random = False
        input_bet_num(is_random)
    else:
        input_is_random("输入的不对哦,请重新输入")

def input_bet_num(is_random):
    bet_num_input = input("请输入下注数目: ")
    try:
        bet_num = int(bet_num_input)
    except ValueError:
        print("输入的不对哦，请重新输入")
        input_bet_num(is_random)
    else:
        input_mutliple_num(is_random,bet_num)

def input_mutliple_num(is_random ,bet_num):
    mutliple_num_input = input("请输入下注倍数: ")
    try:
        mutliple_num = int(mutliple_num_input)
    except ValueError:
        print("输入的不对哦，请重新输入")
        input_mutliple_num(is_random,bet_num)
    else:
        if is_random :
            creat_random_lottery(bet_num,mutliple_num)
        else:
            creat_write_lottery(bet_num,mutliple_num)

def creat_random_lottery(bet_num,mutliple_num):
    rd_list = []
    while len(rd_list) < bet_num:
        random_list = list(range(1, 34))
        num_list = []
        while len(num_list)<6:
            v = rd.choice(random_list)
            random_list.remove(v)
            num_list.append(v)
        num_list.append(rd.randint(1,16))
        rd_list.append(num_list)
        print(num_list,"*",mutliple_num)


def creat_write_lottery(bet_num,mutliple_num):
    rd_list = []
    while len(rd_list)<bet_num:
        num_list = []
        while len(num_list)<6:
            num = input_correct_num(len(rd_list),num_list)
            num_list.append(num)
        blue_num = input_correct_num(len(rd_list),num_list)
        num_list.append(blue_num)
        rd_list.append(num_list)
    for l in rd_list:
        print(l,"*",mutliple_num)

def input_correct_num(mutliple,num_list):
    if len(num_list)<6:
        input_num = input("请输入第"+str(mutliple+1)+"注第"+str(len(num_list)+1)+"个红球号码:" )
        try:
            num = int(input_num)
        except ValueError:
            print("输入的不对哦，请重新输入")
            return input_correct_num(mutliple,num_list)
        else:
            if num in num_list or num>33 or num<1:
                print("请输入未输入过的1到33的整数")
                return input_correct_num(mutliple, num_list)
            else:
                return num
    else:
        input_num = input("请输入第" + str(mutliple+1) + "注蓝球号码:")
        try:
            num = int(input_num)
        except ValueError:
            print("输入的不对哦，请重新输入")
            return input_correct_num(mutliple, num_list)
        else:
            if num>16 or num <1:
                print("请输入1到16的整数")
                return input_correct_num(mutliple, num_list)
            else:
                return num

input_is_random("欢迎来到中国福利彩票")