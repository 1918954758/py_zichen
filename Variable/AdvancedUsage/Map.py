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
print(list(object1))
# 注意，map()函数返回列表较少的结果集