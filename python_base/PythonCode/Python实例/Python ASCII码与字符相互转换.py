#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    c = input("请输入一个字符：")
    a = int(input("请输入一个ASCII码："))
    print("{}的ASCII码为：{}".format(c, ord(c)))
    print("{}对应的字符为：{}".format(a, chr(a)))
