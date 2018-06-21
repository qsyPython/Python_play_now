'''
diango 使用

diango结构：
       __init__py:目录结构,和调用有关的包初始文件
       urls.py 网址，关联到对应的views.py中的一个函数，访问网址就是调用某个函数
       settings.py 设置配置文件，比如 DEBUG 的开关，模板文件、静态文件等
       wsgi.py: 部署服务器
       manage.py:diango程序的执行入口

       views.py ：处理用户发出的请求，通过渲染templates中的网页可以将显示内容
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
==========================practice 1:搭建django 项目和apps  ==========================
1、获取django项目路径：cd /Users/mac/Desktop/Python_play_now/qiushaoyi/programs
2、创建项目：django-admin startproject django_first（名称）
3、进入项目目录: cd django_first
4、新建app：python3 manage.py startapp app_first（名称）

创建数据库表 或 更改数据库表或字段 
# 1. 在django的project下，创建更改的文件：python3 manage.py makemigrations
# 2. 将生成的py文件应用到数据库：python3 manage.py migrate（创建的是sqlite3，若要建mysql文件，sqlmigrate）
# 3.python3 manage.py syncdb
  3. 清空数据库:python3 manage.py flush
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

project的urls：定义视图函数相关的URL。如下：
  path('add/',app_second_views.add,name='add'), #实现加法功能，需要手动拼参数：访问方式 http://127.0.0.1:8000/add/?a=4&b=5
name 可以用于在 templates, models, views ……中得到对应的网址，相当于“给网址取了个名字”。
只要这个名字不变，网址变了也能通过名字获取到。

问题1、使用name写死网站的后果：
如果这样写“死网址”，会使得在改了网址（正则）后，
模板（templates)，
视图(views.py，比如用于URL跳转)，
模型(models.py，获取记录访问地址等）用了此网址的，
都必须进行相应的更改，修改的代价很大，一不小心，有的地方没改过来，就不能用了

解决办法->：在模板、视图和模型中均使用name作为url的连接key，只要name不变，path/url正则即使随便改变，也会被链接到。

进入python shell:(可快速获取某个name对应url的方法，这里的name本质上是key)
python3 manage.py shell

from django.urls import reverse  # Django 1.10.x - Django 2.x 新的，更加规范了
>>> reverse('add2', args=(4,5))
u'/add/4/5/'
>>> reverse('add2', args=(444,555))
u'/add/444/555/'

问题2、用户收藏的url为旧的，如何让以前的 /add/3/4/自动跳转到现在新的网址呢？
在views添加跳转函数,具体查看app_second实例


问题3、查找机制，导致模板名称会找错？
在每个templates中新建一个app同名的file就ok,但所有涉及到的html文件使用必须加上该apo的文件路径



然后可再在某个端口执行服务：默认是8000
python manage.py runserver 8002

'''





'''
==========================practice 2: 走一波项目  ==========================
1、db中使用的字段：
__双下划线不合法 + python的所有关键字也不合法
查询方法：import keyword; print(keyword.kwlist) 可以打出所有的关键字

2、使用python3的shell操作指令：
from people.models import Person 

# 增加对象4种方式:
1、Person.objects.create(name='我擦',age=11)
2、p = Person(name='woca',age=12)
p.save()
3、p = Person(name='rilegoule')
p.age = 12
p.save()
4、Person.objects.get_or_create(name='喔吼吼',name = 33)

# 查询 对象的n种方法：

Person.objects.all()
Person.objects.all()[:10] 切片可以节约内存

Person.objects.get(name='得到名字为xxx的数据')

Person.objects.filter(name='abc')
Person.objects.filter(name__iexact='abc') #名称为abc并不区分大小写
Person.objects.filter(name__contain= 'ab')
Person.objects.filter(name__icontain='ab')#名称中包含 "abc"，且abc不区分大小写
Person.objects.filter(name__regex='^abc')# 正则表达式查询
Person.objects.filter(name_iregex='^abc')# 正则表达式不区分大小写
Person.objects.filter(name__contains='abc').exlude(age=23)
Person.objects.exclude(name__contains='WC')

# 删除：
Person.objects.filter(name__contains='abc').delete()

# 更新：
Persoon.objects.get(name='wocao').update(name='nima',email='1379587985@qq.com')
Person.objects.filter(name__contains='abc).update(name='我是新name')

# 异常判断
if Person.objects.all().exists(): 表中是否存在数据
Person.objects.count()>0 表中是否存在数据

# pickle序列化和反序列化
import pickle
s = Person.objects.all()  Entry.objects.all() 或者 es 是QuerySet 是查询所有的 Entry 条目
query = pickle.loads(s)
qs = Person.objects.all
qs.query = query


2、QuerySet：数据库接口shell操作：
当有一对多，多对一，或者多对多的关系的时候，先把相关的对象查询出来
>>> from blog.models import Entry
>>> entry = Entry.objects.get(pk=1)
>>> cheese_blog = Blog.objects.get(name="Cheddar Talk")
>>> entry.blog = cheese_blog
>>> entry.save()





'''

