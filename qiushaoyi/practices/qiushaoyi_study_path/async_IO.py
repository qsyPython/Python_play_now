# 异步IO：


'''
==========================practice 0: 同步IO ==========================
就是顺序执行：
同步IO: 一旦遇到IO操作，如读写文件、发送网络数据时，就需要等待IO操作完成，才能继续进行下一步操作。
'''
# def do_some_code(r):
#     return r
#
# f = open('/path','r')
# r = f.read()# <== 线程 停在此处等待IO操作结果
# do_some_code(r) # <== IO操作完成后线程才能继续执行


'''
==========================practice 1: 异步IO：消息循环 ==========================
loop = get_event_loop()
while True:
    event = loop.get_event()
    process_event(event)
'''

'''
===============重点看===========practice 2: 协程 ==========================
整个流程无锁，并且由1个线程执行，produce和consumer协作完成任务，所以称为“协程”！！！
# 但CPU的速度 远远快于 磁盘、网络等IO
Python的yield不但可以返回一个值，它还可以接收调用者发出的参数！！！

方法切换：函数名.send()
yield：暂停当前函数执行，切回到原函数执行
'''

# def consumer():
#     r = ''
#     while True:
#         n = yield r #切回到produce执行
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n) # 切换到consumer函数执行
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
# c = consumer()
# produce(c)


'''
==========================practice 3: asyncio：单线程的IO：基本使用 ==========================
异步IO：单线程中的处理方式！！！
'''
# A、tasks为重复的某任务（函数）：几乎是同步执行
# import asyncio,threading
# @asyncio.coroutine
# def hello():
#     print('hello,world',threading.current_thread())
#     r = yield from asyncio.sleep(3)#asyncio.sleep()也是一个coroutine,是耗时3秒的IO操作
#     print('hello ,again',threading.current_thread())
#
# #获取异步IO的消息循环：event_loop
# loop = asyncio.get_event_loop()
# tasks = [hello(),hello()] #可以放很多函数的那种，几乎是同步执行
# loop.run_until_complete(asyncio.wait(tasks))
# # loop.run_until_complete(hello())
# loop.close()


# B、tasks为不同参数的任务（函数）：随机执行
# 获取某host请求connect中header中的数据，通过coroutine执行并发的

# import asyncio
# # @asyncio.coroutine
# def wget(host):
#     print('wget %s...'%host)
#     connect = asyncio.open_connection(host,80)
#     reader,writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host,line.decode('utf-8').rstrip()))
#         writer.close()
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

'''
==========================practice 4: asyncio：单线程的IO：Python 3.5的新语法 ==========================
asyncio:实现单线程并发IO操作，常用于客户端
'''

# import asyncio
# @asyncio.coroutine  #可替换为async
# def hello():
#     print('hello world')
#     r = yield from asyncio.sleep(1)
#     print('hello again!')

# 等效于下面👇👇👇👇👇
# import asyncio
# async def hello():
#     print('hello world!!!')
#     r = await asyncio.sleep(1)
#     print('hello again!!!')
#
# loop = asyncio.get_event_loop()
# tasks = [hello(),hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

'''
==========================practice 5: aiohttp: 基于asyncio实现的HTTP框架 ==========================
'''
import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()