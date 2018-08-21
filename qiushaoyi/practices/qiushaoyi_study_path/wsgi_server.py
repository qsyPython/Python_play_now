from wsgiref.simple_server import make_server

from web_app import application

# 创建一个wsgi服务器，IP地址为空，端口是8000，处理函数是application
httpd = make_server('', 9000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求
httpd.serve_forever()
