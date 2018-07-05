#CGI(Common Gateway Interface),通用网关接口,它是一段程序,运行在服务器上如：HTTP服务器，提供同客户端HTML页面的接口

'''
开启apache:  sudo apachectl start
重启apache:  sudo apachectl restart
关闭apache:  sudo apachectl stop
'''

#http://localhost/cgi-bin/hello.py
#/private/etc/apache2/httpd.conf   apache服务器的配置路径
#/资源库/WebServer/Documents        apache服务器访问路径
#/资源库/WebServer/CGI-Executables  cgi访问路径

#mac的具体配置可以查看这个简书https://www.jianshu.com/p/68b11edc055e
#按照以上的配置完成后,可能会出现  You don't have permission to access..."的错误
#解决:将"Require all denied"修改成"Require all granted"

#例子
'''
http://localhost/cgi-bin/hello.py
http://localhost/cgi-bin/path.py
'''
