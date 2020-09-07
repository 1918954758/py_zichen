# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: ListComprehension
# @Discription: 列表推导式
# @Author: 子辰
# @Date: 2020-09-08 01:17
# @Software: PyCharm
#######################################################
# 列表推导式
# 格式：
# variable = [ i for i in input_list if 条件判断]
# variable      列表名，可以自定义
# i             循环变量
# input_list    可迭代序列
# if            条件判断，如果不写的话，默认所有条件都成立
#######################################################

"""
如何生成一个 0 - 9 的列表
"""
list1 = [i for i in range(0, 10)]  # 默认所有条件都成立
print(list1)

print('------------------利用函数生成--------------------')
list2 = []


def generater_num():
    for i in range(0, 10):
        list2.append(i)


generater_num()
print(list2)

print('------------------利用条件判断生成大于3的列表--------------------')
list3 = [i for i in range(0, 10) if i > 3]
print(list3)

"""
需求： 生成一个列表，列表的元素为a 列表中每个元素的三次方
"""
a = [1, 2, 3, 4, 5]
'''之前用map()'''
print('------------------利用map()函数生成--------------------')
obj1 = map(lambda x: x ** 3, a)
print(list(obj1))
print('------------------利用列表推导式生成--------------------')
list4 = [i ** 3 for i in a if True]
print(list4)

'''
需求： 将字典中的键，保存到另一个列表c中
'''
d = {'lemon': 5, 'apple': 3, 'pear': 4}
print('------------------利用列表推导式保存字典中的键--------------------')
c = [i for i in d.keys()]
print(c)
print('------------------利用列表推导式保存字典中的值--------------------')
e = [i for i in d.values()]
print(e)

'''
需求： 将字典中的键与值，进行替换
'''
print('------------------字典推导式--------------------')
f = {value:key for key, value in d.items()}
print(f)