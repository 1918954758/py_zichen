#!/usr/bin/python
# -*- coding: UTF-8 -*-

nterms = int(input("你需要几项？"))


def fiboooooo():
    # 第一项
    n1 = 0
    # 第二项
    n2 = 1

    count = 2
    # 判断输入的值是合法
    if nterms <= 0:
        print("请输入一个正整数。")
    elif nterms == 1:
        print("斐波那契数列：")
        print(n1)
    else:
        print("斐波那契数列：")
        print(n1, ",", n2, end=" , ")
        while count < nterms:
            nth = n1 + n2
            print(nth, end="  ,  ")
            # 更新值
            n1 = n2
            n2 = nth
            count += 1


if __name__ == '__main__':
    fiboooooo()
