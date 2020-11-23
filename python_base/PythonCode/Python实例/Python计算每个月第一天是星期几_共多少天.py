#!/usr/bin/python
# -*- coding: UTF-8 -*-
import calendar

tu = calendar.monthrange(2020, 10)

if __name__ == "__main__":
    print(tu)
    print("2020年10月第一天是星期{}".format(tu[0] + 1))
    print("2020年10月一共有{}天".format(tu[1]))
