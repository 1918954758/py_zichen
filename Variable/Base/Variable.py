# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: Variable
# @Discription: python中的变量介绍
# @Author: 子辰
# @Date: 2020-09-05 11:26
# @Software: PyCharm

# 变量的赋值
a = 1
print(a)
a = b = c = 2
a, b, c, d = 1, 2, 3, 4
print(a, b, c, d)
a = [1, 2, 3, 4]
print(a)

# 变量的命名规则
"""
1. 变量只能包含 字母，数字，下划线。变量名可以字母或者下划线开头，但不可以数字开头
2. 不能将python中的关键字作为变量名
    False       class       finally     is          return
    True        continue    for         lambda      try
    None        def         from        nonlocal    while
    and         del         gloabl      not         with
    as          elif        if          or          yield
    assert      else        import      pass        break
    raise       except      in
3. 变量名最好精简又具有面属性
4. 变量名最好使用小写字母，不建议使用大写字母
"""


