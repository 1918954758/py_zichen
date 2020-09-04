# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: TransferDataType
# @Discription: 4种数据类型之间的转换   int()     float()     str()       bool()
# @Author: 子辰
# @Date: 2020-09-04 23:40
# @Software: PyCharm

a1 = 20000
b1 = "1000"
# 将数据转成int类型
c1 = int(b1)
print(a1 + c1)

a = "35"
b = 50
c = 3.14
d = ""
e = 0
f = None
print("转换前", type(a))
a = float(a)
print("转换后", type(a))
print("转换前", type(a))
x1 = bool(a)
x2 = bool(b)
x3 = bool(d)
x4 = bool(c)
x5 = bool(e)
x6 = bool(f)
print("转换后", type(x1), x1)
print("转换后", type(x2), x2)
print("转换后", type(x3), x3)
print("转换后", type(x4), x4)
print("转换后", type(x5), x5)
print("转换后", type(x6), x6)
