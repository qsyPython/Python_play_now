# -*- coding:UTF-8 -*-
# 面向对象
# 有意义的面向对象的代码
# 类 = 面向对象
# 类 、 对象

# 类定义 第一个字母大写  

# 类和对象  (实例化关联在一起的)
class  Student():
    name = ''   # 这个不是全局变量
    age = 0

    def print_file(self):# 类下面的函数必须加self  下面调用参数需要用self.语法
        print('name:'+ self.name)
        print('age:'+ str(self.age))
    # print_file() #这个外部不调用那么 不会执行  类只负责定义  不包括执行
# class StudentHomework():
#     homework_name ='
#

tudent = Student()
student.print_file()

