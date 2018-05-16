from xiedong.L2.score import *

def login_score(msg):
    print(msg)
    input_str = input("请确定查分还是录入成绩 1 查分 2 录入: ")
    if "1" == input_str.rstrip().lstrip().lower():
        get_score()
    elif "2" == input_str.rstrip().lstrip().lower():
        input_score()
    else:
        login_score("输入的不对哦,请重新输入")

def get_score():
    name = input("请输入姓名: ")
    score_sys = ScoreSystem("123")
    score = score_sys.get_score(name)
    if score == "":
        print("没有你的成绩或者输入姓名不对")
    else:
        print(score)

def input_score():
    name = input("请输入姓名: ")
    input_score = input("请输入成绩: ")
    score_sys = ScoreSystem("123")
    try:
        score = int(input_score)
    except ValueError:
        print("输入的不对哦")
    else:
        stu = Student(name)
        stu.set_score(score)
        score_sys.imput_score(stu)



login_score("欢迎")