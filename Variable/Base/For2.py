# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: For2
# @Discription: for循环与continue/break的组合使用
# @Author: 子辰
# @Date: 2020-09-05 14:08
# @Software: PyCharm

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in a:
#     if i == 5:
#         break
#     print(i, end=" ")
# else:
#     print("for-break循环结束")

for i in a:
    if i == 2:
        continue
    print(i, end=" ")
else:
    print("for-continue循环结束")

