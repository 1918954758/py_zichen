#!/usr/bin/python
# -*- coding: UTF-8 -*-
import calendar

if __name__ == '__main__':
    yyyy = input("请输入年份：")
    mm = input("请输入月份：")
    print(calendar.month(int(yyyy), int(mm)))
