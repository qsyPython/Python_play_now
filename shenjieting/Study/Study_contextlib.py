
from contextlib import contextmanager
from contextlib import closing
from urllib.request import urlopen

# 在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。正确关闭文件资源的一个方法是使用try...finally：
try:
    f = open('sometext.txt', 'r')
    f.read()
    print("文件名1: ",f.name)
finally:
    if f:
        f.close()

# 写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭，所以上面的代码可以简化为：
with open('sometext.txt', 'r') as f:
    print("文件名2: ",f.name)

# 并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如，下面的class实现了这两个方法：
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin1')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error1')
        else:
            print('End1')

    def query(self):
        print('Query info about 1%s...' % self.name)

# 这样我们就可以把自己写的资源对象用于with语句：
print("*"*30)
with Query('Bob') as q:
    q.query()

# 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：
class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about 2%s...' % self.name)

@contextmanager
def create_query(name):
    print("*" * 30)
    print('Begin2')
    q = Query(name)
    yield q
    print('End2')
'''
yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器
当你调用这个函数的时候，函数内部的代码并不立马执行 ，这个函数只是返回一个生成器对象
当你使用for进行迭代的时候，函数中的代码才会执行
第一次迭代中你的函数会执行，从开始到达 yield 关键字，然后返回 yield 后的值作为第一次迭代的返回值. 
然后，每次执行这个函数都会继续执行你在函数内部定义的那个循环的下一次，再返回那个值，直到没有可以返回的。
'''
# @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：
with create_query('Bob') as q:
    q.query()

# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：
print("*"*30)
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")
'''
代码的执行顺序是：
with语句首先执行yield之前的语句，因此打印出<h1>；
yield调用会执行with语句内部的所有语句，因此打印出hello和world；
最后执行yield之后的语句，打印出</h1>。
因此，@contextmanager让我们通过编写generator来简化上下文管理。
'''
print("*"*30)
# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：
# with closing(urlopen('https://www.baidu.com')) as page:
#     for line in page:
#         print("urlopen:",line)

# closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：它的作用就是把任意对象变为上下文对象，并支持with语句。
# print("*" * 30)
# @contextmanager
# def closing(thing):
#     try:
#         yield thing
#     finally:
#         thing.close()


