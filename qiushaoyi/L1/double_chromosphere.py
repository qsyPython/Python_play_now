'''
	作者：邱少一
	日期：2018/4/3
	功能：
	第一期作业：双色球
    目标：在控制台打印符合要求的数字，输出7个数字即可，不需要带颜色
    具体细节：1.红球区6个，区间1-33,蓝色球1个，区间1-16，一共7个
            2.需要满足条件：①能够随机输出7个在区间内的数字，6个红球1个蓝球，6个红球不能重复，蓝球可以和前面有重复
                          例如：在控制台上输出结果：[1,3,5,17,26,33 5]
                          ②能够随机N注N倍，例如随机1注5倍，2注每注5倍
                          例如：在控制台输出结果：[1,3,5,17,26,33 5]*3
                                                  [1,5,8,15,20,26  9]*5
                          ③能够手动输入6个红球，1个蓝球，并且可以乘以倍数
                          例如：[1,5,8,15,20,26  9]*5
            3.除了满足以上要求，还要能够做好边界检查，保证函数传入非法参数能够正常反应
            例如：输入了不满足格式的，输入了非整数类型等等
            4.会的多的可以用input，不会使用可以直接方法调用的形式，传不同参数实现就好
    完成后由组长抽查，随机选6个人来讲自己的代码，也可以让觉得自己写的好的来讲
'''
# /usr/bin/env python
# -*- coding: utf-8 -*-

import random,logging

def random_choose_number():
    '''
    	 机选1注：6红1蓝
    '''
    random_red_ball = random.sample(range(1,34),6)
    random_blue_ball = random.randint(1,16)
    random_list_oneMultiple = []
    for red_ball in random_red_ball:
        random_list_oneMultiple.append(red_ball)
    random_list_oneMultiple.append(random_blue_ball)
    return random_list_oneMultiple

def random_choose_bet_multiple(bet):
    '''
         机选n注1倍数
    '''
    random_list_nBet = []
    for i in range(bet):
        random_list_one_multiple = random_choose_number()
        random_list_nBet.append(random_list_one_multiple)
    return random_list_nBet

def manual_choose_number(blue_number,*red_number):
    '''
             手选1注：6红1蓝
    '''
    manual_list_oneMultiple = []
    for i in red_number:
        if i>0 and i<34:
            manual_list_oneMultiple.append(i)
    if blue_number>0 and blue_number <17:
        manual_list_oneMultiple.append(blue_number)
    return manual_list_oneMultiple

def main():
    '''
    	 主函数
    '''
    y_or_n = input('彩票 买不买(y/n):')
    while y_or_n != 'n':
       is_random = input('机选还是手选(r/m):')
       if is_random == 'r':
           random_list_oneMultiple = random_choose_number()
           print('机选1注:\033[1;31;0m', random_list_oneMultiple,'\33[0m')

           random_betCount_multiple = input('请输入 注数和倍数，用空格分割(如2 3):')
           random_str_list = random_betCount_multiple.split(' ')
           try:
               betCount = random_str_list[0]  # 注数
               multiple = random_str_list[1] # 倍数
               random_list_nBet = random_choose_bet_multiple(int(betCount))
               multiple_number = int(multiple)
               for i,value in enumerate(random_list_nBet):
                   print('机选第{}注{}倍数:\033[1;31;0m{}*{}\33[0m'.format(i+1, multiple_number, value,multiple_number))
           except ValueError as e:
               print('请输入正确信息:\n',e)
               continue
           except IndexError as e:
               print('输入信息过少:\n',e)
               continue
           except:
               print('程序异常!\n')
               continue
       elif is_random == 'm':
           manual_red_ball = input('请输入6个红球,\033[1;31;0m区间1-33\33[0m,用空格分割(如2 23 33 13 6 8):')
           manual_blue_ball = input('请输入1个蓝球,\033[1;34;0m区间1-16\33[0m(如3):')
           manual_multiple  = input('请输入倍数(如5):')
           manual_red_ball_list = manual_red_ball.split(' ')
           try:
               manual_red_number_list = list(map(lambda x:int(x),manual_red_ball_list))
               blue_number = int(manual_blue_ball)
               manual_number_multiple = int(manual_multiple)

               manual_list_oneMultiple =  manual_choose_number(blue_number,*manual_red_number_list)
               if len(manual_red_number_list) != len(set(manual_red_number_list)):#去重
                   raise ValueError
               elif len(manual_list_oneMultiple) != 7:#红球和篮球的区间不符合条件
                   raise IndexError
               else:
                print('手选1注{}倍数的结果:\033[1;31;0m{}*{}\33[0m'.format(manual_number_multiple, manual_list_oneMultiple,manual_number_multiple))
           except ValueError as e:
               print('请输入正确信息:\n',e)
               continue
           except IndexError as e:
               print('输入信息过少:\n',e)
               continue
           except:
               print('程序异常!\n')
               continue
       else:
           print('\033[1;31;0m仅支持机选r和手选m,请输入:r/m\33[0m')
           continue
       y_or_n = 'n'

if __name__ == '__main__':
    main()




