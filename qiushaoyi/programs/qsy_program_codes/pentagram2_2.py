'''
	作者：邱少一
	功能：五角星绘制
	版本：3.0
	日期：2017/11/24
	新增功能：加入循环操作绘制重复不同大小的图形
    新增功能：使用迭代函数绘制重复不同大小的图形，递归函数
'''

import turtle


def draw_pentagram(size):
    '''
        绘制五角星
    '''
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1


def draw_recursive_pentagram(size):
    '''
        迭代绘制五角星
    '''
    count = 1
    while count <= 5:
        turtle.forward(size)  # 向前走size
        turtle.right(144)  # 向右转144度
        count += 1
    size += 10
    if size <= 90:
        draw_recursive_pentagram(size)


def main():
    '''
        主函数
    '''
    turtle.penup()  # 抬起笔
    turtle.backward(200)  # 向后走200
    turtle.pendown()  # 放下笔，开始画
    turtle.pensize(2)  # 设置笔大小
    turtle.pencolor('red')
    size = 50
    draw_recursive_pentagram(size)

    turtle.exitonclick()


if __name__ == '__main__':
    main()
