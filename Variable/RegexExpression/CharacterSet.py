# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: CharacterSet
# @Discription: 字符集
# @Author: 子辰
# @Date: 2020-09-06 16:15
# @Software: PyCharm

#################################################
# 字符集
# [xxx]  单字符匹配
#################################################
import re


match_str = 'bac | bbc | bcc | bdc | bec'
"""
需求： 匹配 bac 或 bbc
"""
list1 = re.findall('b[ab]c', match_str)
print(list1)
# 如果匹配除了 bac 或 bbc之外的 bxc
list2 = re.findall('b[^ab]c', match_str)
print(list2)
"""
需求： 匹配 bac 或 bbc 或 bcc 或 bdc 或 bec
"""
list3 = re.findall('b[a-e]c', match_str)
print(list3)
list4 = re.findall('b[\\w]c', match_str)   # \w 匹配一个单词字符   [A-Za-z0-9_]   \W  匹配一个非单词字符   [^A-Za-z0-9_]
print(list4)
