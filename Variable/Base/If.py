# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: If
# @Discription: if条件语句
# @Author: 子辰
# @Date: 2020-09-05 13:13
# @Software: PyCharm

"""
if condition:
    expression
other_expression
"""
# eg:
a = True
if a:
    print("执行条件")
print("执行完成")

b = False
if b:
    print("执行条件")
print("执行完成")

print("》》》》》》》》》》》》》》》》》》》》》分割线《《《《《《《《《《《《《《《《《《《《《《")

"""
if condition:
    ture_expression
else:
    false_expression
other_expression
"""
a = 1
b = 2
if a == b:
    print("等式成立")
else:
    print("等式不成立")
print("执行完毕")

"""
if-else 可以嵌套：但是不太优雅
if xxx:
    xxx
else:
    if xxx:
        xxx
    else:
        if xxx:
            xxx
        else:
            xxx
在python中可以使用 if-elif-else来书写：方便阅读
if xxx:
    xxx
elif xxx:
    xxx
elif xxx:
    xxx
else:
    xxx
"""