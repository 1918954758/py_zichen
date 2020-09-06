# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: RegexExpression
# @Discription: 初识正则表达式
# @Author: 子辰
# @Date: 2020-09-06 15:19
# @Software: PyCharm

#################################################
# 初识正则表达式
#################################################

""" 正则表达式： 通过某种规则来匹配符合条件的字符序列 """
import re

'''
使用场景：
    快速查找、匹配或替换具有特殊格式的字符；
    如：
        1. 文本替换
        2. 匹配电子邮箱、电话号码、IP地址等
        3. 匹配爬虫程序中，某些特点格式的字符
'''
# 会将所有符合条件的字符，放在一个列表中
# re.findall(pattern, string, flags = 0)
'''
pattern         正则表达式匹配规则
string          要进行匹配的字符串
flags           可选参数，进行特定条件的匹配
'''
# 匹配下面字符串中所有的lemon(一个o的lemon,两个o的lemon等都需要匹配到)
match_str = 'lemon&apple&lemoon&lemooon&pear&lemoooon'
list1 = re.findall("lemon", match_str)  # 这里的 lemon 是一个普通的字符串，并不是一个正规的正则表达式
print(list1)
print('------------------------------------------------')
# 匹配所有lemon   lemoon    lemooon    lemoooon
list2 = re.findall('lemo{1,4}n', match_str)         # TODO 注意 对于python中的正则花括号{}，里面的连个参数之间不能有空格
print(list2)
