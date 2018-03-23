import turtle
turtle.screensize(302,278)
turtle.write("hello world",font=("宋体",200,"normal"))
turtle.showturtle()

turtle.pensize(2)
turtle.begin_fill()
turtle.circle(200,steps = 3)
turtle.color("red")
turtle.end_fill()

turtle.reset()

turtle.pensize(2)
turtle.begin_fill()
turtle.circle(200,180)
turtle.color("red")
turtle.end_fill()

turtle.done()