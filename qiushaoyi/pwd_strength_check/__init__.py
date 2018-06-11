# 包的使用注意事项：
'''

1、假如__init__.py为空，那么仅仅导入包是什么都做不了的，也不能访问包下面的模块；
只有当在__init__.py将模块逐一import，导入包后才能有效地使用包中的模块。
当然，没有在__init__.py中import模块的包，还是可以通过  from 包 import 模块  的方式导入模块

2、手动往自己创建的包里逐一导入模块时，使用：from 包名 import * (导入包名中的所有模块) / from 包名.某模块名 import *（导入包中某模块中所有内容）
但有个问题：并没有 完全导入该包的所有模块中的内容（函数或class等）。
结论：以*导入所有module时，package内的module是受__init__.py管理和限制的!!!

'''

from pwd_strength_check import file_tool
from pwd_strength_check import pwd_strength
from pwd_strength_check.file_tool import FileTool
from pwd_strength_check.pwd_strength import main

__all__ = ['pwd_strength','file_tool']