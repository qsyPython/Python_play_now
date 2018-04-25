# Python的第2期作业：
# 写或仿写一个供大家可以import 的类库
# 要求：
# 1、至少有一个方法和__init__
# 2、完整易懂的使用方法或注释
# 3、实现的功能和场景不限（比如手机号码检查，但不能仅限于长度、开头、数字，要丰富更多其他内容，例如归属地等）
# 本次实现的功能为 信息系统：对个人信息的增删改查 姓名 工号 年龄 工作 手机号 等

from SJTHomeWorkTwo_userSystemClass import *

if __name__ == '__main__':
    user_system = User_System()
    user_system.main()
