# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: TernaryExpression
# @Discription: 三元表达式
# @Author: 子辰
# @Date: 2020-09-07 21:02
# @Software: PyCharm

###############################################
# 三元表达式
###############################################

"""
三元表达式格式：

条件为真的结果    if    条件判断    else    条件为假的结果
Java或C语言三元表达式（三目运算符）格式：
条件判断 ? 条件为真的结果 : 条件为假的结果
"""

'''
需求：
    输入一个单词，
    如果是小写单词，则返回小写单词，否则返回大写单词
'''

f = lambda x: x if x.islower() else x.upper()
print(f('Hello'))