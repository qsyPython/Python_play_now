import types


# class继承写法
class father_class(object):
    namee = 123
    def father_first_name(self):
        print('父亲性李')

class son_class_1(father_class):
    def father_first_name(self):
        print('儿子也姓李')

son = son_class_1()
son.father_first_name()

# 判断 数据类型 type
type('123') == type(123)
# false
type('123') == type('344')
#true
type('123') == str


# 判断变量是否是函数  除此之外还可以判断lambda 表达式之类的
def test_method():
    pass
print(type(test_method) == types.FunctionType)
# true
print(type(son) == type(son_class_1))
# false
#判断对象是否是某种类型  isinstance
print(isinstance(son,son_class_1))
# true

# 使用Dir  没发现啥乱用

# print(dir(son))


# 判断某个对象里是否有某个属性
father = father_class()
if hasattr(father,'namee'):
    print('有namee属性')
    getattr(father,'namee') #获取nemee属性

setattr(father,'add',123)  #添加add属性赋值123
if hasattr(father,'add'):
    print('有ADD的属性')
else:
    print('没有add属性')

# 动态给类添加属性和方法
class Person(object):
    def __init__(self,add_meth5):
        self.__add_meth5 = add_meth5


    def __set__(self, value):
        self.__add_meth5 = value
    def __get__(self):
        return self.__add_meth5

# p = Person()
# p.add_meth5 = 'Person新添加的属性值'
# print(p.add_meth5)

# def add_meth(self,age):
#     print(age)
# p.add_meth = types.MethodType(add_meth, p)
# p.add_meth('qwe')
#
# # 以上动态添加的之争对于同一个对象 新的对象不会存在 想要所有的实例对象都可以 获取添加的对象必须给class绑定方法
#
# def add_meth2(self):
#     print('添加的第二个方法')
#
# Person.add_meth2 = add_meth2
# p2 = Person()
# p2.add_meth2()
