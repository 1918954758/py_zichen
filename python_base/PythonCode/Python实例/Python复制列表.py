#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
复制列表
"""

li = [1, 2, 3, 4, 6]

if __name__ == "__main__":
    li_copy = li.copy()
    print(f"使用copy()：\n原：\t{li} \n复制后：\t{li_copy}")
    print()
    #
    li_ = li[:]
    print(f"使用切割[:]：\n原：\t{li} \n复制后：\t{li_}")
    print()
    #
    li_extend = []
    li_extend.extend(li)
    print(f"使用extend：\n原：\t{li} \n复制后：\t{li_extend}")
    print()
    #
    li_list = list(li)
    print(f"使用list：\n原：\t{li} \n复制后：\t{li_list}")