'''
	作者：少一
	版本：1.0
	日期：2017/11/11
	功能：利用递归函数绘制分形树
'''

import turtle


def draw_branch(branch_length):
    '''
        迭代绘制树枝
    '''
    if branch_length > 5:
        # 绘制右侧树枝
        turtle.forward(branch_length)
        print('向前 ', branch_length)
        turtle.right(20)
        print('右转 20')
        draw_branch(branch_length - 15)  # 递归执行该递归，才向下顺序执行，branch_length从0到90

        # 绘制左侧树枝
        turtle.left(40)
        print('左转 40')
        draw_branch(branch_length - 15)  # 递归执行，才向下顺序执行，branch_length从0到90

        # 返回之前的树枝
        turtle.right(20)
        print('右转 20')
        turtle.backward(branch_length)
        print('向后 ', branch_length)


def main():
    '''
        主函数
    '''

    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.pensize(3)
    turtle.pencolor('brown')

    turtle.left(90)
    branch_length = 90
    draw_branch(branch_length)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
