'''
    1.0增加功能：用元组表示
	2.0增加功能：用列表替换元组
    3.0增加功能：将月份划分为不同的集合再操作
    4.0增加功能：将月份及其对应天数通过字典表示
'''
from datetime import datetime


def is_leap_year(year):  # 使用 初始化的变量 可简化if else
    '''
        是否是闰年
    '''
    is_leap = False
    if (year % 400) == 0 | (year % 4 == 0) | (year % 100 != 0):
        is_leap = True
    return is_leap


def main():
    input_date_str = input('请输入日期(yyyy/mm/dd): ')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')

    year = input_date.year
    month = input_date.month
    day = input_date.day
    days = 0
    # 1、元组
    # days_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # days = sum(days_in_month_tup[:month-1])+day
    # if is_leap_year(year) & month >2:
    # 	days += 1

    # 2、列表
    # days_in_month_tup = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # for i in range(month-1):
    # 	days += days_in_month_tup[i]
    # days += day
    # if is_leap_year(year) & month> 2:
    # 	days += 1
    # 3、集合
    # _30_days_month = {4,6,9,11}
    # _31_days_month = {1,3,5,7,8,10,12}
    # for i in range(1,month):
    # 	if i in _30_days_month:
    # 		days += 30
    # 	elif i in _31_days_month:
    # 		days += 31
    # 	else:
    # 		days += 28
    # days += day
    # if is_leap_year(year) & month >2:
    # 	days += 1

    # 4、字典
    month_day_dict = {1: 31,
                      2: 28,
                      3: 31,
                      4: 30,
                      5: 31,
                      6: 30,
                      7: 31,
                      8: 31,
                      9: 30,
                      10: 31,
                      11: 30,
                      12: 31
                      }
    for i in range(1, month):
        days += month_day_dict[i]
    days += day
    if is_leap_year(year) & month > 2:
        days += 1

    print('这是{}年的第{}天。'.format(year, days))


if __name__ == '__main__':
    main()
