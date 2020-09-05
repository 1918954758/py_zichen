# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: Iterator
# @Discription: Python中的4种常用的迭代函数
# @Author: 子辰
# @Date: 2020-09-05 17:52
# @Software: PyCharm

"""
Python中的4种迭代函数，有：
enumerate(seq)          编号迭代
sorted(seq)             排序迭代
reversed(seq)           反转迭代
zip(seq)                并行迭代
seq  是可以遍历/迭代的对象，如列表，字符串，元组等
"""
# enumerate()       编号迭代
"""
编号迭代，在迭代的时候即返回序列中的编号(默认从0开始)，又返回序列中的元素
需要两个循环变量，分别接受编号和元素的值
"""
a = 'abcd'
for index, value in enumerate(a):
    print(index, value)
print('\n')
list1 = ['a', 'b', 'c']
dict1 = {'lemon':'a', 'apple':'b'}
tuple1 = ('a', 'b', 'c', 'd')
set1 = {'a', 'b', 'c', 'd', 'e', 'f'}
print('编号迭代，迭代list,dict,tuple,set>>>>>>>>>开始')
print("编号迭代，迭代list：")
for i in enumerate(list1):
    print(i, end=' ')
print('\n')
print("编号迭代，迭代字典：")
for i in enumerate(dict1):
    print(i, end=' ')
print('\n')
print("编号迭代，迭代元组：")
for i in enumerate(tuple1):
    print(i, end=' ')
print('\n')
print("编号迭代，迭代set集合：")
for i in enumerate(set1):
    print(i, end=' ')
print('\n')
print('编号迭代，迭代list,dict,tuple,set>>>>>>>>>结束')
# sorted()          排序迭代
"""
for循环变量的时候，默认先遍历序列中较小的值，后遍历序列中较大的值
可迭代对象中的元素，需要是可排序的同类数据
"""
b = [1, 2, 7, 2, 3, 4, 5]
for x in sorted(b):
    print(x)
for x in sorted(b, reverse=True):
    print(x)
# reversed()        反转迭代
"""将可以迭代的对象中的元素，从尾到头，进行遍历"""
print("a字符串:", a)
for x in reversed(a):
    print(x, end=' ')
print("\n")
# zip()             并行迭代
"""
zip() 同时遍历可迭代对象中同一序号的元素
如果元素长度不一致，只遍历到最短的序列长度
"""
x = [1, 2]
y = [3, 4]
z = [5, 6, 7]
for i in zip(x, y, z):
    print(i, end=' ')
'''output====>>>(1, 3, 5) (2, 4, 6) '''
print('\n')
x1 = [1, 2, 3, 4]
y1 = [5, 6]
z1 = [7, 8, 9]
for i in zip(x1, y1,z1):
    print(i, end=' ')
'''output====>>>(1, 5, 7) (2, 6, 8) '''
# 如下遍历就失去了zip的意义了
# string = 'abc'
# for i in zip(string):
#     print("字符串abc使用zip并行迭代： ", i, end=" ")
# print("\n")
# li = ['a', 'b', 'c']
# for i in zip(li):
#     print("list集合['a', 'b', 'c']使用zip并行迭代： ", i, end=' ')
# print("\n")
# lis = ['a', ['a1', 'b1', 'c1'], {1, 3, 5, 6}]
# for i in zip(lis):
#     print("list集合['a', ['a1', 'b1', 'c1'], {1, 3, 5, 6}]使用zip并行迭代", i, end=" ")
