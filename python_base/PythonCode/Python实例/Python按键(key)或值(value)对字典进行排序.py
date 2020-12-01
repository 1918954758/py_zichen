#!/usr/bin/python
# -*- coding: UTF-8 -*-
def dictionairy():
    # 排序key
    key_value = {}
    key_value[1] = 32
    key_value[2] = 19
    key_value[4] = 24
    key_value[3] = 45
    key_value[5] = 3
    print("按键(key)排序:")
    for i in sorted(key_value):
        print(f"({i}, {key_value[i]})", end=' ')

    print("\n按值(value)排序:")
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))


def main():
    dictionairy()


if __name__ == '__main__':
    main()
