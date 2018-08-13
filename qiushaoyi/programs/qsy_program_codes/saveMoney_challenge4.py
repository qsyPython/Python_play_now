'''
	2.0增加功能：记录每周的存款数
    3.0增加功能：使用循环直接计数
    4.0增加功能：灵活设置每周的存款数，增加的存款数及存款周数
    5.0增加功能：根据用户输入的日期，判断是一年中的第几周，然后输出相应的存款金额
'''
import time

t = time.time()
print(t)

import math
import datetime, time

saving = 0  # 全局变量，在所有函数中都适用。 但若要想修改该全局变量，需要在函数内用global声明


def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    '''
        计算n 周内的存款金额
    '''
    print(math.sin(1.3))
    money_list = []  # 记录每周存款数的列表
    saved_money_list = []  # 记录每周账户累计的列表
    global saving
    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)  # saving为局部变量:函数内部定义的，只在对应函数内起作用
        saved_money_list.append(saving)
        money_per_week += increase_money
    return saved_money_list


def main():
    '''
        主函数
    '''
    money_per_week = float(input('请输入每周的存入的金额: '))
    increase_money = float(input('请输入每周递增金额: '))
    total_week = int(input('请输入总共的周数：'))

    input_date_str = input('请输入截止日期(yyyy/mm/dd):')
    input_date = datetime.datetime.strptime(input_date_str, '%Y/%m/%d')

    current_time_date_str = time.strftime('%Y/%m/%d', time.localtime(time.time()))
    current_time_date = datetime.datetime.strptime(current_time_date_str, '%Y/%m/%d')

    week_num = input_date.isocalendar()[1]
    week_curretn_num = current_time_date.isocalendar()[1]
    last_all_week = week_num - week_curretn_num
    if last_all_week > total_week:
        saved_money_list = save_money_in_n_weeks(money_per_week, increase_money, last_all_week)
        print('第{}周的总存款：{}元'.format(total_week, saved_money_list[total_week - 1]))
    else:
        saved_money_list = save_money_in_n_weeks(money_per_week, increase_money, total_week)
        print('第{}周的总存款：{}元'.format(total_week, saved_money_list[last_all_week - 1]))


if __name__ == '__main__':
    main()
