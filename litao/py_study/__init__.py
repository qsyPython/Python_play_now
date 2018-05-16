#  @property学习
# @property 这个可以在同一个方法上使用用来区分 get 和 set 方法 @property表示get方法 score.setter表示set方法

class  Stduent(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return ''

    @property
    def score(self):
        return self.name

    @score.setter
    def score(self,name):
        self.name = name


s = Stduent('李泽华',12)
s.score = '李涛'
print(s.score)

# Python支持多继承
class Animal(object):
    pass
class Mannal():
    pass

class Dag(Animal,Mannal):
    pass




# 所有数据基本都可以迭代
# isinstance('abc', Iterable) # str是否可迭代
# true
#打印下标和数据   enumerate
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# 0 A
# 1 B
# 2 C
# 打印两个变量
for i ,value in [(1,1),(2,3)]:
    print(i,value)


#filter  map 测试
def is_add(n):
    return n%2==1

def tesr_map(n):
    return n/2

list3 = list(filter(is_add,[1,2,3,4,5,6,7,7,8,8]))
print('输出filte测试%s'%list3)
list4 = list(map(tesr_map,[1,2,3,4,5,6,7,7,8,8]))
print('输出map测试%s'%list4)



#生成器  一边遍历一边计算 用()表示

list = [x*x for x in range(10)]
g = (1,2,3,4,5,6,444,8)
g2 = (x*x for x in range(10))
# print(list)
# print(g2)
#打印生成器里的内容
for i in g2:
    print(i)


# g3 = (x*y for x in range(10)  for y in range(9))
# for i in g3:
#     print(i)

# fib(6)
# t  = (b,a+b)
# a = b   1
# b = a+b  1
#yield 是在生成器里拦截的方法 类似于break   下次再调用时 从下一个数据接着开始打印
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
next(o)
next(o)
next(o)

#切片操作  用来获取 部分区间下标的数据
list2 = [1,2,3,4,5,6,444,8]
print('这里是切片操作%s'%list2[:3])  #0 可以省略  表示下标 0-2
print('这里是切片操作%s'%list2[1:3])
#字符串也可以用
strs = '李涛测试切片'
print(strs[:3])



# 装饰器
def logs(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@logs
def tes_log():
    print('测试log的打印')

tes_log