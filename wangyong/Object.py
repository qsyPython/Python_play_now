# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念
# 面向对象的设计思想是抽象出Class，根据Class创建Instance
# 面向对象最重要的概念就是类（Class）和实例（Instance），类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。


# 在Python中，定义类是通过class关键字：

class Student(object):
    pass

# 创建实例是通过类名+()实现的：
# 可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

class Student(object):

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

class Students(object):
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


# 多重继承 ： 一个子类就可以同时获得多个父类的所有功能
# 在设计类的继承关系时，通常，主线都是单一继承下来的，如果需要“混入”额外的功能，通过多重继承就可以实现，这种设计通常称之为MixIn。
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系
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
#s.score = 99  # 绑定属性'score'

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
# __str__()方法，返回一个字符串
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
print(Student('Michael'))


# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。


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
# 要创建一个class对象，type()函数依次传入3个参数：
#
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
Hello = type('Hello', (object,), dict(hello=fn))



# metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# __new__()方法接收到的参数依次是：
#
# 当前准备创建的类的对象；
#
# 类的名字；
#
# 类继承的父类集合；
#
# 类的方法集合。
class MyList(list, metaclass=ListMetaclass):
    pass
