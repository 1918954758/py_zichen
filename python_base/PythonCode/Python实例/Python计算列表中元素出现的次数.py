#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
计算列表中元素出现的次数
"""
li = [1, 1, 1, 1, 2, 3, 3, 5, 546, 5, 7, 6, 8, 79, 809, 2, 78, 67, 789870, 34, 6, 8, 4, 9, 0, 3, 4]


def li_count(n, li):
    count = 0
    for x in range(0, len(li)):
        if n == li[x]:
            count += 1
    return count


def li_c(n, li):
    return li.count(n)


if __name__ == "__main__":
    print(f"使用自定义方法：{li_count(1, li)}")
    print(f"使用count：    {li_c(1, li)}")
