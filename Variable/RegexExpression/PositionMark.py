# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: PositionMark
# @Discription: 定位符 ^ 和 $
# @Author: 子辰
# @Date: 2020-09-06 18:14
# @Software: PyCharm
#################################################
# 定位符 ^ 和 $
#################################################
import re
match_str = 'abcdef 123456 abcdef 456 abc'
# 匹配字符串开始的位置
# ^[a-z]{6} 表示，必须要以小写字母开头，匹配6位，知道遇到非单词字符就结束匹配
''' ^ '''
list1 = re.findall('^[a-z]{6}', match_str)
print(list1)                # output------->['abcdef']

# 匹配字符串结束的位置
''' $ '''
list2 = re.findall('[a-z]{3}$', match_str)
print(list2)                # output------->['abc']

'''
注意： ^
[^abc]  表示匹配除了abc字符意外的字符
^[abc]  表示匹配以abc字符开头的字符串
'''