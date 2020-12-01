#!/usr/bin/python
# -*- coding: UTF-8 -*-

def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum += myDict[i]
    return sum


def main(obj):
    return returnSum(obj)


if __name__ == "__main__":
    dict = {'a': 12, 'b': 32, 'c': 43}
    print(main(dict))
