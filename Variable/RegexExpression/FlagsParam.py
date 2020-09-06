# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: FlagsParam
# @Discription: Flag可选参数
# @Author: 子辰
# @Date: 2020-09-06 18:45
# @Software: PyCharm
#################################################
# Flags可选参数
#################################################
"""
对于函数findall(pattern, string, flags=0)
pattern         指的是：正则表达式匹配规则
string          指的是：要进行匹配的字符串
flags           指的是：可选参数，进行特定条件的匹配
"""
import re
# 如果我不想区分大小写，匹配lemon，那么就用到了flags可选参数了
match_str = 'lemon LEMON'
list1 = re.findall('lemon', match_str, re.I)
print(list1)                # output----------->['lemon', 'LEMON']

"""
补充： 元字符 .
表示：匹配除 \n之外的任何单字符
"""
match_str2 = '\n123 abc\r'
list2 = re.findall('.', match_str2)
print(list2)                # output----------->['1', '2', '3', ' ', 'a', 'b', 'c', '\r']
# 如果我们也想匹配 \n ，该怎么办呢？
list3 = re.findall('.', match_str2, re.S)
print(list3)                # output----------->['\n', '1', '2', '3', ' ', 'a', 'b', 'c', '\r']

# 如果我想不区分大小写，并且让 . 也去匹配 \n
match_str3 = 'lemon\n LEMON\n'
list4 = re.findall('lemon.', match_str3, re.I | re.S)
print(list4)                # output----------->['lemon\n', 'LEMON\n']
'''这里的re.I表示不区分大小写，re.S表示让.也匹配 \n'''
