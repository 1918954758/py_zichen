# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: Filter
# @Discription: Filter()函数
# @Author: 子辰
# @Date: 2020-09-08 00:44
# @Software: PyCharm

"""
filter(function, iterable)
function:       接收一个函数
iterable：      接收一个可迭代的序列
过滤元素，返回需要的结果
"""
'''
需求：
    将列表a=[0, 1, 2, 3, 4, 5, 6]中非0的元素放到b=[]中去
'''
print('-----------------------传入lambda表达式-----------------------')
a = [0, 1, 2, 3, 4, 5, 6]
b = []
for i in a:
    if i != 0:
        b.append(i)
print(b)

# 用felter()函数实现上述需求
obj1 = filter(lambda x: x != 0, a)
'''
filter()中的函数，其实就是传递了一个过滤条件，然后再把剩下的元素放到b列表中，返回一个对象
'''
print(list(obj1))

print('-----------------------传入一个自定义函数-----------------------')
# 不适用lambda表达式，来实现上述需求
def fil(param):
    if param != 0:
        return param

obj2 = filter(fil, a)   # a序列中的元素会一个一个的传递个fil函数，其实内部对a序列做了循环遍历操作
print(list(obj2))
# filter()函数 返回结果必须是 True 或者 False
# bool(1)------->True
# bool(0)------->False
# 优化需求

print('-----------------------优化lambda表达式-----------------------')
obj3 = filter(lambda x: x, a)   # 0表示False   非0的正整数表示True
print(list(obj3))

print('-----------------------lambda表达式配合三元表达式使用-----------------------')
obj4 = filter(lambda x: x if x != 0 else False, a)
print(list(obj4))

print('-----------------------优化lambda表达式配合三元表达式使用-----------------------')

obj5 = filter(lambda x: True if x != 0 else False, a)
print(list(obj5))