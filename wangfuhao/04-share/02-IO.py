#=========================初步认识=====================
# def test1():
#     while True:
#         print("我是任务1")
#         yield None
#
# def test2():
#     while True:
#         print("我是任务2")
#         yield None
#
# t1 = test1()
# t2 = test2()
# while True:
#     t1.__next__()
#     t2.__next__()

#=========================举例使用=====================
# def consumer():
#     tellyou = ''
#     while True:
#         n = yield tellyou
#
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         tellyou = '200 OK'
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         result = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % result)
#     c.close()
#
# c = consumer()
# produce(c)

#=========================asyncio=====================
# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# =========================async/await=====================
'''
为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
把@asyncio.coroutine替换为async；
把yield from替换为await。
'''
# import asyncio
#
#
# async def hello():
#     print("Hello world!")
#     r = await asyncio.sleep(1)
#     print("Hello again!")
#
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# #=========================asyncio实例=====================
# import asyncio
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     writer.close()
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
