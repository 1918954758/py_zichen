#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 使用 in 判断
def substrIsHas(sub, origin):
    if sub in origin:
        print("存在")
    else:
        print("不存在")


if __name__ == '__main__':
    print('==========================')
    substrIsHas('zichen', 'www.zichen.com')
    substrIsHas('zichen', 'wwwzichencom')
    substrIsHas('zichene', 'wwwzichencom')


# 使用方法 str.find(子串, 原串)
def substrIsHas1(sub, origin):
    if origin.find(sub) >= 0:
        print("存在")
    else:
        print("不存在")
    '''
    if origin.find(sub) == -1:
        print("不存在")
    else:
        print("存在")
    '''


if __name__ == '__main__':
    print('==========================')
    substrIsHas1('zichen', 'www.zichen.com')
    substrIsHas1('zichen', 'wwwzichencom')
    substrIsHas1('zichene', 'wwwzichencom')
