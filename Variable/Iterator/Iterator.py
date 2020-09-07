# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: Iterator
# @Discription: 迭代器
# @Author: 子辰
# @Date: 2020-09-07 00:30
# @Software: PyCharm

###############################
# 迭代器
###############################

"""
本章之前的代码，使用的for循环语句，本质上都是迭代器的应用
迭代器，可以理解为一个容器，循环的时候，每次从容器中取出一个数据，知道数据被取完为止
"""

'''
如何自定义一个迭代器：
以类为例：
    需要在类中，实现两个方法： __iter__ 和 __next__
    其中：
        1. __iter__ 方法需要返回对象本身，他是fou循环使用迭代器的要求；
        2. __next__ 方法用于返回容器中下一个元素，当容器中的数据取完时，需要引发StopIteration一场
'''
'''
需求：
    1. 自定义一个迭代器，通过传入最小值和最大值，返回该范围所有值的三次方
    2. 将返回的值，存入num_list列表中
'''


# noinspection PyRedundantParentheses,PyShadowingBuiltins
class Number():
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        # 需要返回这个范围内所有数字的三次方
        num = self.min
        if self.min <= self.max:
            self.min += 1
            return num ** 3
        else:
            raise StopIteration


# 将返回的值存到列表中
num_list = []
for i in Number(1, 5):
    num_list.append(i)
print(num_list)
