class MyClass:
    # 初始化，也可以传入参数
    def __init__(self,r,s):
        self.s = r
        self.r = s
        self.data = ["sssd",124,"fff"]
    def print_my_class(self):
        print("这是一个类",self.r,self.s)
        # self 代表实例 而非类
        print(self.__class__)
        for i in self.data:
            print(i)

x = MyClass("sdsd",56566)
x.print_my_class()