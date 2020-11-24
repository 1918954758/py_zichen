#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


if __name__ == '__main__':
    print(getYesterday())
