# Collections模块基本介绍

# 我们都知道，Python拥有一些内置的数据类型，
# 比如str, int, list, tuple, dict等，
# collections模块在这些内置数据类型的基础上，提供了几个额外的数据类型：

# 1.namedtuple(): 生成可以使用名字来访问元素内容的tuple子类
# 2.deque: 双端队列，可以快速的从另外一侧追加和推出对象
# 3.Counter: 计数器，主要用来计数
# 4.OrderedDict: 有序字典
# 5.defaultdict: 带有默认值的字典


# 1、可命名元组(namedtuple)
# 作用：namedtuple主要用来产生可以使用名称来访问元素的数据对象，
# 通常用来增强代码的可读性， 在访问一些tuple类型的数据时尤其好用。
# 创建一个自己的可扩展tuple的类（包含tuple所有功能以及其他功能的类型），在根据类创建对象，然后调用对象
# 最长用于坐标，普通的元组类似于列表以index编号来访问，而自定义可扩展的可以类似于字典的keys进行访问
# 下例列举用collections.namedtuple以及普通元组进行元素调用的实例子。
import collections
# 调用namedtuple方法来定义mytuple的变量，并创建一个名称为['x','y','z']的列表
mytuple = collections.namedtuple('mytuple',['x','y','z'])
# 给mytuple赋值，这里赋值的（3,5,7）是分别赋值给['x','y','z']这个列表中每个元素的。
a = mytuple(3, 5, 7)
print(a)
# 打印结果可以看出赋值的每个值已经传给了列表中对应的每个元素中了。
mytuple(x=3, y=5, z=7)
# 上述我们把mytuple赋给了变量a,所以a=mytuple。那么我们在调用mytuple中的元素时，要使用a.x,a.y,a.z的方式去调用。
print(a.x)
# a.x=3，a.z=7那么再相乘结果为21
print(a.x * a.z)


# 普通tuple调用方法
#生成一个普通的数字元组
#通过上述方法可以看出使用collections
# 模块中的namedtuple方法可以给每个元素起别名，通过名称调用的方式来获取值使用。
# 而普通元组的方法必须通过下标的方式来取值。
mytuple = (3,5,7)
print(mytuple)
# 在做元素调用以及算法计算时，因为元组调用元素
print(mytuple[0]*mytuple[2])

# deque
# 使用list 存储数据时，按照索引访问元素很快，但是插入和删除元素就很慢了，
# 因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈。
from collections import deque
q = deque(['a','b','c'])
q.append('x')    # 默认添加列表最后一项
q.appendleft('y')  # 添加到列表第一项
print(q)
# deque(['y', 'a', 'b', 'c', 'x'])
q.pop()  # 默认删除列表最后一个元素
q.popleft()  # 删除列表的第一个元素
# deque(['a', 'b', 'c'])
print(q)

# defaultdict
# 使用字典时，如果引用的Key不存在，就会抛出 KeyError，如果希望key不存在时，返回一个默认值，就可以用 defaultdict.
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。除了key不存在而返回默认值，其他功能与普通字典无异。
from collections import defaultdict
Mydict = defaultdict(lambda: 'N/A')
Mydict['key1'] = 'abc'
Mydict['key1']    # 字典的key1存在
print(Mydict)
Mydict['key2']    # 字典的key2不存在，返回默认值为‘N/A’
print(Mydict)

# OrderedDict
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
# dict的Key是无序的{'a': 1, 'c': 3, 'b': 2}
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)  # OrderedDict的Key是有序的OrderedDict([('a', 1), ('b', 2), ('c', 3)])
#通过 OrderedDict 可以实现一个FIFO（先进先出）的字典，当容量超出限制后，先删除最早添加的KEY。
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

# Counter
#简单的计数器，例如，统计字符出现的个数。
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
    print(ch)