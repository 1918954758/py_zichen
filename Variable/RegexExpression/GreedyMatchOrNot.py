# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: GreedyMatch
# @Discription: 贪婪匹配与非贪婪匹配
# @Author: 子辰
# @Date: 2020-09-06 17:42
# @Software: PyCharm
#################################################
# 贪婪匹配与非贪婪匹配
#################################################

"""
数量词
贪婪： 倾向于取最大长度匹配
非贪婪：倾向于取最小长度匹配
"""
import re
'''
匹配描述：
由于正则匹配的是a-z，所以lemon可以进行匹配，然后他匹配到第四个字符的时候发现它可以匹配的最大长度是6个字符，那么又接着向下匹配了一个n字符
接着遇到12，不在匹配范围之内，就放弃匹配，然后匹配banana，同样道理匹配，以此类推，，由此可见，下面例子属于贪婪匹配，趋向于最大长度的匹配
'''
match_str = 'lemon12banana34pear56'
list1 = re.findall('[a-z]{4,6}', match_str)
print(list1)               # output----->['lemon', 'banana', 'pear']
'''
那么如何才能让他做到非贪婪匹配呢？
我们可以在数量词后面加上一个?，这个?表示让正则表达式做到最小长度的匹配，匹配长度为4个字符
'''
list2 = re.findall('[a-z]{4,6}?', match_str)
print(list2)               # output----->['lemo', 'bana', 'pear']


# 案例：
match_str2 = 'lemonnnnnnnn'
list3 = re.findall('lemon{1,}', match_str2)
print('贪婪匹配》》》》》》》：', list3)            # output--------->贪婪匹配》》》》》》》： ['lemonnnnnnnn']
list4 = re.findall('lemon{1,}?', match_str2)
print('非贪婪匹配》》》》》》：', list4)            # output--------->非贪婪匹配》》》》》》： ['lemon']

'''
贪婪模式在整个表达式成功的前提下，尽可能多的匹配
非贪婪模式在整个表达式成功的前提下，尽可能少的匹配
'''