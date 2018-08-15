# 异步IO：

# 同步IO: 一旦遇到IO操作，如读写文件、发送网络数据时，就需要等待IO操作完成，才能继续进行下一步操作。
# CPU的速度远远快于磁盘、网络等IO

'''
==========================practice 0: 同步IO ==========================
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
==========================practice 1: 协程 ==========================
整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”！！！
Python的yield不但可以返回一个值，它还可以接收调用者发出的参数
'''
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) # 切换到consumer执行
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)