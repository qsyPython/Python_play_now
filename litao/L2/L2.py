
# Python的第2期作业：
# 写或仿写一个供大家可以import 的类库 要求：
# 1、至少有一个方法和__init__
# 2、完整易懂的使用方法或注释
# 3、实现的功能和场景不限（比如手机号码检查，但不能仅限于长度、开头、数字，要丰富更多其他内容，例如归属地等）
import re
from urllib.request import urlopen

from litao.L2.FileOperate import File_utils



phone_num = input()

f = File_utils()
f.__set__(phone_num)
f.select_phone()





