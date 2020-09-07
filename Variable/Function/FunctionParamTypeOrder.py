# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: FunctionParamTypeOrder
# @Discription: 函数参数类型顺序
# @Author: 子辰
# @Date: 2020-09-06 00:01
# @Software: PyCharm
'''
def fruits(*args, lemon):
    print(args)
    print(lemon)
fruits(4, 5, 6, 7)
'''
'''
Traceback (most recent call last):
  File "D:/py_zichen/Variable/Function/FunctionParamTypeOrder.py", line 12, in <module>
    fruits(4, 5, 6, 7)
TypeError: fruits() missing 1 required keyword-only argument: 'lemon'

Process finished with exit code 1
'''
""" 必须参数必须放到可变参数和默认值参数的前面 """

''' 默认值参数放到可变参数前面，打印出的结果和我们的预期不一样，所以，必须要将默认值参数放在可变参数的后面 '''
def fruits(apple=5, *args):
    print(apple)
    print(args)
fruits(1, 2, 3, 4, 5)
'''
output=====>>>>
1
(2, 3, 4, 5)

Process finished with exit code 0
'''
''' 可变关键子参数 '''
def func_name1(param1, *args, param = 0, **kwargs):
    pass
''' 可变关键字放在下面的位置，编译不通过，语法错误
def func_name2(**kwargs, param1, *args, param = 0):
    pass

def func_name3(param1, **kwargs, *args, param = 0):
    pass

def func_name4(param1, *args, **kwargs, param = 0):
    pass
'''
#################################
# 总结：
# 1. 必须参数
# 2. 可变参数
# 3. 默认值参数
# 4. 可变关键字参数
#################################