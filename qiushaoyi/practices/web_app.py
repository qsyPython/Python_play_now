'''
web开发：
1、PC机的兴起，软件开始主要运行在桌面上，而数据库这样的软件运行在服务器端，
这种Client/Server模式简称CS架构。

2、互联网的兴起，Web应用程序的修改和升级非常迅速，逐个升级web应用比较麻烦，
这时候，Browser/Server模式开始流行，简称BS架构。蔓延开，
除了重量级的软件如Office，Photoshop等，大部分软件都以Web形式提供。
比如，新浪提供的新闻、博客、微博等服务，均是Web应用

3、Web开发也经历了好几个阶段：
a、静态Web页面：html页面
b、CGI（Common Gateway Interface）：简单交互，用C和C++
c、ASP/JSP/PHP：web本身开发快，脚本语言（VB、Java、PHP、Python）高级语言由于开发效率高，与HTML结合紧密
d、MVC：解决直接用脚本语言嵌入HTML导致的可维护性差的问题，MVC模式出现
现在，异步开发、MVVM模式出来...

总结：
Python为解释型脚本语言，开发效率高，炒鸡适合web开发。

'''


'''
==========================practice 1: http协议 ==========================
'''
# HTML是一种用来定义网页的文本，会HTML，就可以编写网页；
#
# HTTP是在网络上传输HTML的协议，用于浏览器和服务器的通信。

# 跟踪了新浪的首页，我们来总结一下HTTP请求的流程3步走：
#
# 步骤1：浏览器首先向服务器发送HTTP请求，请求包括：
#
# 方法：GET还是POST，GET仅请求资源，POST会附带用户数据；
#
# 路径：/full/url/path；
#
# 域名：由Host头指定：Host: www.sina.com.cn
#
# 以及其他相关的Header；
#
# 如果是POST，那么请求还包括一个可选的Body，包含用户数据。
#
# 步骤2：服务器向浏览器返回HTTP响应，响应包括：
#
# 响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；
#
# 响应类型：由Content-Type指定；
#
# 以及其他相关的Header；
#
# 通常服务器的HTTP响应会携带内容，也就是有一个Body，包含响应的内容，网页的HTML源码就在Body中。
#
# 步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2。

# 浏览器请求分为GET和POST：
# GET /path HTTP/1.1
# Header1: Value1
# Header2: Value2
# Header3: Value3
#
# POST /path HTTP/1.1
# Header1: Value1
# Header2: Value2
# Header3: Value3
#
# body data goes here...

# 服务器返回：
# 200 OK
# Header1: Value1
# Header2: Value2
# Header3: Value3
#
# body data goes here...
'''
==========================practice 2: html简介 ==========================
'''
# 见web基础开发.html
'''
==========================practice 3: wsgi接口使用：1个函数 对应 1个http请求 ==========================
一个Web App的本质就是：

浏览器发送一个HTTP请求；

服务器收到请求，生成一个HTML文档；

服务器把HTML文档作为HTTP响应的Body发送给浏览器；

浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

wsgi简化web应用为：
从environ这个dict对象拿到HTTP请求信息，然后构造HTML，通过start_response()发送http请求信息中的Header，最后返回Body
这么吊，那application()函数谁调用的？ 必须是由WSGI服务器来调用的
'''
# 参数2个
# environ：一个包含所有HTTP请求信息的dict对象；
# dict就是client的请求的信息
# start_response：一个发送HTTP响应的函数；
#start_response该函数：接受2个参数：1个是HTTP响应码，1个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示。

# 返回值：函数的返回值b'<h1>Hello, web!</h1>'将作为HTTP响应的Body发送给浏览器，用于展示
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # body = '<h1> hello ,%s!</h1>'%(environ['PATH_INFO'][1:] or 'web')
    # return [body.encode('utf-8')]
    return [b'<h1>Hello, web!</h1>']


# 配合 wsgiref 服务器使用，见 wsgi_server.py文件
'''
==========================practice 4: 常见web框架使用 ==========================
'''


'''
==========================practice 5: 模板 ==========================
'''
