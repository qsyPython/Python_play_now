"""django_first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('b_blog/', include('b_blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from app_first import views as app_first_views #2.0以上django使用
from app_second import views as app_second_views
from app_third import views as app_third_views
from app_forth import views as app_forth_views

urlpatterns = [
    # 参数1为能匹配到url正则表达，参数2为该url对应的函数，参数3为该url对应的key


    # ====操作app_first_views
    path('',app_first_views.index),#2.0以上django使用，调用到views层中index进行渲染
    path('admin/', admin.site.urls),#进入super管理员模式


    # ====操作app_second_views
    # path('add/',app_second_views.add,name='add'), #实现加法功能，需要手动拼参数：访问方式 http://127.0.0.1:8000/add/?a=4&b=5
    path('addhhh/<int:a>/<int:b>/',app_second_views.add2,name='add2'),#实现加法2功能，需要手动拼参数 访问方式 http://127.0.0.1:8000/add/234/665
    path('minute/',app_second_views.minute,name='minute'), #实现减法功能，需要手动拼参数 访问方式 http://127.0.0.1:8000/minute/?a=3&b=5

    #url使用同path,不过url得正则匹配
    url(r'^second_home/$',app_second_views.index,name='second_home'),
    url(r'^add/$',app_second_views.add,name='add'),
    url(r'^add/(\d+)/(\d+)/$',app_second_views.old_add2_redirect),


    # ====操作app_third_views
    url(r'^third_home/$', app_third_views.app_third_home, name='third_home'),


    # ====操作app_forth_views
    url(r'^forth_home/$',app_forth_views.forth_index,name='forth_home'),
    url(r'^forth_add/(\d+)/(\d+)/$',app_forth_views.add,name='forth_add'),

]
