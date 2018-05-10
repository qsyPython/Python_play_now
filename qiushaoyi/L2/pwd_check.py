'''
	作者：邱少一
	日期：2018/4/3
	功能：密码强度的读取以及保存
	第二期作业：
        写或仿写一个供大家可以import 的类库
        要求：1、至少有一个方法和__init__
             2、完整易懂的使用方法或注释
             3、实现的功能和场景不限（比如手机号码检查，但不能仅限于长度、开头、数字，要丰富更多其他内容，例如归属地等）
'''

import pwd_strength_check
# print(dir(pwd_strength_check))

#检查输入的密码强度
if __name__ == '__main__':
    pwd_strength_check.main()
