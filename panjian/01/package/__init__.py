'''
__init__.py 文件的作用是将文件夹变为一个Python模块,Python 中的每个模块的包中，都有__init__.py 文件。
在导入一个包时，实际上是导入了它的__init__.py文件。
可以在__init__.py文件中批量导入我们所需要的模块，而不再需要一个一个的导入
'''

import os
import sys
import re


# __all__ 它用来将模块全部导入
# from package import *
# __all__ = ['os', 'sys', 're']
# ? 测试没通过



# __version__ = "1.0.0"
