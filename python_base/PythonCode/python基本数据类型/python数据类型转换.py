#!/usr/bin/python
# -*- coding: UTF-8 -*-


if __name__ == '__main__':
    # int(x, base)
    print(int('12', 16))  # 12是十六进制数
    print(int('10', 8))
    print(int('1', 2))
    # float(x)
    print(float(45))
    # complex(real, imag)
    print(complex(2))
    print(complex(1, 2))
    # str(x)
    print(str(19))
    print(str(False))
    print(str(True))
    # repr(x)
    print(repr(12))
    print(repr('3s'))
    # eval(str)
    print(eval('3 * 7'))
    print(eval('pow(2, 2)'))
    print(eval('2 + 2'))
    # tuple(s)
    print(tuple('23465gsfwey'))
    # list(s)
    print(list('3ret54fer32tgre'))
    # set(s)
    print(set('3ffq43few'))
    # dict(d)
    print(dict({1: 2, 2: 3, 4: 2}))
    # frozenset(s)
    print(frozenset('fqewfq34tt455y34tf'))
    # chr(x)
    print(chr(0x30), chr(0x31), chr(0x61))      # 十六进制
    print(chr(48), chr(49), chr(97))            # 十进制
    # ord(x)        将一个字符转换为它的整数值
    print(ord('s'))
    # ord('fd')  会报错
    # hex(x)
    print(hex(3))       # 转换成十六进制
    # oct(x)
    print(oct(87))      # 转换为八进制