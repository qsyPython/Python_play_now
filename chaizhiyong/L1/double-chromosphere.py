import random
from colorSimplePattern import Colored

'''
目标：在控制台打印符合要求的数字，输出7个数字即可，不需要带颜色
具体细节：1.红球区6个，闭区间1-33,蓝色球1个，闭区间1-16，一共7个
          2.需要满足条件：①能够随机输出7个在区间内的数字，6个红球1个蓝球，6个红球不能重复，蓝球可以和前面有重复
          例如：在控制台上输出结果：[1,3,5,17,26,33 5]
          ②能够随机N注N倍，例如随机1注5倍，2注每注5倍 
          例如：在控制台输出结果：[1,3,5,17,26,33 5]*3
          [1,5,8,15,20,26  9]*5
          ③能够手动输入6个红球，1个蓝球，并且可以乘以倍数
          例如：[1,5,8,15,20,26  9]*5
          3.除了满足以上要求，还要能够做好边界检查，保证函数传入非法参数能够正常反应
          例如：输入了不满足格式的，输入了非整数类型等等
'''
'''
   检验手动输入红球规则
'''
def manual_select_red_ball_number(red_number_list):
    is_success = True
    manual_red_ball_list = red_number_list.split(' ')
    if len(manual_red_ball_list) != 6:
        is_success = False
        return is_success

    manual_red_ball_remove_repeat_list = set(manual_red_ball_list)
    if len(manual_red_ball_remove_repeat_list)  != len(manual_red_ball_list):
        is_success = False
        return is_success

    for red_ball in manual_red_ball_list:
        if red_ball.isdigit() == False or int(red_ball) < 1 or int(red_ball) > 33:
            is_success = False
            return is_success

    return is_success

'''
   检验手动输入蓝球规则
'''
def manual_select_blue_ball_number(blue_number):
    is_success = True
    if blue_number.isdigit() == False or int(blue_number) < 1 or int(blue_number) > 16:
         is_success = False
         return is_success

    return is_success

'''
  机选6个红球和1个蓝球
'''
def machine_select_number():
    machine_red_ball = random.sample(range(1,34),6)
    machine_blue_ball = random.randint(1,16)
    machine_red_ball.append(machine_blue_ball);
    return machine_red_ball

'''
  机选多注时将红球和蓝球存储规则
'''
def machine_select_bet_number(numberBet):

    machine_list_bet = []
    for i in  range(numberBet):
        machine_selected_numbers = machine_select_number()
        redBoll = machine_selected_numbers[0:6]
        blueBoll =  "[" + str(machine_selected_numbers[-1]) + "]"
        machine_sub_list_number = [] #将红球和蓝球放到一个列表
        machine_sub_list_number.append(redBoll)
        machine_sub_list_number.append(blueBoll)
        machine_list_bet.append(machine_sub_list_number )

    return machine_list_bet

'''
   购彩入口
'''
def buy_lottery():
    is_machine = input('机选还是手选(R/M):')
    if is_machine == "R":
        color = Colored()
        machine_select_number1 = machine_select_number()
        redBoll =  color.red(machine_select_number1[0:6])
        blueBoll =color.blue("[" + str(machine_select_number1[-1]) +"]")
        print("机选1注:"+ redBoll + blueBoll)

        while True:
           machine_bet = input('请输入投注数:')
           machine_multiple = input('请输入投注倍数:')
           try:
              machine_bet_list_number = machine_select_bet_number(int(machine_bet))
              for i, value in enumerate(machine_bet_list_number):
                 print("第{}注投{}倍:{}{}*{}".format(i + 1, int(machine_multiple), color.red(value[0]), color.blue(value[1]),
                                                int(machine_multiple)))
              break
           except ValueError as e:
                 print('请输入正确信息:\n', e)
                 continue
           except IndexError as e:
                 print('输入信息过少:\n', e)
                 continue
           except:
                 print('程序异常!\n')
                 continue

    elif is_machine == "M":
        is_red_success = False
        manual_red_ball = []
        while is_red_success == False:
            manual_red_ball = input('请输入区间1-33中不重复的6个红球,数字之间用空格分割(如1 2 3 5 6 31):')
            is_red_success = manual_select_red_ball_number(manual_red_ball)

        is_blue_success = False
        manual_blue_ball = ""
        while is_blue_success == False:
            manual_blue_ball = input('请输入区间1-36中1个蓝球,(如3):')
            is_blue_success = manual_select_blue_ball_number(manual_blue_ball)

        is_integer = False
        manual_multiple = ""
        while is_integer == False:
           manual_multiple = input('请输入投注倍数(如3):')
           if manual_multiple.isdigit():
               is_integer = True

        color = Colored()
        print("投注{}倍:{}{}*{}".format( manual_multiple, color.red("[" + manual_red_ball + "]"), color.blue("[" + manual_blue_ball + "]"),
                                      manual_multiple))

    else:
      print("else")

def main():
    print("中国福利彩票中心欢迎您")
    is_success = True
    while is_success == True:
       buy_Y_or_N = input("你如果购买彩票请输入Y否则输入N：")
       if buy_Y_or_N == "Y":
           buy_lottery();
       elif buy_Y_or_N == "N":
           print("game over")
       else:
           is_success = False

#主程序入口

main();
