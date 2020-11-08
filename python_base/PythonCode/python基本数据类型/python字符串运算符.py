#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 'Hello'
b = 'Python'

if __name__ == '__main__':
    print("a + b输出结果：", a + b)
    print("a * 2输出结果：", a * 2)
    print("a[1]输出结果：", a[1])
    print("a[1:4]输出结果：", a[1:4])

    if "H" in a:
        print("H在变量a中")
    else:
        print("H不爱变量a中")
    if "M" not in a:
        print("M不在变量a中")
    else:
        print("M在变量a中")
    print(r'\n')
    print(R'\n')