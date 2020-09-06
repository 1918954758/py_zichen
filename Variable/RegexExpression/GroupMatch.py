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
