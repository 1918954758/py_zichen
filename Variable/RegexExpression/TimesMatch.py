# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: TimesMatch
# @Discription: 次数匹配
# @Author: 子辰
# @Date: 2020-09-06 18:01
# @Software: PyCharm
#################################################
# 次数匹配
#################################################
"""
 *      匹配前面的字符零次或者多次  {0,}
 +      匹配前面的字符一次或者多次  {1,}
 ?      匹配前面的字符零次或者一次  {0,1}
"""
import re
match_str = 'lemo123 lemon345 lemonnnn567'
list1 = re.findall('lemon*', match_str)
print(list1)                    # output------>['lemo', 'lemon', 'lemonnnn']
list2 = re.findall('lemon+', match_str)
print(list2)                    # output------>['lemon', 'lemonnnn']
list3 = re.findall('lemon?', match_str)
print(list3)                    # output------>['lemo', 'lemon', 'lemon']