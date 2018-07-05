from django.shortcuts import render

# 创建一个templates的文件
def app_third_home(request):
    return render(request,'app_third/app_third_home.html')