# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: Amount
# @Discription: 数量词匹配{}
# @Author: 子辰
# @Date: 2020-09-06 17:31
# @Software: PyCharm

#################################################
# 数量词匹配{}
#################################################
import re
"""
需求：
    向去除完整的数字集合 如：0、12、344、55等
"""
match_str1 = '&a0b12c344d55&AC_'
list1 = re.findall('\d', match_str1)
print(list1)                # output------>['0', '1', '2', '3', '4', '4', '5', '5']
list2 = re.findall('\d{1,3}', match_str1)
print(list2)                # output------>['0', '12', '344', '55']
"""
需求：
    想取出完整的单词集合 如： lemon、banana、pear
"""
match_str2 = 'lemon12banana34pear56'
list3 = re.findall('[a-z]{4,6}', match_str2)
print(list3)                # output----->['lemon', 'banana', 'pear']

# 贪婪匹配：倾向于最大长度的匹配
# 非贪婪匹配：倾向于最小长度的匹配
