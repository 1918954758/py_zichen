# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: RegexSubstitute
# @Discription: 正则替换
# @Author: 子辰
# @Date: 2020-09-06 20:03
# @Software: PyCharm
#################################################
# 正则替换
#################################################
"""
正则替换使用的是   re.sub()函数
re.sub(pattern, repl, string, count=0, flags=0)
pattern             正则表达式
repl                要替换的内容，也可传入函数
string              被替换的字符串
count               替换次数，默认是0，代表全部替换
                    1  代表替换一个
                    2  代表替换两个
                    ...
"""
import re

match_str = 'lemon apple 123456789 lemon  lemon'
'''
需求1：
将lemon全部替换成a
'''
ret1 = re.sub('lemon', 'a', match_str, count=0)
print(ret1)  # output------>a apple 123456789 a  a
'''
需求2：
将数字小于7的都转为0，将数字大于等于7的都转位10
'''
print('--------------------传入函数的情况-------------------------')
def transform(value):
    match_num = value.group()
    # print(match_num)
    if int(match_num) < 7:
        return '0'
    return '10'
    # print(type(match_num))
print('原字符串：' + match_str)
ret2 = re.sub('\d', transform, match_str, count=0)
print('结果是：' + ret2)
