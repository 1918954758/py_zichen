# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: Reduce
# @Discription: reduce()函数
# @Author: 子辰
# @Date: 2020-09-07 22:07
# @Software: PyCharm

"""
reduce python内置函数
reduce(function, sequence[], initial)
与map(function, sequence[])
"""
'''
需求：
    机选列表a个元素之间相乘之后的值
    a = [1, 2, 3, 4, 5]
    num = 1
    for i in a:
        num *= i
    print(num)  output ------> 120
'''
"""
reduce()函数书写格式:
    reduce(function, sequence[], initial)
    function：       接受一个函数
    sequence：       接受一个可迭代序列
    initial：        初始运算的值
    reduce()函数，要求至少要传入前两个参数，第三个初始运算值可以不传
"""
'''
需求：
    计算a 列表个元素相加之后的值
'''
from functools import reduce
a = [1, 2, 3, 4, 5]


num = reduce(lambda x, y: x * y, a)
'''
x=1         y=2
x=1*2       y=3
x=1*2*3     y=4
x=1*2*3*4   y=5
return 1*2*3*4*5=120
'''
print(num)          # output------->120

# 如果给了一个初始值，那么这个初始值就会作为第一个元素来进行乘算
numb = reduce(lambda x, y: x * y, a, 1000)
'''
x1000           y=1
x=1000*1        y=2
x=1000*1*2      y=3
...
x=1000*1*2*3*4  y=5
return 1000*1*2*3*4*5=120000

'''
print(numb)         # output------->120000

'''
例：
将列表中所有元素相加
'''

b = ['a', 'b', 'c']
r = reduce(lambda x, y: x + y, b)
'''
x=a         y=b
x=a+b       y=c
return a+b+c=abc
'''
print(r)

red = reduce(lambda x, y: x + y, b, '???')
'''
x=???       y=a
x=???+a     y=b
x=???+a+b   y=c
return ???+a+b+c=???abc
'''
print(red)






