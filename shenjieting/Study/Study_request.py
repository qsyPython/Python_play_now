

import urllib.request
import urllib.parse

'''
urllib中包括了四个模块，包括:urllib.request,urllib.error,urllib.parse,urllib.robotparser
urllib.request可以用来发送request和获取request的结果
urllib.error包含了urllib.request产生的异常
urllib.parse用来解析和处理URL
urllib.robotparse用来解析页面的robots.txt文件


使用urllib.request发送请求


urllib.request.urlopen()基本使用
urllib.request 模块提供了最基本的构造 HTTP 请求的方法，利用它可以模拟浏览器的一个请求发起过程，同时它还带有处理 authenticaton （授权验证）， redirections （重定向)， cookies (浏览器Cookies）以及其它内容。好，那么首先我们来感受一下它的强大之处，我们百度为例，我们来把这个网页抓下来。
'''
r = urllib.request.urlopen("http://www.baidu.com")
print(r.read().decode("utf-8"))
print(type(r))

#通过输出结果可以发现它是一个 HTTPResposne 类型的对象，
# 它主要包含的方法有 read() 、 readinto() 、getheader(name) 、 getheaders() 、 fileno() 等函数和 msg 、 version 、 status 、 reason 、 debuglevel 、 closed 等属性。
# 得到这个对象之后，赋值为 response ，然后就可以用 response 调用这些方法和属性，得到返回结果的一系列信息。
# 例如 response.read() 就可以得到返回的网页内容， response.status 就可以得到返回结果的状态码，如200代表请求成功，404代表网页未找到等。
print("*"*30)
print(r.getheaders())

'''
urllib.request.urlopen()详解
利用以上最基本的 urlopen() 方法，我们可以完成最基本的简单网页的 GET 请求抓取。
如果我们想给链接传递一些参数该怎么实现呢？我们首先看一下 urlopen() 函数的API。
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None) 
'''
print("*"*30)
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding= 'utf8')
res = urllib.request.urlopen("http://www.baidu.com",data=data)
print(res.read())


'''
timeout参数

timeout 参数可以设置超时时间，单位为秒，意思就是如果请求超出了设置的这个时间还没有得到响应，就会抛出异常，如果不指定，就会使用全局默认时间。它支持 HTTP 、 HTTPS 、 FTP 请求。
'''
print("*"*30)
respon=urllib.request.urlopen("http://httpbin.org/get",timeout=1)
print(respon.read())

