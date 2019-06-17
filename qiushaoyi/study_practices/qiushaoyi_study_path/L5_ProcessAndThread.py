'''
多任务的实现有3种方式：线程是最小的执行单元，而进程由至少一个线程组成
1、多进程模式；
2、多线程模式；
3、多进程+多线程模式
多任务模式： 设计Master-Worker模式，Master负责分配任务，Worker负责执行任务
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。
普通的函数调用，调用一次，返回一次。
但fork()调用1次，返回2次，操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回

'''

import os, time, random
from multiprocessing import Process, Pool, Queue
import subprocess
import threading
import multiprocessing

import queue
from multiprocessing.managers import BaseManager

# 1.进程: 创建进程方法2种：fork 和 Process
# 1.1 fork()
pid = os.fork()  # current process（父进程） 复制一份进程 称为 ===子进程===。并把该子进程分别返回给current process父进程、子进程中
if pid == 0:  # 在父进程内，子进程中该pid永远为0
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:  # 在子进程内 首先进入该进程的condition
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# 1.2 Process(target = run_proc, args = ('test',))
def run_proc(name):
    print('Run child process %s(%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    p.start()
    p.join()  # 等待子进程执行完毕,执行主线程
    print('Child process end.')


# 1.3.进程池来管理子进程:
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(multiprocessing.cpu_count())  # Pool的默认大小是CPU的核数。这个会随着CPU数变化
    for i in range(multiprocessing.cpu_count() + 1):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()  # 等待所有子进程执行完毕
    print('All subprocesses done.')

# 1.4子进程执行
print('$ nslookup www.baidu.com')
r = subprocess.call(['nslookup', 'www.baidu.com'])
print('Exit code:', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\nbaidu.com\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)


# 1.5进程间通信
def write(q):
    print('Process to write:%s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read:%s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    q = Queue()  # 父进程创建一个Queue，并传给各个子进程
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()  # 启动子进程pw，写入:
    pr.start()  # 启动子进程pr，读取:
    pw.join()  # 等待pw结束:
    pr.terminate()  # pr进程里是死循环，无法等待其结束，只能强行终止


# 2.线程：
# 2.1创建线程
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s end...' % threading.current_thread().name)


print('首先执行 thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')  # 创建一个子线程name为LoopThread
t.start()  # 启动子线程t
t.join()  # 等待t结束
print('最后执行thread %s ended...' % threading.current_thread().name)

'''
2.2多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响。而多线程中，所有变量都由所有线程共享
任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱

看个线程抢变量的例子：原因在于 线程的调度是由操作系统决定，balance = balance + n
	balance = balance - n 这2个过程在高级语言中，其实是先加入临时变量x，然后再执行赋值。
	2个线程交错进行，所以就可能错乱。
	所以，必须保证一个线程在修改变量时，其他线程不能访问
'''
balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(1000000):
        lock.acquire()  # 先要获取锁
        try:
            change_it(n)
        except Exception as e:
            raise e
        finally:
            lock.release()  # 改完了一定要释放锁


t1 = threading.Thread(target=run_thread, name='Run_thread1', args=(5,))
t2 = threading.Thread(target=run_thread, name='Run_thread2', args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('我就是看看我加锁了，多线程运行是否正确:', balance)

'''
2.3解释器执行代码时，有一个GIL锁：Global Interpreter Lock.Python解释器由于设计时有GIL全局锁
这个GIL全局锁实际上把所有线程的执行代码都给上了锁,多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核.
解决办法：可以通过多进程实现多核任务
下面是个死循环，但是电脑还是不会崩，就是上面的解释。
'''


def loop():
    x = 0


# while True:
# x = x + 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()


# 3.ThreadLocal: 解决若用全局变量必须加锁，若是线程内的局部变量，会造成每层都得作为参数传递的麻烦
# 解决方案1：全局dict key 为当前线程  value为要保存的局部变量
# 解决方案2：ThreadLocal:解决了参数在一个线程中各个函数之间互相传递的问题
class Student(object):
    def __init__(self, name):
        super(Student, self).__init__()
        self.name = name


def process_student(name):
    std = Student(name)
    do_task_1(std)
    do_task_2(std)


def do_task_1(std):
    do_stutask_1(std)
    do_stutask_2(std)


def do_task_2(std):
    do_stutask_1(std)
    do_stutask_2(std)


def do_stutask_1(std):
    print('传递局部变量，就问你累不累')


def do_stutask_2(std):
    print('没看见吗？累成狗啊')


# 解决方案1
global_dict = {}


def std_thread(name):
    std = Student(name)
    global_dict[threading.current_thread()] = std
    do_task_11()
    do_task_22()


def do_task_11():
    # 不传入std，而是根据当前线程查找
    std = global_dict[threading.current_thread()]


def do_task_22():
    std = global_dict[threading.current_thread()]


# 解决方案2：threadLocal
local_school = threading.local()  # 创建全局ThreadLocal对象,不用管理锁的问题，ThreadLocal内部会处理


def process_student():
    std = local_school.student
    print('Hello ,%s(in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# 多进程和多线程比较：多任务 master-worker模式。
# 1、多进程中，主进程为master，其他子进程为worker，子进程挂掉不影响其他进程，除非主进程自身挂掉：应用 Apache服务器，执行效率低，稳定性高
# 2、多线程中，主线程为master，其他子线程为worker，任意一线程挂掉，整个进程就会挂掉：应用 微软的IIS服务器，执行效率高，稳定性差
# 3、多进程和多线程：
# a、计算密集型任务，消耗CPU资源，最好用C语言编写，运行效率高，计算密集型任务同时进行的数量应当等于CPU的核心数。
# b、IO密集型：99%的时间都花在IO上，花在CPU上的时间很少，所以运行效率节省CPU的时间没什么意义，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差
# c、异步IO:CPU和IO执行速度的强大差异，操作系统提供的异步IO，单进程单线程模型来执行多任务，也称 事件驱动模型。Nginx就是支持异步IO的Web服务器

# 4、分布式进程:有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？
'''
在Thread和Process中，应当优选Process，因为Process更稳定
Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上
'''

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()
