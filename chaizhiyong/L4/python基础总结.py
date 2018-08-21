#本次分享主要针对Pyhton的3.0版本，由于时间有限，内容侧重于函数、类（metaclass）、

#1、变量
#变量作为储存在内存中的值。这就意味着在创建变量时会在内存中开辟一个空间
#基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中


#变量赋值

counter = 100   #整型
miles = 1000.0  #浮点
name = "qlk"    #字符串

#多个变量赋值
#Python允许你同时为多个变量赋值。例如：
a = b = c = 1
#也可以为多个对象指定多个变量。例如：
a, b, c = 1, 2, "john"

#2、字符串
#字符串是 Python 中最常用的数据类型。我们可以使用引号('或")来创建字符串。
var1 = 'Hello World!'
var2 = "Hello World!"

#Python不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
#Python访问子字符串，可以使用方括号来截取字符串，如下实例：

var = 'Hello World!'
print(var[0])
print(var[1:5])
print(var1[:6])

#3、列表
#序列都可以进行的操作包括索引，切片，加，乘，检查成员。
#列表的数据项不需要具有相同的类型
#创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：
list = ['physics', 'chemistry', 1997, 2000]

#访问列表中的值 例如：

print("list[0]: ", list[0])

#更新列表
#可以使用append()方法来添加列表项

list = []          ## 空列表
list.append('hello')   ## 使用 append() 添加元素
list.append('world')
print(list)

#删除列表元素
list = ['physics', 'chemistry', 1997, 2000]
del list[2]
print(list) #['physics', 'chemistry', 2000]

#列表运算操作符

print(len([1,2,3])) #获取列表长度 3
print([1,2,3]+[4,5,6]) #组合 [1, 2, 3, 4, 5, 6]
print(['Hi！',]*4)  # 重复 ['Hi!', 'Hi!', 'Hi!', 'Hi!']
print(3 in [1,2,3]) # 元素是否存在于列表中 true
for x in [1,2,3]:
    print(x)    #迭代 1，2，3

#列表截取


list = ['physics', 'chemistry', 1997, 2000]

print(list[2]) # 读取列表中第三个元素
print(list[-2]) #读取列表中倒数第二个元素
print(list[1:]) #从第二个元素开始截取列表

#其他列表函数
#cmp(list1, list2)  比较两个列表的元素  len(list) 列表元素个数 max(list)  返回列表元素最大值
#min(list) 返回列表元素最小值 list(seq) 将元组转换为列表
#list.count(obj)  统计某个元素在列表中出现的次数  list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
#list.index(obj) 从列表中找出某个值第一个匹配项的索引位置 list.insert(index, obj) 将对象插入列表
#list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
#list.remove(obj) 移除列表中某个值的第一个匹配项
#list.reverse() 反向列表中元素 list.sort(cmp=None, key=None, reverse=False) 对原列表进行排序


#4 元组
#Python的元组与列表类似，不同之处在于元组的元素不能修改。
#元组使用圆括号，列表使用方括号。
#元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
tup = ('physics', 'chemistry', 1997, 2000)
#访问元组 和访问列表一样
print(tup[:2])
#修改元组  元组中的元素值是不允许修改的，但可以对元组进行连接组合
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

tup3 = tup1 + tup2;
print(tup3)

#删除元组 元组中的元素值是不允许删除的，但可以使用del语句来删除整个元组
tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
del tup
print("After deleting tup : ")
print(tup)

#元组是一个序列，运算操作符和列表的一致 例如：


print(len((1,2,3))) #获取列表长度 3
print((1,2,3)+(4,5,6)) #组合 [1, 2, 3, 4, 5, 6]
print(('Hi！',)*4)  # 重复 ['Hi!', 'Hi!', 'Hi!', 'Hi!']
print(3 in (1,2,3)) # 元素是否存在于列表中 true
for x in (1,2,3):
    print(x)    #迭代 1，2，3
#元组索引，截取
#因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素,规则和列表一样

#无关闭分隔符
#任意无符号的对象，以逗号隔开，默认为元组，如下实例：
print('abc', -4.24e93, 18+6.6j, 'xyz')

#元组内置函数 同列表

#5、字典(Dictionary) 字典是另一种可变容器模型，且可存储任意类型对象
#字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 ,格式如下所示：
#d = {key1 : value1, key2 : value2 }
#键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。例如：
dict = {'a': 1, 'b': 2, 'b': '3'};
print(dict['b'])

#>>> 3

#访问字典里的值
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
print(dict['Name'])

#修改字典
#向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First','Class': 'sec'};
dict['Age'] = 8;  # 更新
dict['School'] = "School";  # 添加

print(dict['Class'])
# sec

#删除字典元素
#能删单一的元素也能清空字典，
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
del dict['Name'];  # 删除键是'Name'的条目
dict.clear();  # 清空词典所有条目
del dict;  # 删除词典

#6条件语句
#if条件判断
num = 5
if num == 3:            # 判断num的值
    print ('boss')
elif num == 2:
    print ('user')
elif num == 1:
    print ('worker')
elif num < 0:           # 值小于零时输出
    print ('error')
else:
    print ('roadman')    # 条件均不成立时输出
#while循环
num =0
while num<5:
    print(num)
    num +=1

#for循环
for x in range(101):
    sum = sum + x
print(sum)

#break语句可以提前退出循环 continue语句跳过当前的这次循环

#7、函数
# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念
# 面向对象的设计思想是抽象出Class，根据Class创建Instance
# 面向对象最重要的概念就是类（Class）和实例（Instance），类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

# 函数定义
# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
# 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
# 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
# 函数内容以冒号起始，并且缩进。
# return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

#格式
#def 函数名（参数列表）:
#    函数体
#例如：
# 计算面积函数
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)

print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))


#Welcome Runoob
#width = 4  height = 5  area = 20

#7、可更改(mutable)与不可更改(immutable)对象
#在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
#不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
#可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

#python 函数的参数传递：
#不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
#可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

#注意 python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

#关键字参数
#关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
#使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

def printme(str):
    "打印任何传入的字符串"
    print(str)
    return

# 调用printme函数
printme(str="python")

#  python

def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="python")

#名字:  python
#年龄:  50


#默认参数
#调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="python")
print("------------------------")
printinfo(name="python")

#名字:  python
#年龄:  50
#------------------------
#名字:  python
#年龄:  35

#不定长参数
#你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。
#加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)

#输出:
#70
#(60, 50)

#如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

#输出:
#10
#输出:
#70
#60
#50

#加了两个星号 ** 的参数会以字典的形式导入。
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)

# 调用printinfo 函数
printinfo(1, a=2, b=3)

#输出:
#1
#{'a': 2, 'b': 3}

#声明函数时，参数中星号 * 可以单独出现

def f(a,b,*,c):
    return a+b+c
#如果单独出现星号 * 后的参数必须用关键字传入。

#>>> def f(a,b,*,c):
#...     return a+b+c
#...
#>>> f(1,2,3)   # 报错
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: f() takes 2 positional arguments but 3 were given
#>>> f(1,2,c=3) # 正常
#6


#匿名函数
#python 使用 lambda 来创建匿名函数。
#所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
#lambda 只是一个表达式，函数体比 def 简单很多。
#lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
#lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
#虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
#相加后的值为 :  30

# 8 类
# 在Python中，类定义是通过class关键字定义的，语法格式：
#class ClassName:
 #   <statement-1>
 #   <statement-N>

#类实例化后，可以使用其属性，实际上，创建一个类之后，可以通过类名访问其属性。
#类对象支持两种操作：属性引用和实例化。
#属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。
#类对象创建后，类命名空间中所有的命名都是有效属性名。所以如果类定义是这样:
class  Student:
    name = 'python'
    score = 123

    def f(self):
        return 'hello world'


#实例化类：
x = Student()

#以上创建了一个新的类实例并将该对象赋给局部变量 x，x 为空的对象。
#很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为 __init__() 的特殊方法（构造方法），像下面这样：

class Student():

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
            print('%s: %s' % (self.name, self.score))

# __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：

# 要定义一个方法，除了第一个参数是self外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入：
bart = Student('Bart Simpson', 59)
print(bart.name)
print(bart.score)
bart.print_score()

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问，确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护：

class Students():
    __author__ = 'Michael Liao'
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


bart = Students('Bart Simpson', 59)
bart.set_name('john')
print(bart.get_name())
print(bart.get_score())
print('\n')

# 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名


# 当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# 继承有什么好处？最大的好处是子类获得了父类的全部功能。由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法

dog = Dog()
dog.run()

cat = Cat()
cat.run()
print('\n')

# 当然也可以对子类增加一些方法

class Dog(Animal):
    def eat(self):
        print('Eating meat...')
dog = Dog()
dog.run()
dog.eat()
print('\n')

# 继承的另一个好处：多态
# 多态：任何依赖父类作为参数的函数或者方法都可以不加修改地正常运行  由运行时该对象的确切类型决定
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
# dog.run()

cat = Cat()
cat.run()
print('\n')



# 获取对象信息 使用type()判断对象类型 返回对应的Class类型
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))


# type()返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
print(type(123)==type(456))
print(isinstance(type(123), int))
print(type(123)==int)

print(type('abc')==type('123'))
print('\n')

# 判断基本数据类型可以直接写int，str等，判断一个对象是否是函数可以使用types模块中定义的常量：

import types
def fn():
    pass
    print(type(fn)==types.FunctionType)

    print(type(abs)==types.BuiltinFunctionType)

    print(type(lambda x: x)==types.LambdaType)

    print(type((x for x in range(10)))==types.GeneratorType)

fn()


class Husky(Dog):
    pass

# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
h = Husky()
# 判断一个变量是否是某个类型可以用isinstance()判断：
print(isinstance(b, Animal))
print(isinstance(c, Dog))

print(isinstance(c, Animal)) # 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行：
print(isinstance(b, Dog))
print(isinstance(h, Animal))
# 能用type()判断的基本类型也可以用isinstance()判断：
print(isinstance(a, list))
# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))
print('\n')

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))

# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：如果试图获取不存在的属性，会抛出AttributeError的错误：
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x'))
print(obj.x)
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(obj.y)
# 可以传入一个default参数，如果属性不存在，就返回默认值：
print(getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404
# 获取对象方法
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))

# 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用
# 实例变量：定义在方法中的变量，只作用于当前实例的类。
# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。


# 多重继承：一个子类就可以同时获得多个父类的所有功能
#现在我们要实现一个Animal类层次的设计，假设我们要有以下4种动物
#Dog - 狗狗；
#Bat - 蝙蝠；
#Parrot - 鹦鹉；
#Ostrich - 鸵鸟。
#如果按照哺乳动物和鸟类归类，我们可以设计出这样的类的层次：
                     --Dog
         -- Mammal --
                     --Bat
Animal --
                   --Parrot
         -- Bird --
                   --Ostrich


#但是如果按照“能跑”和“能飞”来归类，我们就应该设计出这样的类的层次：
                       --Dog
         -- Runnable --
                       --Ostrich
Animal --
                     --Parrot
         -- Flyble --
                     --Bat

#如果要把上面的两种分类都包含进来，我们就得设计更多的层次：
#类的层次就复杂了 正确的做法是采用多重继承。
class Animal(object):
    pass

# 大类:哺乳类和鸟类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

# 加上Runnable和Flyable的功能，定义好Runnable和Flyable的类：
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

# 在设计类的继承关系时，通常，主线都是单一继承下来的，如果需要“混入”额外的功能，通过多重继承就可以实现，这种设计通常称之为MixIn。
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系


# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：

class Dog(Mammal, Runnable):
    pass
# 对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat：

class Bat(Mammal, Flyable):
    pass

# __slots__
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age')
s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
s.score = 99  # 绑定属性'score'

#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'Student' object has no attribute 'score'

#由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score = 9999
print('\n')
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__


# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.set_score(60) # ok!
print(s.get_score())
# s.set_score(9999)

# @property
# Python内置的@property装饰器就是负责把一个方法变成属性调用的
# 把一个getter方法变成属性，只需要加上@property就可以了，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

# 定制类
#看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
# __str__()方法，返回一个字符串
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

print(Student('Michael'))
#这样打印出来的实例，不但好看，而且容易看出实例内部重要的数据。
#但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看
# s = Student('Michael')
# s
#<__main__.Student object at 0x109afb310>
#这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

#解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__


# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

#我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值


for n in Fib():
    print n


# 枚举
# 枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
# @unique装饰器可以帮助我们检查保证没有重复值。

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

# 元类
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
#比方说我们要定义一个Hello的class
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

#当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象
#>>> h = Hello()
#>>> h.hello()
#Hello, world.
#>>> print(type(Hello))
#<type 'type'>
#>>> print(type(h))
#<class 'hello.Hello'>

#type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
#所以我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

#type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：



# 要创建一个class对象，type()函数依次传入3个参数：
#
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
#例如：
Hello = type('Hello', (object,), dict(hello=fn))

#通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
#正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。

# metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass（元类）。
#当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
#但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
#连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
#所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

#先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法
# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    __metaclass__ = ListMetaclass # 指示使用ListMetaclass来定制类

#__metaclass__ = ListMetaclass语句指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
# 在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

#__new__()方法接收到的参数依次是：
#当前准备创建的类的对象；
#类的名字；
#类继承的父类集合；
#类的方法集合

#现在我们可以测试一下

#  L = MyList()
#  L.add(1)
#  L
# [1]

#而普通的list没有add()方法：

# l = list()
# l.add(1)
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'add'

#动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下，确实应该直接写。
#通过metaclass修改类定义的。ORM就是一个典型的例子。
#ORM全称“Object Relational Mapping”，即对象-关系映射，
#就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

#要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

#让我们来尝试编写一个ORM框架。
#编写底层模块的第一步，就是先把调用接口写出来。
#比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User，如下这样的代码：

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()

#其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，
#save()全部由metaclass自动完成。虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。

#首先来定义Field类，它负责保存数据库表的字段名和字段类型：

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

#在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


#下一步，就是编写最复杂的ModelMetaclass了：
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name # 假设表名和类名一致
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        return type.__new__(cls, name, bases, attrs)

#以及基类Model：

class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

    def delete(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'delete into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


# 当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找__metaclass__，
# 如果没有找到，就继续在父类Model中查找__metaclass__，找到了，就使用Model中定义的__metaclass__的ModelMetaclass来创建User类，
# 也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。

#在ModelMetaclass中，一共做了几件事情：
#排除掉对Model类的修改；
#在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，否则，容易造成运行时错误；
#把表名保存到__table__中，这里简化为表名默认为类名。

#我们实现了save()方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。


u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()

#输出如下
# Found model: User
# Found mapping: email ==> <StringField:email>
# Found mapping: password ==> <StringField:password>
# Found mapping: id ==> <IntegerField:uid>
# Found mapping: name ==> <StringField:username>
# SQL: insert into User (password,email,username,uid) values (?,?,?,?)
# ARGS: ['my-pwd', 'test@orm.org', 'Michael', 12345]

#9 错误、调试和测试
#程序一旦出错，还要一级一级上报，直到某个函数可以处理该错误（比如，给用户输出一个错误信息）。
#所以高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。

try:
    print ('try...')
    r = 10 / 0
    print ('result:', r)
except ZeroDivisionError as e:
    print ('except:', e)
finally:
    print ('finally...')
print ('END')


#执行结果：
# try...
# except: integer division or modulo by zero
# finally...
# END

#没有错误发生，except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）。
#错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理。没错，可以有多个except来捕获不同类型的错误：
#如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：

try:
    print ('try...')
    r = 10 / int('a')
    print ('result:', r)
except ValueError as e:
    print ('ValueError:', e)
except ZeroDivisionError as e:
    print ('ZeroDivisionError:', e)
else:
    print ('no error!')
finally:
    print ('finally...')
print ('END')


#Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类
#常见的错误类型和继承关系 https://docs.python.org/2/library/exceptions.html#exception-hierarchy
#使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
#也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写try...except...finally的麻烦。