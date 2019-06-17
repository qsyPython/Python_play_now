#!/usr/bin/env python3 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# -*- coding: utf-8 -*- 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
# 少
import math, os, functools, sys
from collections import Iterable
from collections import Iterator
from operator import itemgetter
from functools import reduce

print('hello world first my love', 'jump over', '中国有嘻哈', '300+200 =', 300 + 200)
inputCon = input('请输入您要输入的内容，ok：')
print('输入的内容是:', inputCon)

print('输出字符串: 在内部使用转义字符\ ', "I'm OK", 'I\'m "OK"!', 'I\'m \'Qiu\nshao\tyi\'!', r'''
=====格式化表示法========
	line1
=====================
	line2
=====================
	line3''')

r'''
判断运算符
'''
True and True
False or False
5 > 3 or 1 > 3
not True
not 1 > 2

age = 19
if age >= 18:
    print('adult')
else:
    print('teenager')
    pass

# 可赋值的数据类型
a1 = None, 100, 300.5, True, '天下无双', ['dsjg', '8884', '我就是测测'], ('tianxia', '你就是测测而已', '6666'), {23: '就是这个feel',
                                                                                                 '看看': 656}

# 变量指针重指向: 该打印 ABC
a2 = 'ABC'
a2.replace('a', 'A')
b2 = a2
a2 = 'XYZ'
print(b2)
# Python是UNICode编码。单字符编码  用ord和chr可实现key和value的切换查看 
print(10 / 3, 10 // 3, 10 % 3, ord('A'), chr(66), ord('中'), chr(25991))

# bytes类型的数据用带b前缀的单引号或双引号表示：该bytes类型特点是每个字符占用一个字节，所以必须是大小写的英文、数字和一些特殊符号，也就是bytes使用的是ASCII编码
x = b'Yuming'
# 字符的编码encode(） 和 字符的解码decode()：网络或磁盘上读取了字节流，那么读到的数据就是bytes，也就是以b开头，但b不作为字符
print('uuu'.encode('ascii'), '中文666'.encode('utf-8'), b'ABC'.decode('ascii'),
      b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# %运算符就是用来格式化str的:字符串内部，%s表示用字符串替换，%d表示用整数替换，%f表示浮点数, 有几个%?占位符;在字符串外部。 %%表示转义字符%
print('Hello,%s,%2d,%.3f,%%%s' % ('World', 3, 1.38587, '7'))

# list tuple
classmates = ['Machael', 'Bob', 'Tracy']
classmates[0]
classmates[:2]
classmates[1:2]
classmates[1:]
classmates[-1]
classmates.append(78)
classmates.insert(2, ['插入新数据', '我也是list'])
classmates.pop()
classmates.pop(2)
classmates[1] = '999'
classmates * 2
classmates = []

classmate = ('Machael', 'Bob', 'Tracy')
classmate1 = ()
classmate2 = (1,)  # 防止和自然数1的表示发生冲突 classmate = (1)，通常会在表示一个元素时在末尾加上,
classmate3 = ('a', 'b', ['A', 'B'])
classmate3[2][0] = 'X'
classmate3[2][1] = 'Y'  # 内部可变的元素经过修改后，最后的结果classmate = ('a','b',['X','Y'])

# if 条件语句
age = 20
if age > 10:
    print('your age is %d,老年人你好' % age)
elif age <= 10 and age < 3:
    print('你年轻你说啥都对')
else:
    print('小盆友，鉴定完毕')
    pass

# 少：待解决 若输入的不是数字，就会出现报错
birth = input('请输入年龄:')
births = int(birth)
if births < 2000:
    print('00前')
else:
    print('00后')
    pass

# for in 循环语句
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
    pass

sum = 0
for x in range(1, 101):  # 计算1到100的和
    sum = sum + x
print(sum)

for x in range(0, 5):
    print(x)

# dict
d = {'Michael': 98, 'Bob': 23, 'Tracy': 67}
d['Bob']
d.get('Bob')
d['Michael'] = 104
d.pop('Bob')

# set 集合
s = set([1, 2, 3, 1, 2, 3])
s.add(4)
s.remove(4)
s1 = set([1, 2, 3, 4])
s2 = set([2, 3, 5])
print(s, s1 & s2, s1 | s2)

alist = ['c', 'a', 'b']
alist.sort()
print('最新的排序: ', alist)

print(abs(-100), max(12, 56, 88, -125), int('124'), float('12.34'), str(238.5), bool(2), bool(''))


# 基本的函数设计
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad opperand type')
    if x >= 0:
        return x
    else:
        return -x
    pass


my_abs(-235)


# 空函数
def nop():
    pass


# 多返回值的函数：函数可以同时返回多个值，但其实就是一个tuple 元祖
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
    pass


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


def quadratic(a, b, c):
    x1 = (b - (b * b - 4 * a * c)) / 2 * a
    x2 = (b + (b * b - 4 * a * c)) / 2 * a
    return x1, x2


x1, x2 = quadratic(1, 2, 1)
print(x1, x2)


# 计算x的n次方函数(n>0)
def power(x, n):
    sum = 1
    while n > 0:
        n = n - 1
        sum = sum * x
    return sum


print(power(2, 10))


# 含有默认参数：默认参数必须指向不变对象（整数、bool、浮点和str ）
def powerDefault(x, n=2):
    sum = 1
    while n > 0:
        n = n - 1
        sum = sum * x
    return sum


print(powerDefault(3))


# 若 默认参数 为可变list：会记录到该可变对象，造成数据累加的错误，所以一般不要这么处理. 如下：解决办法为默认的参数传 None
def add_end(x=[]):
    x.append('End')
    return x


add_end()
add_end()
print(add_end())  # ['End', 'End', 'End']


def add_end1(x=None):
    if x is None:
        x = []
    x.append('End')
    return x


add_end1()
add_end1()
print(add_end1())  # ['End']


# 可变参数:形参是tuple，不是list：解决了上面所说传递的参数是可变的list的问题。  通过 *list 方式作为参数来从传递
# 本质上：可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


calc(1, 2, 3)  # 14
calc()  # 0
nums = [1, 2, 3]
calc(*nums)  # 14 *nums表示把nums这个list的所有元素作为tuple可变参数传进去


# 关键字参数：解决了上面所说传递参数是可变的dict的问题 。 通过 **dict 方式作为参数来从传递
# 本质上：允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Qiu', 30, **extra)


# 命名关键字参数: 命名的关键字参数是为了限制调用者可以传入的参数名。 因此调用时，命名关键字参数必须传入参数名,否则会报错
def person1(name, age, *, city='Beijing', job):
    print(name, age, city, job)


print(person1('Jake', 23, job='Engineer'))


# Python函数可以传递的参数：必选参数、默认参数、可变参数、关键字参数和命名关键字参数。参数定义的顺序必须是：必选参数、默认参数、可变参数、关键字参数和命名关键字参数
# Python解释器自动按照参数位置和参数名把对应的参数传进去。
def f1(a, b, c=0, *list1, **dict):  # 含有必选参数、默认参数、可变参数、关键字参数
    print('a=', a, 'b=', b, 'c=', c, 'list1=', list1, 'dict=', dict)


f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 'a', 'b')  # 或用list1= ['a','b']  f1(1,2,3,*list1)
f1(1, 2, 3, x=99, y='woqu')  # dict1= {'x': 99, 'y': 'woqu'}  f1(1,2,3,**dict1)
f1(1, 2, 3, 'a', 'b', x=99, y='woqu')


def f2(a, b, c=0, *, d, **kw):  # 含有必选参数、默认参数、命名关键字参数、关键字参数
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f2(1, 2, d=99)
f2(1, 2, 3, d=99)
f2(1, 2, 3, d=99, ext='来一发')


# 递归函数：函数内部调用自身，不同的是参数变化而已
# 递归会带来栈溢出：在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的。会导致栈的溢出。

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))

# 解决递归调用栈溢出的方法,尾递归优化：在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。然后并没有卵用，因为python解释器内部并没有进行内存处理
# def fact1(n):
# 	return fact_iter1(n,1)

# def fact_iter1(num,product):
# 	if num == 1:
# 		return product
# 	return fact_iter1(num-1,num*product)
# fact(1000000)

# 切片: str、dict、list 以index, nums为基础（注：）
li = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
li[1:2]  # ['Sarah'] index 为1,nums 为1
li[:2]  # ['Michael','Sarah'] index 为0,nums 为2
li[-1] == li[4]
li[-2:-1]  # ['Bob'] index 为-2,nums 为1
li[-2:]  # ['Bob','Jack'] index 为-2,nums 为2

tu = (0, 1, 2, 3, 4, 5)
tu[:3]  # (0,1,2)
tu[-2:-1]  # (4)
tu[-2:]  # (4,5)

str = 'ABCDRFTG'
str[:3]  # 'ABC'
str[-2:-1]  # 'T'
str[-2:]  # 'TG'

# 迭代:dict
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)

if isinstance(d, Iterable):  # 判断str、list、dict是否可迭代
    for k, v in d.items():
        print(k, v)
else:
    pass

# 迭代：list
dd = ['A', 'B', 'C']
if isinstance(dd, Iterable):  # 判断str、list、dict是否可迭代
    for i, v in enumerate(dd):
        print(i, v)
else:
    pass

d1 = '456'
if isinstance(d1, Iterable):  # 判断str、list、dict是否可迭代
    for x in d1:
        print(x)
else:
    pass

for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)

# 生成[1x1, 2x2, 3x3, ..., 10x10]
L2 = []
for x in range(1, 11):
    L2.append(x * x)

L3 = [x * x for x in range(1, 11)]
L4 = [d for d in os.listdir('.')]

print(L2, L3, L4)
# 生成器：一边循环一边计算的机制，称为生成器：generator。如下
generator1 = (x * x for x in range(1, 11))
print(generator1)
for x in generator1:
    print(x)


# next(generator1)#一旦生成器generator1打印完全，再调用next(generator1)就会抛出异常
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# 迭代器:数组、字典、字符串、生成器都可以发生迭代，但不都是迭代器。可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator(特点：所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算)。生成器都是Iterator对象。
if isinstance([], Iterator):  # false
    pass
if isinstance({}, Iterator):  # false
    pass
if isinstance('', Iterator):  # false
    pass
if isinstance((x for x in range(10)), Iterator):  # True
    pass
if isinstance(100, Iterator):  # false
    pass
# list、dict、str都不是Iterator,但可以通过iter()函数转换
if isinstance(iter([]), Iterator):
    pass
if isinstance(iter({}), Iterator):
    pass
if isinstance(iter(''), Iterator):
    pass

# for 循环本质：不断调用next() 
for x in range(1, 6):
    pass
it = iter(range(1, 6))
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

x = abs(-10)
f = abs  # 变量可以指向函数,函数名本身就是变量！！
y = f(-10)
if x == y:
    print('变量可以指向函数，并且可以调用函数')


# 函数名本身就是变量！！！对该变量重新赋值会造成什么结果？再次以函数形式调用的话会出错
# abs = 10
# abs(-100)

# 高阶函数: 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数，如map、reduce、filter、sorted。
def add(x, y, f):
    return f(x) + f(y)


val = add(-5, -9, abs)
print('val:', val)


def f(x):
    return x * x


# map()和reduce()函数: 接收两个参数，一个是函数，一个是Iterable，返回的是一个。reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
r1 = map(f, range(1, 10))
r2 = map(str, range(1, 10))
print('返回的是Iterator：', r1, '返回的也是Iterator：', r2)


def add(x, y):
    return x + y


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print(reduce(add, [1, 3, 5, 7, 9]), reduce(fn, map(char2num, '13579')))


# 少：filter：过滤
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, range(1, 11))))  # 保留奇数


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', 'B', 'C', None, ' '])))  # 过滤掉空格和空值


def _odd_iter():  # 少，这个算法牛B。素数:filter求素数
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


primeList = []
for n in primes():  # 打印1000以内的所有素数
    if n < 1000:
        primeList.append(n)
    else:
        break

print(primeList)

# sorted ():过滤函数
sortedL1 = [36, 5, -12, 9, -21]
sortedL2 = ['bob', 'about', 'Zoo', 'Credit']


def keyLower(string):
    return string.lower()


sorted(sortedL1)  # 升序
sorted(sortedL1, reverse=True)  # 降序
sorted(sortedL1, key=abs)  # 按绝对值大小排序,key可为自定义的排序规则

sorted(sortedL2)  # 对字符串排序，是按照ASCII的大小进行升序
sorted(sortedL2, key=keyLower)  # 忽略大小写ASCII的影响，可以统一key转为小写后的函数再排序
sorted(sortedL2, key=keyLower, reverse=True)
print(sorted(sortedL1), sorted(sortedL1, reverse=True), sorted(sortedL1, key=abs), sorted(sortedL2),
      sorted(sortedL2, key=keyLower), sorted(sortedL2, key=keyLower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]  # 按照名字排序


def by_name(t):
    return t[0].lower()


def by_age(t):
    return t[1]


L2 = sorted(L, key=by_name)  # 添加后位降序：reverse = True
L3 = sorted(L, key=by_age)  # 添加后位降序：reverse = True
print(L2, L3)


# 返回函数:返回的结果是一个函数.闭包：函数内部套着一函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


layz_f = lazy_sum(1, 3, 5, 7,
                  9)  # 在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”
print(layz_f, layz_f())


def count():
    fs = []
    for i in range(1, 4):
        def f():  # 每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了
            return i * i

        fs.append(f)
    return fs


f11111, f22222, f333333 = count()  # 因为该函数是循环，所以会返回list，包含3个元素


def count21():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f21, f22, f23 = count21()
print(f11111(), f21())

# 匿名函数:x:返回值
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))  # lambda x:x*x 本质上 def f(x):return x*x
lamF = lambda x: x * x
print(lamF, lamF(6))


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log  # 添加打印调用某个函数的功能
def now(testStr):
    print('208598-237895-33', testStr)


f = now  # 变量指向
f('我就是邱少依')

# 偏函数:functools.partial就是帮助我们创建一个偏函数
int('12345', base=8)  # 转换10进制为8进制
int2 = functools.partial(int, base=8)  # 等同函数：转换10进制为8进制。第1个参数为返回值，第2个参数是把该参数作为传递给上面原函数
int3 = functools.partial(max, 100)  # 把100作为参数传递给max函数
print('我就测试下转为2进制的数', int('12345', base=8), int2('12345'), int3(12, 34, 50, 89))
