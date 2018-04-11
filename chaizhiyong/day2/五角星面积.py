import turtle
import math
data = input("请输入数据：")
data = eval(data)
area = 5*data*data/math.tan(math.pi/5)/4
turtle.circle(data,steps = 5)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.write(str(area))
turtle.done()
