from enum import Enum,unique
@unique
# 装饰器可以帮助我们检查保证没有重复值。
# 可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
# 枚举成员不能进行大小比较

class MJlib(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7