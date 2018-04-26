
#collections是Python内建的一个集合模块，提供了许多有用的集合类。
from collections import  namedtuple

from  collections import  deque

from collections import defaultdict

from  collections import OrderedDict

from collections import Counter


#⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
'''
namedtuple
是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
'''
# 一个点的二维坐标就可以表示成：
Point = namedtuple('Point',['x','y'])

p = Point(1,2)
print("namedtuple-----点的坐标：",p.x,p.y)

#验证Point 对象是tuple的一种子类
print("namedtuple-----p是否和Point类型一致",isinstance(p,Point))
print("namedtuple-----p是否和tuple类型一致",isinstance(p,tuple))

#如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
Circle = namedtuple('Circle',['x','y','r'])
c = Circle(10,10,20)
print("namedtuple-----圆的坐标X:{};Y:{};半径:{}".format(c.x,c.y,c.r))

#⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
'''
deque
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，
因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
'''
q = deque(['a','b','c'])
q.append("x")
q.appendleft("y")
print("deque-----",q)
q.pop()
print("deque-----",q)
q.popleft()
print("deque-----",q)

#注：deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

#⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
'''
defaultdict
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
'''
dd = defaultdict(lambda:'error')
dd['key1'] = 'abc'
print("defaultdict-----",dd['key1'])
print("defaultdict-----",dd['key2'])

#注：默认值是调用函数返回的，而函数在创建defaultdict对象时传入。除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。

#⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
'''
OrderedDict
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict：
'''
oo = dict([('a',1),('b',2),('c',3)])
print("OrderedDict-----",oo)
# OrderedDict的Key是有序的
od = OrderedDict([('a',1),('b',2),('c',3)])
print("OrderedDict-----",od)


odd = OrderedDict()
odd['z'] = 1
odd['y'] = 2
odd['x'] = 3
odd["z"] = 4
print(odd.keys())# 按照插入的Key的顺序返回

#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：

class LastUpdataOrdereDict(OrderedDict):
    def __init__(self , capacity):#init方法在父类OrderedDict的__init__方法基础上，为LastUpdatedOrderedDict类添加了一个_capacity属性
        super(LastUpdataOrdereDict,self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value): #setitem实现了在为LastUpdatedOrderedDict实例添加key的时候，先检查是否超出容量；三个顺序判断分别实现：
        if key in self :
            del self[key]
            print("OrderedDict-----set:", (key, value))  #如果已存在key，则取代
        else:
            if len(self)  == self._capacity:
                last =self.popitem(last=False) #如果超出容量，则pop出最早添加的Key
                print('OrderedDict-----remove:', last)
            else:
                print("OrderedDict-----add:", (key, value)) #如果不存在key，则添加
        OrderedDict.__setitem__(self,key,value)
print(odd)
las = LastUpdataOrdereDict(odd)
print(odd)


'''
Counter
Counter是一个简单的计数器，例如，统计字符出现的个数：
Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。
'''
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print("Counter-----",c)

