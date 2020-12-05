#!/usr/bin/python
# -*- coding: UTF-8 -*-
def remove1(s, n):
    li = list(s)
    del li[n - 1]
    st = ''
    for i in range(0, len(li)):
        st += li[i]
    return st


if __name__ == '__main__':
    print(remove1('ziichen', 3))
