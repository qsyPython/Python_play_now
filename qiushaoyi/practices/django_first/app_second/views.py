from django.shortcuts import render
from django.http import HttpResponse
# url跳转需要导入的模块
from django.http import HttpResponseRedirect
from django.urls import reverse

def add(request): # get请求后返回的数据
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def minute(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) - int(b)
    return HttpResponse(str(c))

# 渲染template使用render
def index(request):
    return render(request,'app_second/second_home.html')

# 处理用户收藏了旧url自动跳转新url
def old_add2_redirect(request,a,b):
    return HttpResponseRedirect(
        reverse('add2',args=(4,5))
    )



