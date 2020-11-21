#!/usr/bin/python
# -*- coding: UTF-8 -*-

dec = int(input("请输入一个数字："))

if __name__ == '__main__':
    print("十进制数为：{}".format(dec))
    print("转换为二进制为：{}".format(bin(dec)))
    print("转换为八进制为：{}".format(oct(dec)))
    print("转换为十六进制为：{}".format(hex(dec)))
