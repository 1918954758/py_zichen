# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: GroupMatch
# @Discription: 组的匹配
# @Author: 子辰
# @Date: 2020-09-06 18:29
# @Software: PyCharm
#################################################
# 组的匹配
#################################################
import re

# 说明什么是组
# 组是一组字符的集合
match_str = 'lemonlemonlemonappleapplepearpear'
list1 = re.findall('(lemon){3}', match_str)
print(list1)                # output------->['lemon']   re.findall()函数比较特殊，他会对匹配的组中的元素进行去重，在返回
# 要想不去重，我么可以使用 re.search()函数
obj = re.search('(lemon){3}', match_str)
print(obj)                  # output-------><re.Match object; span=(0, 15), match='lemonlemonlemon'>
print(type(obj))            # output-------><class 're.Match'>
# 如果查看匹配到的字符串，我们在调用serach()函数的group()函数即可
print(obj.group())          # output------->lemonlemonlemon
print(type(obj.group()))    # output-------><class 'str'>

'''
组与字符集的区别
组(lemon)            匹配lemon这一组字符
字符集[lemon]         匹配括号中的任意一个字符
'''
print('-------------组与字符集的区别--------------')
list2 = re.findall('(lemon){3}', match_str)
print(list2)                # output------->['lemon']
list3 = re.findall('[lemon]{3}', match_str)
print(list3)                # output------->['lem', 'onl', 'emo', 'nle', 'mon']

"""
Group组的匹配
"""
print('--------------group()分组函数--------------')
match_str1 = 'life is mostly happy,but sometimes sad'
'''
需求：
    1. 将is mostly happy,but sometimes匹配出来
    2. 将is mostly happy 以及sometimes分别匹配出来
'''
# 需求 1
r = re.search('life(.*)sad', match_str1)
print(r.group(0))               # output------>life is mostly happy,but sometimes sad
print(r.group(1))               # output------>is mostly happy,but sometimes
# print(r.group(2))  该语句要想顺利执行需要将 sad 放到一个组里才可以，，不然python找不到该组

# 需求 2
r1 = re.search('life(.*)but(.*)sad', match_str1)
print(r1.group(1))              # output------>is mostly happy,
print(r1.group(2))              # output------>sometimes

# 如果想查看所有分组的情况，我们可以使用groups()函数
print(r1.groups())              # output------>(' is mostly happy,', ' sometimes ')
'''
补充一下group()函数：
    该函数默认情况是等价于传参数0的，也就是把所有的匹配结果都返回
    如果参数传递的是1，那么返回第一个分组情况
    如果参数传递的是2，那么返回第二个分组情况
'''