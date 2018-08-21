
# type()：
# 作用：1、获取某个对象和类的类；2、创建新的类：相当于oc中的 class
#要创建一个class对象，type()函数依次传入3个参数：
#class的名称；
#bases: 注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#dict: class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
print(type('33'))

def fn(self,name='World'):
    print('Hello , %s'%name)

# hello = type('Hello',(object,),dict(hello=fn,))
# h = hello()
# h.hello()
# print(type(hello),type(h))


# 🐂🐂🐂🐂🐂🐂🐂🐂hello相当于class，且class的类型都是type，包括下面的Hello🐂🐂🐂🐂🐂🐂🐂🐂🐂
# 结论：type就是元类


# class Hello(object):
#     def hello(self,name='World'):
#         print('Hello, %s'%name)
#
# h = Hello()
# h.hello()
# print(type(Hello),type(h))



#metaclass元类

# metaclass作用：允许你创建类 或者 修改类！！！
# 元类Listmetaclss
class Listmetaclss(type):
    def __new__(cls, name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

 # 元类创建class Text
class Text(metaclass=Listmetaclss):
    def append(self,value):
        list = []
        list.append(value)
        return list
# l = Text()
# t = l.add(4)
# print(l,t)

# 元类创建class MyList
class MyList(list,metaclass=Listmetaclss):
    pass

l = MyList()
l.add(2)
l.add(3)
print(l)

# 为什么ORM要用metaclass? 表的结构不定 --> 类属性和方法不定-->动态的修改类 首选metaclass！！！

# ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，
# 也就是1个类 对应 1个表，这样，写代码更简单，不用直接操作SQL语句。
# 要编写一个ORM框架： 所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。



# ORM精简版：

class Field(object):
    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s : %s>'%(self.__class__.__name__,self.name)

class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')


class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')



# 设计ORM的思路：
# 1、定义所有ORM映射的 基类Model
# 2、Model继承自dict、又实现了特殊方法__getattr__()和__setattr__()；
#    就可以使用了 user['name']、user.name
# 3、Model的元类ModelMetaclass: metaclass可以隐式地继承到子类
#    可通过该元类实现 class的类属性和值的读取 并 对其建立映射关系
#    attrs['__mappings__'] = mappings # 保存属性和列的映射关系
#    attrs['__table__'] = name
# 4、Model的元类ModelMetaclass中，又把属性和sql语句也进行了绑定,
#   定义各种操作数据库的方法，比如save()，delete()，find()，update等等。
#
# 5、从而通过model的方式实现的数据库





# 元类实现了类属性和value的映射
# 参数：
# cls 当前类 orm.ModelMetaclass
# name：类及其子类名字
# bases：cls的继承的类orm.Model
# attrs: 该类的所有属性和方法
class ModelMetaclass(type):
    def __new__(cls, name,bases,attrs):
        if name == 'Model': #排除掉对Model类的修改；
            return type.__new__(cls,name,bases,attrs)

        print('Found Model: %s' % name)
        mappings = dict()
        for k,v in attrs.items(): # 查找定义的类的所有属性,并绑定到mappings
            if isinstance(v,Field):
                print('Found mapping: %s ==> %s' % (k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)#从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致  把表名保存到__table__中
        return type.__new__(cls,name,bases,attrs)

# 基类Model
class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r'\'Model\' object has no attrs :%s'%key)
    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        field =[]
        params =[]
        args = []
        for k,v in self.__mappings__.items():
            field.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql = 'insert into %s(%s) values (%s)' % (self.__table__,','.join(field),','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
    age = IntegerField('age')


u = User(id = 12345,name ='john',email='1129331905@qq.com',password = '112933',height=23)
# u.age = 23
u.save()







