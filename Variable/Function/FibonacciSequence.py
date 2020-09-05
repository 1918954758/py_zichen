# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: FibonacciSequence
# @Discription: 案例：Fibonacci sequence 斐波那契数列
# @Author: 子辰
# @Date: 2020-09-06 01:23
# @Software: PyCharm

# 斐波那契数列又称黄金分割数列
# 因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，故而又称”兔子案例“
# 1， 2， 3， 5， 8， 13， 21， 34， ...
"""
这个数列从第3项开始，每一项都等于前两项之和。
在数学上，斐波那契数列以如下被以地推的方法定义：
F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2) (n > 3, n数据正整数)
"""

# def fibonacci_seq(input_num):
#     if input_num == 1 or input_num == 2:
#         return 1
#     elif input_num <= 0:
#         # return '输入不合法，请重新输入！！！'
#         raise Exception('输入不合法！！！')
#     return fibonacci_seq(input_num - 1) + fibonacci_seq(input_num - 2)
# input_num = input('请输入一个正整数：\n')
# print(input_num)
# sum = fibonacci_seq(int(input_num))
# print(sum)
'''  扩展：将第一项到第N项的结果，存为一个列表 '''
""" 
列表推导式：
[ 循环变量名 for 循环变量名 in 可迭代对象 if 条件判断]
"""
def fibonacci_seq(input_num):
    if input_num == 1 or input_num == 2:
        return 1
    elif input_num <= 0:
        # return '输入不合法，请重新输入！！！'
        raise Exception('输入不合法！！！')
    return fibonacci_seq(input_num - 1) + fibonacci_seq(input_num - 2)
fibonacci_seq(4)
input_num = int(input('请输入一个正整数：\n'))
num = range(1, input_num + 1)
lis = [fibonacci_seq(i) for i in num]
print(lis)
