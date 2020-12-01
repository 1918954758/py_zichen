#!/usr/bin/python
# -*- coding: UTF-8 -*-
def Marge1(arg1, arg2):
    marge = {**arg1, **arg2}
    return marge


def Marge2(arg1, arg2):
    return (arg1.update(arg2))


if __name__ == "__main__":
    # 使用星星来合并字典，由于星星会将参数转成字典来传递
    a = {1: 1}
    b = {2: 2}
    print(Marge1(a, b))
    # 使用update()  将b 合并到a中，所以Marge2(a, b)返回None
    print(Marge2(a, b))  # None
    print(a)  # {1: 1, 2: 2}
