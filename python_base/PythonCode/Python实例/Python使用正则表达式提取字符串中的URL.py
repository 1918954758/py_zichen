#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re


def getURL(s):
    regex = "http[s]?://[w]{3}[.][\\d\\s\\w]+.com"
    url = re.findall(regex, s)
    return url

if __name__ == '__main__':
    s = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'
    print(getURL(s))
