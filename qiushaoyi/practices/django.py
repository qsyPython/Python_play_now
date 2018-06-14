'''
diango 使用

diango结构：
       __init__py:目录结构,和调用有关的包初始文件
       urls.py 网址，关联到对应的views.py中的一个函数，访问网址就是调用某个函数
       settings.py 设置配置文件，比如 DEBUG 的开关，静态文件的位置等
       wsgi.py:
       manage.py:

       views.py 处理用户发出的请求，通过渲染templates中的网页可以将显示内容
       models.py 与数据库操作相关，存入或读取数据
       forms.py 表单，用户在浏览器上输入数据提交，对数据的验证工作以及输入框的生成等工作；
                templates 文件夹，views.py中的函数渲染templates中的Html模板，动态内容的网页，缓存用
       admin.py 后台，可以用很少量的代码就拥有一个强大的后台。


准备： 1、virtualenv 来管理多个开发环境：pip3 install virtualenv virtualenvwrapper
添加环境变量指令：vim ~/.bash_profile
添加如下：
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/workspace
source /usr/local/bin/virtualenvwrapper.sh
修改生效指令：source ~/.bash_profile


virtualenv虚拟环境使用方法：
mkvirtualenv zqxt：创建运行环境zqxt
workon zqxt: 工作在 zqxt 环境 或 从其它环境切换到 zqxt 环境
deactivate: 退出终端环境
其它的：
rmvirtualenv ENV：删除运行环境ENV
mkproject mic：创建mic项目和运行环境mic
mktmpenv：创建临时运行环境
lsvirtualenv: 列出可用的运行环境
lssitepackages: 列出当前环境安装了的包

'''

'''
==========================practice 1:搭建django 项目和app  ==========================
1、获取django项目路径：cd /Users/mac/Desktop/Python_play_now/qiushaoyi/programs
2、创建项目：django-admin startproject django_first（名称）
3、进入项目目录: cd django_first
4、新建app：python3 manage.py startapp app_first（名称）

创建数据库表 或 更改数据库表或字段
# 1. 在django的project下，创建更改的文件：python3 manage.py makemigrations
# 2. 将生成的py文件应用到数据库：python3 manage.py migrate（创建的是sqlite3，若要建mysql文件，sqlmigrate）
# 3. 清空数据库:python3 manage.py flush
# 4. 复制appdata的数据库内容：python3 manage.py dumpdata appname > appname.json
# 5. 加载appdata的数据库内容：python3 manage.py loaddata appname.json


使用开发服务器(实现修改代码后会自动重启): django的服务器
python3 manage.py runserver
（# 当提示端口被占用的时候，可以用其它端口：
python3 manage.py runserver 8001
python3 manage.py runserver 9999
# 监听机器所有可用ip （电脑可能有多个内网ip或多个外网ip）：
python3 manage.py runserver 0.0.0.0:8000）
补充： 
    接口的工作流程：以访问web的url为例
    1、访问该url，connect到http的【web服务器:如Apache服务器、Django服务器】
    2、web服务器收到请求后，【执行CGI 或 Django服务】,解析url，在【database】/【file system】中查找访问的文件在服务器上是否存在，对就返回内容，否则报错返回
    3、浏览器从服务器上接收信息，并显示接收的文件或者错误信息
    
    
# 创建超级管理员 ：python3 manage.py createsuperuser（按照提示输入用户名和对应的密码就好了邮箱可以留空，用户名和密码必填） 
# 修改 用户密码可以用：python3 manage.py changepassword username(名称)


Django项目环境终端（调用django中的某些py文件的API）：python3 manage.py shell    退出：exit()
数据库命令行（操作数据库）： python3 manage.py dbshell


总结：不同的指令实现不同的功能
查看更多命令：python3 manage.py

'''



'''
==========================practice 2: 走一波项目  ==========================
django-admin startproject project_name
python3 manage.py startapp app_name
project的settings：在末尾添加app_name,（你就不添加？好，django就不能自动找到app中的模板文件(app-name/templates/下的文件)和静态文件(app-name/static/中的文件) ）

app的views定义视图函数：
from django.http import HttpResponse
def index(request):
    return HttpResponse(u'欢迎跟着你少一哥哥学习django')

project的urls：定义视图函数相关的URL


'''