'''
    CGI(Common Gateway Interface),通用网关接口。
    它是一段运行在服务器（如http服务器）上的程序。
    该接口可为客户端提供HTML页面的接口！
    接口的工作流程：以访问web的url为例
    1、访问该url，连接到http的【web服务器】
    2、web服务器收到请求后，【执行CGI】,解析url，在【database】/【file system】中查找访问的文件在服务器上是否存在，对就返回内容，否则报错返回
    3、浏览器从服务器上接收信息，并显示接收的文件或者错误信息

    CGI编程的准备：
         1、配置Apache等web服务器
         2、配置Apache服务器 支持CGI
         3、配置CGI的处理程序
    服务器访问地址：http://10.9.3.240/cgi-bin/py文件名.py
'''

'''
==========================practice 1: 基本使用加载text/html的content ==========================
'''

# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# print ("Content-type:text/html") # 发送给浏览器告诉浏览器文件的内容类型
# print                           # 空行，告诉服务器结束头部
# print ('<html>')
# print ('<head>')
# print ('<meta charset="utf-8">')
# print ('<title>Hello World - 我的第一个 CGI 程序！</title>')
# print ('</head>')
# print ('<body>')
# print ('<h2>Hello World! 我是来自菜鸟教程的第一CGI程序</h2>')
# print ('</body>')
# print ('</html>')


'''
==========================practice 2: 加载系统的环境变量 ==========================
'''
# !/usr/bin/python
# -*- coding: UTF-8 -*-
# filename:test.py

# import os
#
# print ("Content-type:text/html")
# print
# print ("<meta charset=\"utf-8\">")
# print ("<b>环境变量</b><br>")
# print ("<ul>")
# for key in os.environ.keys():
#     print ("<li><span style='color:green'>%30s </span> : %s </li>" % (key,os.environ[key]))
# print ("</ul>")


# !/usr/bin/python
# -*- coding: UTF-8 -*-
# filename:test.py
# CGI 处理模块
import cgi, cgitb

'''
======================practice 3: 简单的url实例：GET方法:结合cgi_get.html跳转 ==========================
'''
# # 服务器路径/cgi-bin/test.py?name=少测下教程一&url=http://www.baidu.com
# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# #filename:test.py
#
# #CGI处理模块
# import cgi,cgitb
# #创建FieldStorage的实例化：该中存放着url的参数
# form = cgi.FieldStorage()
# #获取数据
# site_name = form.getvalue('name')
# site_url = form.getvalue('url')
#
# print ("Content-type:text/html") # 发送给浏览器告诉浏览器文件的内容类型
# print                           # 空行，告诉服务器结束头部
# print ('<html>')
# print ('<head>')
# print ('<meta charset="utf-8">')
# print ('<title>测试一下哈</title>')
# print ('</head>')
# print ('<body>')
# print('<h2>%s：%s</h2>'%(site_name,site_url))
# print ('</body>')
# print ('</html>')


'''
==========================practice 4: 简单的url实例：POST ==========================
'''

# #!/usr/bin/python
# # -*- coding:UTF-8 -*-
#
# import cgi,cgitb
#
# #创建 FieldStore的实例化
# form = cgi.FieldStorage()
#
#
# #获取数据
# site_list = form.getlist()
# site_name = form.getvalue('name')
# site_url = form.getvalue('url')
# print('Content-type:text/html')
# print
# print('<html>')
# print('<head>')
# print('<meta charset=\'utf-8\'>')
# print('<title>我就是测一测</title>')
# print('</head>')
# print('<body>')
# print('<h2>%s到时候:%s 和 %s </h2>'%(site_list,site_url,site_name))
# print('</body>')
# print('</html>')

'''
==========================practice 5: 选择器  ==========================
'''

# #!/usr/bin/python
# # -*- coding:UTF-8 -*-
#
# import cgi, cgitb
#
# # 创建 FieldStore的实例化
# form = cgi.FieldStorage()
#
# # 获取数据
# if form.getvalue('ali'):
#     ali_flag = '是'
# else:
#     ali_flag = '否'
#
# if form.getvalue('tencent'):
#     tencent_flag = '是'
# else:
#     tencent_flag = '否'
#
# if form.getvalue('google'):
#     google_flag = '是'
# else:
#     google_flag = '否'
#
# print('Content-type:text/html')
# print
# print('<html>')
# print('<head>')
# print('<meta charset=\'utf-8\'>')
# print('<title>我就是测一测</title>')
# print('</head>')
# print('<body>')
# print('<h2>阿里 是否被选择了:%s</h2>' % ali_flag)
# print('<h2>腾讯是否被选择了:%s</h2>' % tencent_flag)
# print('<h2>google是否被选择了:%s</h2>' % google_flag)
# print('</body>')
# print('</html>')

'''
==========================practice 6: radio使用 ==========================
'''
# #!/usr/bin/python
# # -*- coding:UTF-8 -*-
#
# import cgi, cgitb
#
# # 创建 FieldStore的实例化
# form = cgi.FieldStorage()
#
# # 获取数据
# if form.getvalue('site'):
#     site = form.getvalue('site')
# else:
#     site = '数据提交为空'
#
#
# print('Content-type:text/html')
# print
# print('<html>')
# print('<head>')
# print('<meta charset=\'utf-8\'>')
# print('<title> radio </title>')
# print('</head>')
# print('<body>')
# print('<h2>选中的网站是:%s</h2>' % site)
# print('</body>')
# print('</html>')


'''
==========================practice 7:textarea  ==========================
'''
# #!/usr/bin/python
# # -*- coding:UTF-8 -*-
#
# import cgi, cgitb
#
# # 创建 FieldStore的实例化
# form = cgi.FieldStorage()
#
# # 获取数据
# if form.getvalue('textcontent'):
#     text_content = form.getvalue('textcontent')
# else:
#     text_content = '没有数据'
#
# print('Content-type:text/html')
# print
# print('<html>')
# print('<head>')
# print('<meta charset=\'utf-8\'>')
# print('<title> textarea </title>')
# print('</head>')
# print('<body>')
# print('<h2>输入的内容是:%s</h2>' % text_content)
# print('</body>')
# print('</html>')

'''
==========================practice 8:dropdown  ==========================
'''
# #!/usr/bin/python
# # -*- coding:UTF-8 -*-
#
# import cgi, cgitb
#
# # 创建 FieldStore的实例化
# form = cgi.FieldStorage()
#
# # 获取数据
# if form.getvalue('dropdown'):
#     dropdown = form.getvalue('dropdown')
# else:
#     dropdown = '没有内容'
#
# print('Content-type:text/html')
# print
# print('<html>')
# print('<head>')
# print('<meta charset=\'utf-8\'>')
# print('<title> textarea </title>')
# print('</head>')
# print('<body>')
# print('<h2>选中的内容是:%s</h2>' % dropdown)
# print('</body>')
# print('</html>')

'''
==========================practice 9:cookie set 和 get  ==========================
cookie 就是在客户访问脚本的同时，通过客户的浏览器，在客户硬盘上写入纪录数据。 
当下次客户访问脚本时取回数据信息，从而达到身份判别的功能，cookie 常用在身份校验中！
cookie作用：客户访问脚本的同时，通过客户的浏览器，在客户硬盘上写入纪录数据；
           当下次客户访问脚本时取回数据信息，从而达到身份判别的功能。
python3中为http.cookies模块
'''
#!/usr/bin/python
# -*- coding:UTF-8 -*-

# print('Content-type:text/html')
# print('Set-Cookie: name="邱少一";expires=Wed, 28 Aug 2016 18:30:00 GMT')
# print
# print('<html>')
# print('<head>')
# print('<meta charset=\'utf-8\'>')
# print('<title> Set_Cookie </title>')
# print('</head>')
# print('<body>')
# print('<h2>Cookie set OK</h2>')
# print('</body>')
# print('</html>')



# import os
# import http.cookies
# # print('Content-type:text/html')
# # print('Set-Cookie: name="邱少一";expires=Wed, 28 Aug 2016 18:30:00 GMT')
# # print
# # print('<html>')
# # print('<head>')
# # print('<meta charset=\'utf-8\'>')
# # print('<title> Set_Cookie </title>')
# # print('</head>')
# # print('<body>')
# # print('<h2>Cookie set OK</h2>')
# print(os.environ)
# if 'HTTP_COOKIE' in os.environ:
#     cookie_string = os.environ.get('HTTP_COOKIE')
#     c = http.cookies.SimpleCookie()
#     c.load(cookie_string)
#
#     try:
#         data = c['name'].value
#         print('cookie data:\'+data+\'<br>')
#     except KeyError:
#         print('cookie 没有设置或者已过去<br>')
# # print('</body>')
# # print('</html>')


'''
==========================practice 10:上传文件  ==========================
失败了
'''
# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# import cgi,os
# import cgitb
#
# cgitb.enable()
#
# form = cgi.FieldStorage()
#
# # 获取文件名
# fileitem = form.getvalue('filename')
#
# # 检测文件是否上传
# if fileitem.filename:
#     # 设置文件路径
#     fn = os.path.basename(fileitem.filename.replace("\\", "/"))
#     open('/tmp/' + fn, 'wb').write(fileitem.file.read())
#
#     message = '文件 "' + fn + '" 上传成功'
#
# else:
#     message = '文件没有上传'
#
# print
# ('''\
# Content-Type: text/html\n
# <html>
# <head>
# <meta charset="utf-8">
# <title>upload_file</title>
# </head>
# <body>
#    <p>%s</p>
# </body>
# </html>'''' '% message )

'''
==========================practice 10:下载文件  ==========================

'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# HTTP 头部
print ("Content-Disposition: attachment; filename=\"qsy_foo.txt\"")
print

with open("foo.txt", "rb",newline='') as f:
     print (f.read())




