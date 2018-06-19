from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def forth_index(request):

    # 实例一，显示一个基本的字符串在网页上
    # string = u'我交朋友不在乎你们有没有钱，反正都没我有钱，大家好，我是王思聪了解一下'
    # return render(request,'app_forth/forth_home.html',{'string':string})

    # 实例二，讲解了基本的for 循环 和 List内容的显示
    # tutorialList = [u'HTML是么',u"CSS再说一次", u"jQuery给我", u"Python试试", "Django看"]
    # return render(request,'app_forth/forth_home.html',{'tutorialList':tutorialList})

    # 实例三，显示字典中内容：
    # info_dict = {'site':u'自学开始了','content':u'这是我懂啦攻击力科技考虑到撒娇管理会计'}
    # return render(request,'app_forth/forth_home.html',{'info_dict':info_dict})

    # 实例四，在模板进行条件判断和for 循环的详细操作：
    # list = map(str,range(100))
    # return render(request,'app_forth/forth_home.html',{'list':list})

    # 实例六，模板中的逻辑操作
    # var = 93
    # num = 13
    # return render(request,'app_forth/forth_home.html',{'var':var,'num':num})

    # 实例七，模板中获取当前网址，当前用户等
    tt = 'jjj'
    return render(request,'app_forth/forth_home.html',{'ttt':tt})




# 实例五，模板上得到视图对应的网址
def add(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))



