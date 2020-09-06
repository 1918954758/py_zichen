# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: PackageAndModule
# @Discription: 包和模块
# @Author: 子辰
# @Date: 2020-09-06 21:15
# @Software: PyCharm


"""
包： 比如说Base/Function/ProcessAndObject等
模块：包下面的文件
在一个模块中导入另一个模块的时候，必须用 import
import 后面一定跟的是模块名
eg: import Base
此外，也可以给导入的模块名设置一个别名
eg：import Base as b
如果要使用导入的模块中的方法或属性的时候，需要b.方法 或 b.属性
eg： b.func()   b.variable
"""
"""
如果要引用不同包中的模块：
需要写成：import 包名.模块名 （import 包名.模块名 as t）
"""

""" from import 的用发"""
'''
同包中，不同模块间的引用：
from 模块名 import 模块中的变量名
此时我们访问导入包的变量，就可以不用模块.变量名了，，直接用变量名就可以

不同包中，模块间的引用：
from 包名.模块名 import 模块中的变量名
此时我们就可以不同包中的变量了
为了方便，可以把import后面的模块中的变量名统统用一个星号代替   *  
'''
'''
如果不想让其他人导入变量，我们可以自定义那些变量可以被导入，那些变量不可以被导入：
__all__ = ['属性名']   这就表示，该属性可以被导入，本模块中的其他属性不可以被导入，，，，如果不写'__all__ = ['xxx']'就表示，该模块中的变量全部可以被导入
'''


######################################################
# __init__.py的特点：
#   1. 申明一个文件夹为一个包
#   2. import 包
#   3. 该模块名为一个包名     这条可以在'__init__.py'中利用'print('__name__')'来测试
#   4. 自定义选择那些模块可以导入
#
# import 模块名
# 如果 import后面跟的是一个包名，，那么他其实是导入的该包下的'__init__.py'这个模块，这样看，和import后面必须跟模块名不冲突
# 用from 包 import 模块这种形式，其实也是导入的该包下的 '__init__.py这个模块'
#
# 在'__init__.py'这个模块中可以定以同包下的那些模块是可以被导入的
#       使用'__all__ = ['模块名']'    表示该模块可以被导入
######################################################










