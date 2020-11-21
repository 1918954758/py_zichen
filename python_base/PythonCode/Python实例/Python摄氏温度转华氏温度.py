#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 用户输入摄氏温度
celsius = float(input("请输入摄氏温度："))
# 计算
fahrenheit = (celsius * 1.8) + 32
if __name__ == '__main__':
    print("%.1f°C 摄氏温度转为华氏温度为 %.1fF" % (celsius, fahrenheit))
