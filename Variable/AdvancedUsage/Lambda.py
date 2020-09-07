# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: Lambda
# @Discription: Lambda匿名函数
# @Author: 子辰
# @Date: 2020-09-07 20:46
# @Software: PyCharm

###############################################
# Lambda匿名函数
###############################################

""" 匿名函数就是没有定义函数的名称，但是也可以实现函数某些简单的功能 """
'''
需求：
    传入x, y
    返回 x + y
'''


# 之前的方式
def add(x, y):
    return x + y


'''
匿名函数创建：
    lambda param_list:expression
    lambda:             关键字
    param_list:         参数列表
    expression：        表达式 （建议书写一些简单的表达式，没法完整实现复杂代码块内容）
'''
# 使用匿名函数的方式

f = lambda x, y: x + y
print(f(3, 4))

'''
需求：
    传入两个函数x, y
    如果 x > y 返回 x + y
    如果 x < y 返回 x - y
'''
m = lambda x, y: x + y if x > y else x - y
print(m(5, 1))
