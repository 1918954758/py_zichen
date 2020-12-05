#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
1. 删除某个元素
2. 清空列表
3. 删除列表
"""
li = [1, 3, 5, 7, 9]
if __name__ == '__main__':
    print(f"原列表{li}")
    del li[1]
    print(f"删除元素'3'之后的列表{li}")
    li.clear()
    print(f"清空列表{li}")
    del li
    print(f"删除列表{li}")