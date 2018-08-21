'''
	作者：邱少一
	日期：2018/03/06
	功能：
	python版本：python3 --version
	选择的Web框架：异步的框架aiohttp：pip3 install aiohttp
	前端模板引擎jinja2：pip3 install jinja2
	MySQL的Python异步驱动程序aiomysql：pip3 install aiomysql


0、
Web框架：基于asyncio的aiohttp

1、HTTP请求的流程3步走：
#
# 步骤1：浏览器首先向服务器发送HTTP请求，请求包括：
#
# 请求方式：GET还是POST，GET仅请求资源，POST会附带用户数据；
# 域名：由Host头指定：Host: www.sina.com.cn
# 路径：/full/url/path；
# Header：其他相关的Header；
# 如果是POST，那么请求还包括一个可选的Body，包含用户数据。
#
# 步骤2：服务器向浏览器返回HTTP响应，响应内容包括：
#
# 响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；
# 响应类型：由Content-Type指定；
# Header：以及其他相关的Header；
# 通常服务器的HTTP响应会携带内容，也就是有一个Body：包含响应的内容，网页的HTML源码就在Body中。
#
# 步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2。

2、
async：使用场景 -> 异步网络操作、并发、协程！！！等效于 @asyncio.coroutine
await： 用于挂起阻塞的异步调用接口 ！！！ 等效于 yield from

'''

import logging;logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time,socket
from datetime import datetime
from aiohttp import web,web_runner

# body：为显示html的body，要不然一片空白
# 内容类型为text/html，要不然会被当做file执行下载；
# body中字符的编码charset：utf-8，要不然中文会乱码
def index(request):
    logging.info('server response...')
    return web.Response(body='<h1> Awesome </h1>',content_type='text/html',charset='utf-8')

def hello(request):
    logging.info('我要访问接口了...')
    hello_text = '<h1> 我就是帅,哈哈哈 </h1>'
    return web.Response(body=hello_text,content_type='text/html',charset='utf-8')

async def init(loop):

    # 给web app添加路由
    app = web.Application(loop=loop)
    app = web_runner.AppRunner(app=app).app
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello',hello)
    logging.info('server before...')

    # 创建1个服务器对象
    host = '127.0.0.1'
    port = 9300
    server = await loop.create_server(app.make_handler(),host,port)
    logging.info('server start at http://%s:%s'%(host,port))
    return server

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever() # server 才会执行listen
