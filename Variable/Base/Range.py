# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: Range
# @Discription: range()函数的使用
# @Author: 子辰
# @Date: 2020-09-05 13:57
# @Software: PyCharm

# 将0 - 9 循环遍历出来
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num:
    print(i, end=" ")
print("\n")
"""
range(start, end, step)  参数只能是整型
start:计数从start开始，默认是从0开始，例如：range(10) 等价于 range(0, 10)
end:计数到end结束，但不包括end，例如：range(0, 10) 是 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 没有10
step:步长，默认为1，例如：range(0, 19, 1)
"""
for i in range(0, 10):
    print(i, end=" ")
