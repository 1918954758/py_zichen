# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: Generator
# @Discription: 生成器
# @Author: 子辰
# @Date: 2020-09-07 00:50
# @Software: PyCharm

###############################################
# 生成器
###############################################

"""
如果一个列表中，存有海量数据，如果仅仅想访问其中的某几个元素，那么这样的操作会特别耗内存
生成器的特点：
    1. 操作海量数据，节约大量内存空间
生成器的创建：
    函数中如果包含yield关键字，那么这个函数就不再是一个普通函数，而是一个生成器（generator)对象。
    在python中，使用了yield的函数被称为生成器（generator）
    生成器的运行特点：
        2. 跟普通函数不同的时，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
        3. 在调用生成器运行的过程中，每次遇到yield时，函数会暂停并保存当前所有的运行信息，返回yield的值，并在下一次执行next()方法时，从当前位置继续执行
"""
# 创建一个生成器，传入最大最小值，执行next()方法

def mygene(min, max):
    while min < max:
        yield min
        min += 1

my_gene = mygene(1, 5)
print(next(my_gene))            # outpu----->1
print(next(my_gene))            # outpu----->2
print(next(my_gene))            # outpu----->3


'''
yield 与 return 区别：
    return后，会跳出当前函数。yield 不会跳出当前函数。
    yield保存当前函数的执行状态，在返回后，函数又回到之前保存的状态继续执行。
'''

def test():
    return 1
    return 2

def genetest():
    yield 1
    yield 2

print("====================<<<<<<【return】>>>>>>=====================")
print(test())
print(test())
print("====================<<<<<<【yield】>>>>>>=====================")
print(next(genetest()))
print(next(genetest()))