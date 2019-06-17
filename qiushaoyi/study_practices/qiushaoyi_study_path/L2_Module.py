import sys
from PIL import Image
from enum import Enum, unique

# 模块: cd 文件夹路径 再ls ,读取文件！ 若是上级界面,路径:  ./
im = Image.open('test.png')
print(im.format, im.size, im.mode)

# 面向过程：函数化！！！
# 面向对象(Object Oriented Programming，简称OOP)：对象化(包含数据和函数)！！！高度封装
std1 = {'name': 'Machileg', 'score': 89}
std2 = {'name': 'mahfljg', 'score': 67}


def print_score(std):
    print('name:%s,score:%s' % (std['name'], std['score']))


print_score(std1)


class Student(object):
    """docstring for Student"""

    def __init__(self, name, score):
        super(Student, self).__init__()
        self.name = name
        self.score = score

    def print_score(self):
        print('name:%s,score:%s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


std666 = Student(std2['name'], std2['score'])
std666.print_score()
print(std666.get_grade())


# 开始了class: 实例的变量名如果以__开头，就变成了一个私有变量（private）,无法直接访问,可通过get和set方法
# 变量： 1、普通变量 self.name  2、私有变量 self.__name  3、特殊变量 self.__name__
class Human(object):
    """docstring for Human"""

    def __init__(self, name, sex, height):
        super(Human, self).__init__()
        self.__name = name
        self.__sex = sex
        self.height = height

    def print_hunman(self):
        print('%s:%s:%s' % (self.__name, self.__sex, self.height))

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height


human1 = Human('Borjglj', '男', 160)
human1.print_hunman()
print(human1.set_name('改名就是这么简单'), \
      human1.get_name(), human1.get_sex(), human1.get_height())

# 继承：多重继承。遗传性,python是多继承   多态:多样性
'''
多态的好处是：任何子类都可以调用基类方法，该基类的方法作为一个bridge，可以连接任何子类,
以基类为参数，在任何子类中创建某个func，就可以实现在该func中调用任何子类的方法
'''


class RunJump(object):
    print('能跑和跳的都来这里')


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal, RunJump):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Dog Eating meat...')

    def invokeAnimalSubclass(self, animal):
        animal.run()


class Cat(Animal, RunJump):
    def run(self, t):
        print('Cat is running...')

    def eat(self):
        print('Cat Eating meat...')

    def invokeAnimalSubclass(self, animal):
        animal.run()


dog = Dog()
cat = Cat()
dog.run()
dog.eat()

# 多态：不止是子类调用基类和 重写基类方法；可以实现在某一个子类中通过基类，调用任何其他子类的基类方法
dog.invokeAnimalSubclass(Cat())
cat.run()
cat.eat()
cat.invokeAnimalSubclass(Dog())
# 对象是否同类：type()只是本类，不到基类,isinstance(),issubclass()
if issubclass(Dog, Animal):
    print('Dog 是Animal的子类')
if isinstance(dog, Dog):
    print('dog 是Dog对象')
if isinstance(dog, Animal):
    print('dog 是Animal对象')
if type(dog) == Dog:
    print('type来判断dog 是Dog')
if type(dog) == Animal:
    print('type不能用来判断dog 是Animal对象')
if type(cat) == Cat:
    print('type来判断cat 是Cat对象,获取属性和变量', dir(cat))


class MyDog(object):
    # __slots__ = ('typeName','name','score','height') 限制该class实例能添加的属性: __slots__ = ('name','age')
    typeName = '我是变量'

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, str):
            raise ValueError('score must be an integer')
        self._score = value

    def __init__(self, height):
        super(MyDog, self).__init__()
        self.height = height
        self.a, self.b = 0, 1  # 初始化两个默认的计数器a，b

    def set_name(self, name):
        self.name = name

    def __len__(self):
        return 100

    def __str__(self):
        return 'MyDog object (name:%s)' % self.name

    def __str__(self):
        return 'MyDog object (typeName:%s name:%s height:%s score:%s)' \
               % (self.typeName, self.name, self.height, self.score)

    __repr__ = __str__

    # 获取某个list数据
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration
        return self.a

    # 截取对应的list数据
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    def __getattr__(self, attr):  # 某属性未被定义的补救方法
        if attr == 'qsy':
            return lambda: 25
        raise AttributeError('Dog object has no attribute %s' % attr)

    def __call__(self):
        print('通过对象自身调用，即可调用该方法：My name is %s', self.name)


myDog = MyDog(150)
myDog.typeName = '我就改你的type类型怎么了'
myDog.score = '100分'
myDog.set_name('我类个去')
print(myDog, hasattr(myDog, 'name'), setattr(myDog, 'name', '设置下新的name'), getattr(myDog, 'name'))
for n in myDog:
    print(n)
print(myDog[4])
print(myDog[0:5])
print(myDog.qsy())  # myDog.qsyNo()
myDog()
print('某对象是否可作为函数，被调用', callable(myDog), callable(dog))


# 要写SDK，给每个URL对应的API都写一个方法,完全动态的__getattr__，我们可以写出一个链式调用
class Chain(object):
    """docstring for Chain"""

    def __init__(self, path=''):
        super(Chain, self).__init__()
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


chain = Chain()
print(chain.status.user.timeline.list)

# 枚举
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique  # 装饰器可以帮我们检查保证有没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
day2 = Weekday.Sun
print(day1.value, day2)


# 一、定义类，然后创建实例
# 方式1：通过class
# Hello是一个class，它的类型就是type. 而h是一个实例，它的类型是class Hello
class Hello(object):
    def hello(self, name='world'):
        print('Hello,%s' % name)


h = Hello()
h.hello()


# 方式2：通过type创建class
def fn(self, name='world'):
    print('Hello 1,%s.' % name)


Hello1 = type('Hello', (object,), dict(hello=fn, sex=vars))
h3 = Hello1()
h3.hello()


# 二、定义metaclass，就可以创建类（类本身是metaclass的实例），最后创建实例
class ListMetaclass(type):  # metaclass的类名总是以Metaclass结尾
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(12)
L.add(150)
print(L)


# 总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子:\
# ORM框架全称“Object Relational Mapping”，即对象-关系映射，就是一个类对应一个表
class Field(object):
    """docstring for Field"""

    def __init__(self, name, column_type):
        super(Field, self).__init__()
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return ('<%s:%s>' % (self.__class__.__name__, self.name))


class StringField(Field):
    """docstring for StringField"""

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):  # 定义一个metaclass
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model:%s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping:%s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名映射为一致的
        print('test查看attrs:%s' % attrs)
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):  # 以metaclass创建一个名字为 Model 的对象
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    # 增删改查
    def add(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s(%s) values(%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL:%s' % sql)  # SQL:insert into User(id1,username1,email1,password1) values(?,?,?,?)
        print('ARGS:%s' % str(
            args))  # ARGS:[123456, 'Michael', '1129331905@qq.com', 'my-pwdTest'] 或 [78910, 'Jack', '1279487948@qq.com', 'you-pwdTest']

    def dele(self):
        pass

    def update(self):
        pass

    def find(self):
        pass


# testing code:	User对应一个表
class User(Model):
    id = IntegerField('id1')
    name = StringField('username1')
    email = StringField('email1')
    password = StringField('password1')


u1 = User(id=123456, name='Michael', email='1129331905@qq.com', password='my-pwdTest')
u2 = User(id=78910, name='Jack', email='1279487948@qq.com', password='you-pwdTest')
u1.add()
u2.add()
