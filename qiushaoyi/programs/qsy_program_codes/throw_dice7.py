'''
	作者：邱少一
	功能：
	1.0功能：模拟投掷一个骰子
	2.0新增功能：模拟投掷两个骰子
    3.0新增功能：可视化投掷两个骰子的结果
    4.0新增功能：=======直方图可视化作图和统计工具：matplotlib
    5.0新增功能：=======科学计算工具：numpy

	版本：1.0
	日期：2017/12/1
	学习：1、随机数：random():0到1的数；uniform（a,b）:a到b的随机浮点数；randint（a,b）:a到b的随机数
	choice(<list>)：随机从list中取一个元素 ;shuffle(<list>)：将列表中元素打乱,sample(<list>,k):从列表中随机获取k个元素
	2、安装 matplotlib 终端输入：pip3 install matplotlib pip3是Python3以上自带的包管理器
'''

import random
import matplotlib.pyplot as pltqsy
import numpy as npqsy

# 解决中文显示问题:方案一 matplotlib中缺少中文格式的字体，如simhei，手动添加到
pltqsy.rcParams['font.sans-serif'] = ['SimHei']
pltqsy.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题


def random_roll():
    roll = random.randint(1, 6)
    return roll


def main():
    '''
        主函数
    '''
    # '''
    # 	单个骰子投掷时出现的结果
    # '''
    # throw_times = 100
    # result_list =[0]*6 #用于统计 每个数字 出现的次数。以位置和value建立映射bridge
    #
    # for i in range(throw_times):
    # 	roll = random_roll()
    # 	print('摇的数字：'roll)
    # 	for j in range(1,7):
    # 		if roll == j:
    # 			result_list[j-1] += 1
    #
    # for i,result in enumerate(result_list):
    # 	print('点数{}的次数{},概率{}'.format(i+1,result,result/throw_times))

    # '''
    # 	2个骰子投掷时出现的结果
    # '''
    # throw_total_times = 10
    # result_count_list = [0]*12
    # result_num_list = list(range(2,13))
    # result_dict = dict(zip(result_num_list,result_count_list))

    # 记录每次骰子的结果
    # roll1_list = []
    # roll2_list = []
    # roll_total_list = []
    # for i in range(throw_total_times):
    # 	roll1 = random.randint(1,6)
    # 	roll2 = random.randint(1,6)
    # 	total_roll = roll1 + roll2
    #
    # 	# 记录骰子的结果
    # 	roll1_list.append(roll1)
    # 	roll2_list.append(roll2)
    # 	roll_total_list.append(total_roll)
    #
    # 	for key,value in result_dict.items():
    # 		if key == total_roll:
    # 			result_dict[key] += 1 #坑点：value += 1只是修改了value，但并没有修改对应的dict
    # for key,value in result_dict.items():
    # 	print(('点数之和{}出现的次数{},出现的概率为{}'.format(key,value,value/throw_total_times)))
    # 可视化的散点图绘制： plt.scatte(x,y)
    # x = range(1, throw_total_times + 1)
    # plt.scatter(x, roll1_list, c='red', alpha=0.5)
    # plt.scatter(x, roll2_list, c='green', alpha=0.5)
    # plt.show()

    # 可视化的直方图绘制:plt.hist(data,hins（data数据的边界list）)
    # pltqsy.hist(roll_total_list,bins=range(2,14),normed=1,edgecolor ='white',linewidth = 1)
    # pltqsy.title('骰子点数统计')
    # pltqsy.xlabel('点数')
    # pltqsy.ylabel('频率')
    # pltqsy.show()

    # 科学计算
    # 通过随机数模拟掷骰子过程
    throw_total_times = 10000
    roll1_arr = npqsy.random.randint(1, 7, size=throw_total_times)  # 创建[a,b)间形状为size的数组
    roll2_arr = npqsy.random.randint(1, 7, size=throw_total_times)

    result_arr = roll1_arr + roll2_arr  # numpy的加减是对应的位置value的加减，向量化的数据

    # 读取数据：hist出现的次数，bins为对应的2次摇骰子的和
    # hist,bins = npqsy.histogram(result_arr,bins=range(2,14))
    # print(hist,'\n==========',bins)

    # 数据可视化
    pltqsy.hist(result_arr, bins=range(2, 14), normed=1, edgecolor='white', linewidth=1, rwidth=0.8)

    # 重新设置x轴坐标点：tick_labels 和 固有的点进行位置映射
    tick_labels = [(str(i) + '点') for i in range(2, 13)]
    tick_pos = npqsy.arange(2, 13) + 0.5
    pltqsy.xticks(tick_pos, tick_labels)

    pltqsy.title('骰子点数统计')
    pltqsy.xlabel('点数')
    pltqsy.ylabel('频率')
    pltqsy.show()


if __name__ == '__main__':
    main()
