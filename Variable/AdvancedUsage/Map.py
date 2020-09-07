# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: Map
# @Discription: 高阶函数Map
# @Author: 子辰
# @Date: 2020-09-07 21:17
# @Software: PyCharm

###############################################
# 高阶函数Map
###############################################

"""
map函数格式：
map(func, *iterables)
func            可接受一个函数
*iterables      可接受一个或多个可迭代的序列
"""
'''
需求：
将一个列表里的每个元素开立方，结果生成一个新的列表
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def cube(param):
    return pow(param, 3)


obj = map(cube, a)
print(list(obj))
print('--------------------------------------')
# 将需求，使用lambda来实现
obje = map(lambda param: pow(param, 3), a)
'''
param=1 ----->1**3
param=2 ----->2**3
param=3 ----->3**3
...
param=9 ----->9**3
[1**3, 2**3, 3**3, 4**3, 5**3, 6**3, 7**3, 8**3, 9**3]
'''
print(list(obje))

'''
需求：
    现在有两个列表
    现需要将两个列表相对应的元素相加，组成新的列表
'''
print('--------------------------------------')
c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 3, 2, 5]
object1 = map(lambda param1, param2: param1 + param2, c, d)
'''
param1=1        param2=9        return 1+9
param1=2        param2=8        return 2+8
param1=3        param2=7        return 3+7
...
param1=9         param2=1        return 9+1
param1=None    结束
返回[1+9, 2+8, 3+7, 4+6, 5+5, 6+4, 7+3, 8+2, 9+1]
'''
print(list(object1))
# 注意，map()函数返回列表较少的结果集