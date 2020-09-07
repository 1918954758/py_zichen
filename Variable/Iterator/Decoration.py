# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: Decoration
# @Discription: 装饰器
# @Author: 子辰
# @Date: 2020-09-07 20:29
# @Software: PyCharm

###############################################
# 装饰器
###############################################

"""
装饰器：
    是一种增加函数或类功能的简单方法，它可以快速地给不同的函数或类传入相同的同能。
    调用装饰器函数，与之前调用的过程没有区别
"""

''' 定义一个简单的装饰器 (其实也是一个标准的闭包函数)'''
def decorate(func):
    def wrapper(*args, **kwargs):
        print('>>>>>>>execute start<<<<<<<')
        func(*args, **kwargs)
        print('>>>>>>>execute end<<<<<<<')
    return wrapper

''' 只用装饰器，给使用的函数都加上'execute start'和'execute end' '''

@decorate
def func1():
    print('i am a func1')

@decorate
def func2():
    print('i am a func2')

''' 调用 func1 和 func2 '''
func1()
print('\n')
func2()

# 注意，装饰器的内部外部函数的名字都是可以自定义的



















