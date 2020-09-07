# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: Closure
# @Discription: 闭包函数
# @Author: 子辰
# @Date: 2020-09-07 20:10
# @Software: PyCharm

###############################################
# 闭包
###############################################

"""
闭包函数的特点：
    1. 函数内部，在定义函数
    2. 内部函数需要引用外部变量，但非全局变量
    3. 需要把内部函数返回
"""

''' 简单的闭包函数 '''
def outer():
    a = 0

    def inner(b):
        nonlocal a
        a += b
    return inner

f = outer()

# 用下列方式测试，上面的函数是否为闭包函数，如果是闭包函数，则返回0，不是则报错
print(f.__closure__[0].cell_contents)

# 修改上述闭包函数变量a的值
# 可以使用 nonlocal关键字来修改

fn = outer()
fn(10)
print(fn.__closure__[0].cell_contents)     # 为什么打印的是 a 的值呢？？？
fn(30)
print(fn.__closure__[0].cell_contents)

'''
闭包函数使用场景：
    定制装饰器
    并行运算
    ...
'''