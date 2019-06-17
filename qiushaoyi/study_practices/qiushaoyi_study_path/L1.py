import math

'''
	作者：邱少一
	日期：2018/03/06 
	功能：
	 模块1：
     变量和数据类型（变量、字符串、数字、列表、元组、字典、集合）；
     常用语句和基础语法（条件语句如if、while、for和python语法格式）；
     函数(定义、调用、函数的分类及其使用介绍)和高阶函数（map/reduce、filter、sorted等）；
'''

# 1
# print('hello world first my love','jump over','中国有嘻哈','300+200 = ',300+200)
# inputCont = input('请输入你要输入的内容,好吗:')
# print('输入的内容为：',inputCont)
#
#
# print('输出不同格式的字符串:内部使用转义字符‘\‘ntr’’ ',"I'm OK",'I\'m OK','I\'m Qiu\nshao\nhhh\tyi我美吗？',r'''
# =====格式化表示法=====
# line 1 我就是第1行
# ======格式化表示法====
# line 2 我就是第2行
# ======格式化表示法====
# line 3 我就是第3行
#
# ''')
#
# True and True
# False or False
# 5>3 or 1>3
# not True
# not 1>2
#
# age = 3
# if age>18:
#     print('\nadult')
# elif age>6 and age <=18:
#     print('\tteenager')
# else:
#     print(r'''
#     ====u are a baby=====
#     =====================''')
#
# a1 = None,100,300.5,True,'天下无双',['wo是数组',37,78.47,'enhe'],('tianxiawushaung',222,89.00,False,'我爱大中国'),{}

a2 = 'ABC'
a2.replace('A', 'a')
b2 = a2
a2 = 'XYZ'
print(b2)

print(10 / 3, 10 // 3, 10 % 3, ord('A'), chr(66), ord('中'), chr(25991))

print(10 / 3, 10 // 3, 10 % 3, ord('A'), chr(77), ord('种'), chr(7978))

# encode之后变成了bytes，下面x和y就是bytes的形式
x = b'Yuming'
y = b"Chunjiao"
z = b"\xe4\xb8\xad\xe6\x96\x87"
print('uuu'.encode('ascii'), '中文666'.encode('utf-8'), \
      b'ABC'.decode('ascii'), b"\xe4\xb8\xad\xe6\x96\x87".decode('utf-8')
      )
print('Hello,%s,%2d,%.3f,%%%s' % ('World', 3, 1.38587, '7'))
# list
classmates = ['Machael', 'Bob', 'Tracy']
classmates[0]
classmates[:2]
classmates[1:2]
classmates[1:]
classmates[-1]

classmates.sort()  # 全部都是字符串才进行该操作
print('正序排序：', classmates)
classmates.append(78)
classmates.insert(2, ['插入数组', '我也是list'])
classmates.insert(2, '导入字符串数据')
classmates.pop()
classmates.pop(2)
classmates[1] = '933'
classmates * 2
classmates = []
print(classmates)

# tuple
classmate = ('Machael', 'Bob', 'Tracy')
classmate1 = ()
classmate2 = (1,)
classmate3 = ('a', 'b', ['A', 'B'])
classmate3[2][0] = 'X'
classmate3[2][1] = 'Y'

brith = input('请输入你的年龄:')
brith = int()
if not isinstance(brith, (int, float)):
    print('请输入整数!!!')
else:
    if brith > 18:
        print('00前')
    else:
        print('00后')
        pass

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in range(1, 101):  # 1到100的和,左闭右开
    sum = sum + x
print(sum)

d = {'Michael': 98, 'Bob': 23, 'Tracy': 67}
d['Bob']  # d.get('Bob')
d['Michael'] = 104
d['appendData'] = 19999
d.pop('Bob')
print(d)

s = set([2, 3, 5, 2, 1, 3, 2])
s.add(4)
s.remove(4)
s1 = set([2, 1, 3, 4])
s2 = set([2, 3, 5])
print(s, s1 & s2, s1 | s2)

# 类型转换
print(abs(-100), max(12, 56, 88, -125), int('124'), float('12.13'), str(238.5), bool(2), bool(''))


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad opperand type')
    if x >= 0:
        return x
    else:
        return -x
    pass


print(my_abs(-35))


def nop():
    pass


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
    pass


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


def quadratic(a, b, c):
    x1 = (b - b * b + 4 * a * c) / 2 * a
    x2 = (b + b * b + 4 * a * c) / 2 * a
    return x1, x2


x1, x2 = quadratic(1, 2, 1)
print(x1, x2)


def power(x, n):
    sum = 1
    while n > 0:
        n = n - 1
        sum = sum * x
    return sum


sum_pow = pow(2, 10)
print(sum_pow)


def powser_default(x, n=2):  # 默认参数必须是不可变对象：整数、浮点、bool和str
    sum = 1
    while n > 0:
        n = n - 1
        sum = sum * x
    return sum


sum_default_pow = powser_default(3)
print(sum_default_pow)


def add_end(x=[]):
    x.append('woca')
    return x


add_end()
add_end()
x_list = add_end()
print(x_list)


# ================================================================================================ #

def add_end1(x=None):  # 可变对象list、dict需要默认None，内部需初始化为None
    if x is None:
        x = []
    x.append('End')
    return x


add_end1()
add_end1()
print(add_end1())


def person1(name, age, *, city='Beijing', job, test):  # 可变命名关键字参数:该关键字之后的参数，必须传递参数名才行，已默认的参数除外
    print(name, age, city, job, test)


person1('Jake', 13, job='Engineer', test='踢掉')


def calc(*numbers):  # 可变列表参数:自动把参数组装成一个 tuple
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum


print(calc(), calc(*[]), calc(1, 2, 3))
print(calc(*[1, 2, 3]))


def person(name, age, **kw):  # 关键字参数:自动把参数组装成一个 dict
    print('name:', name, 'age:', age, 'other:', kw)


person('Qiu', 'Shaoyi')
person('Qiu', 'Shaoyi', x='帅', y='666')
person('Qiu', 'Shaoyi', **{'city': 'Beijing', 'job': 'Engineer'})


# 混合函数：
def f0(a, b, c=0, *, d, **kw):  # 命名的关键字参数是为了限制调用者可以传入的参数名,如* 后面的d参数就是需要传输 参数名才可被调用。
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)


f0(1, 2, d='111')
f0(1, 2, 3, d='111')
f0(1, 2, 3, d='111', x=99, y='woqu')
f0(1, 2, 3, d='111', **{'x': 99, 'y': 109})


def f1(a, b, c=0, *list1, **dict1):
    print('a=', a, 'b=', b, 'c=', c, 'list1=', list1, 'dict1=', dict1)


f1(1, 2), f1(1, 2, 3), f1(1, 2, 3, 'a', 'b'), f1(1, 2, 3, x=99, y=21), f1(1, 2, 3, 'a', 'b', x=99, y=21), f1(1, 2, 3,
                                                                                                             *['a',
                                                                                                               'b'], **{
        'x': 199, 'y': 299})

# 递归函数



