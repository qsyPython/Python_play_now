# print('------------------fork------------------------')
# import os
# import time
# '''
# fork可以创建一个新的进程
# '''
# ret = os.fork() #他有两个返回值,会区分父子进程,主进程的ret>0  子进程的ret==0
# '''
# 父进程中fork的返回值,就是刚刚创建出来子进程的id
# '''
# print(ret)  # 855456 0  85546是主进程创造一个子进程后,子进程所在的进程是85546
# '''
# 注意:但你不能说这个ret == 855456 > 0  是主进程创建的子进程id 那就应该代表子进程才对呀? 你下边的判断是不是反了
# 这里一定要注意,区分父子进程 只看ret是否==0,ret等于0 就是子进程, ret > 0  就是父进程  而ret==855456只是说创建的子进程id是85546,不能作为区分父子进程
# '''
# if ret > 0:
#     while True:
#         print("----父进程---%d"%os.getpid()) #getpid打印出当前的进程 比如是85545
#         time.sleep(1)
# else:
#     while True:
#         print("----子进程---%d-%d"%(os.getpid(),os.getppid()))  #父进程创建出子进程 所以getppid打印他的父进程就是85545 而自己所在的进程的是85546
#         time.sleep(1)

# print("------------------Process创建进程------------------")
#fork不跨平台,不常用,用Process
# from multiprocessing import Process
#
# import time
#
# def test():
#     while True:
#         print("---test---")
#         time.sleep(1)
#
# p = Process(target=test)
# p.start() #让这个进程开始执行test函数里的代码
#
# while True:
#     print("---main---")
#     time.sleep(1)

# print("------------------进程池------------------")
# from multiprocessing import Pool
# import os
# import random
# import time
#
# def worker(num):
#     for i in range(5):
#         print("===pid=%d==num=%d="%(os.getpid(), num))
#         time.sleep(1)
#
# #3表示 进程池中对多有3个进程一起执行
# pool = Pool(3)
#
# for i in range(10):
#     print("---%d---"%i)
#     #向进程池中添加任务
#     #注意：如果添加的任务数量超过了 进程池中进程的个数的话，那么不会导致添加不进入
#     #       添加到进程中的任务 如果还没有被执行的话，那么此时 他们会等待进程池中的
#     #       进程完成一个任务之后，会自动的去用刚刚的那个进程 完成当前的新任务
#     # pool.apply_async(worker, (i,))  #非阻塞的方式
#     pool.apply(worker, (i,))#堵塞的方式
#
#
# pool.close()#关闭进程池，相当于 不能够再次添加新任务了
# pool.join()#主进程 创建／添加 任务后，主进程 默认不会等待进程池中的任务执行完后才结束
#             #而是 当主进程的任务做完之后 立马结束，，，如果这个地方没join,会导致
#             #进程池中的任务不会执行

# print("------------------Queue------------------")
# # #在父进程中创建两个子进程,一个往Queue里写数据,一个从Queue里读数据
# from multiprocessing import Process,Queue
# import os,time,random
#
# #写数据进程执行的代码
# def write(q):
#     for value in ['A','B','C']:
#         print("put %s to queue"%value)
#         q.put(value)
#         time.sleep(random.random())
#
# #读数据进程执行的代码
# def read(q):
#     while True:
#         if not q.empty():
#             value = q.get(True)
#             print("get %s from queue"%value)
#             time.sleep(random.random())
#         else:
#             break
#
# if __name__ == '__main__':
#     #父进程创建Queue,并传给各个子进程
#     q = Queue()
#     pw = Process(target=write,args=(q,))
#     pr = Process(target=read,args=(q,))
#
#     #启动子进程,写入
#     pw.start()
#     #等待pw结束:
#     pw.join()
#
#     #启动子进程pr,读取
#     pr.start()
#     pr.join()
#     print("所有数据都写入并且读完")

#++++++++++++++++++++++++++++++++++++线程++++++++++++++++++++++++++++++++++++
# print("------------------01-使用线程完成多任务------------------")
# # #可以明显看出使用了多线程并发的操作,花费时间要短很多
# # #创建好的线程,需要调用start()方法来启动
# from threading import Thread
# import time
#
# #如果多个线程执行的都是同一个函数的话，各自之间不会有影响，各是个的
# def test():
#     print("哈哈哈哈")
#     time.sleep(1)
#
# if __name__ == '__main__':
#     for i in range(5):
#         t = Thread(target = test)
#         t.start()

# print("------------------03-线程的执行顺序------------------")
# # import threading
# # import time
# #
# # class MyThread(threading.Thread):
# #     def run(self):
# #         for i in range(3):
# #             time.sleep(1)
# #             msg = "I'm "+self.name+' @ '+str(i)
# #             print(msg)
# # def test():
# #     for i in range(5):
# #         t = MyThread()
# #         t.start()
# # if __name__ == '__main__':
# #     test()

print("------------------08-使用互斥锁------------------")
# from threading import Thread, Lock
# import time
#
# g_num = 0
#
# def test1():
#     global g_num
#     #这个线程和test2线程都在抢着　对这个锁　进行上锁，如果有1方成功的上锁，那么导致另外
#     #一方会堵塞（一直等待）到这个锁被解开为止
#     mutex.acquire()
#     for i in range(1000000):
#         g_num += 1
#     mutex.release()#用来对mutex指向的这个锁　进行解锁，，，只要开了锁，那么接下来会让所有因为
#                     #这个锁　被上了锁　而堵塞的线程　进行抢着上锁
#
#     print("---test1---g_num=%d"%g_num)
#
# def test2():
#     global g_num
#     mutex.acquire()
#     for i in range(1000000):
#         g_num += 1
#     mutex.release()
#
#     print("---test2---g_num=%d"%g_num)
#
# #创建一把互斥锁，这个锁默认是没有上锁的
# mutex = Lock()
#
# p1 = Thread(target=test1)
# p1.start()
#
# p2 = Thread(target=test2)
# p2.start()

# #print("------------------11-同步的应用-----------------")
# #多个线程有序执行
# from threading import Thread,Lock
# from time import sleep
#
# class Task1(Thread):
#     def run(self):
#         while True:
#             if lock1.acquire():#可以上锁
#                 print("------Task 1 -----")
#                 sleep(0.5)
#                 lock2.release()
#
# class Task2(Thread):
#     def run(self):
#         while True:
#             if lock2.acquire():
#                 print("------Task 2 -----")
#                 sleep(0.5)
#                 lock3.release()
#
# class Task3(Thread):
#     def run(self):
#         while True:
#             if lock3.acquire():
#                 print("------Task 3 -----")
#                 sleep(0.5)
#                 lock1.release()
#
# #使用Lock创建出的锁默认没有“锁上”
# lock1 = Lock()
# #创建另外一把锁，并且“锁上”
# lock2 = Lock()
# lock2.acquire()
# #创建另外一把锁，并且“锁上”
# lock3 = Lock()
# lock3.acquire()
#
# t1 = Task1()
# t2 = Task2()
# t3 = Task3()
#
# t1.start()
# t2.start()
# t3.start()