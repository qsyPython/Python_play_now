"""
Python的第2期作业：
写或仿写一个供大家可以import 的类库
要求：1、至少有一个方法和__init__
2、完整易懂的使用方法或注释
3、实现的功能和场景不限（比如手机号码检查，但不能仅限于长度、开头、数字，要丰富更多其他内容，例如归属地等）
"""
#实现一个记录登录信息功能
"""
1.记录用户的账号  登录时间  登录的使用的系统
"""

from saveLogInfoTool import *

if __name__ == '__main__':
    log_info = saveLogInfoTool()
    log_info.main()