# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: MatchAndSearch
# @Discription: match 和 search 以及 findall函数
# @Author: 子辰
# @Date: 2020-09-06 19:07
# @Software: PyCharm
#################################################
# match 和 search 以及 findall函数
#################################################
"""
re.findall(pattern, string, flags=0)    搜索整个字符串，        返回所有匹配结果
re.match(pattern, string, flags=0)      从字符串首字符开始匹配，     若首字符不匹配，则返回None，   若匹配则返回第一个匹配对象
re.search(pattern, string, flags=0)     搜索整个字符串，            若全部匹配，则返回None，      若匹配则返回第一个匹配对象（这个指的是至少有一个匹配，就返回第一个匹配道德对象）
"""
import re

match_str = 'abc5678 lemon 1234'
print(re.findall('\d', match_str))                      # output------>['5', '6', '7', '8', '1', '2', '3', '4']
print(re.match('\d', match_str))                        # output------>None
print(re.match('\d', '5678 lemon 1234').group())        # output------>5
print(re.search('\d', match_str).group())               # output------>5
print(re.search('\d', 'a#_g?.,d3a4f9').group())         # output------>3
