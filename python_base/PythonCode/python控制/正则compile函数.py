#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

pattern = re.compile(r'\d')

if __name__ == '__main__':
    m = pattern.match('nda34k4l3252kl43j')
    print(m)
    m2 = pattern.match('nda34k4l3252kl43j', 2, 5)
    print(m2)
    m3 = pattern.match('nda34k4l3252kl43j', 3, 10)
    print(m3)
    print(m3.group())
    print(m3.start())
    print(m3.end())
    print(m3.span())

print('===============================')
pattern1 = re.compile(r'\d+')
if __name__ == '__main__':
    ma = pattern1.findall('nda34k4l3252kl43j')
    print(ma)
    ma2 = pattern1.findall('nda34k4l3252kl43j', 2, 5)
    print(ma2)
    ma3 = pattern1.findall('nda34k4l3252kl43j', 3, 10)
    print(ma3)

print('=================')
it = re.finditer(r'\d+', '1fd324r3gfs23rf')

if __name__ == '__main__':
    print(it)
    for match in it:
        print(match.group())

print('===================')

split1 = re.split(r'\d+', '32r4fq8934hg89fhv2h')
split2 = re.split(r'\D+', '32r4fq8934hg89fhv2h')

if __name__ == '__main__':
    print(split1)
    print(split2)