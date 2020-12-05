#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
A、B、C、D、E 五人在某天夜里合伙去捕鱼，到第二天凌晨时都疲惫不堪，于是各自找地方睡觉。

日上三杆，A 第一个醒来，他将鱼分为五份，把多余的一条鱼扔掉，拿走自己的一份。

B 第二个醒来，也将鱼分为五份，把多余的一条鱼扔掉拿走自己的一份。 。

C、D、E依次醒来，也按同样的方法拿鱼。

问他们至少捕了多少条鱼?
"""


# 设：至少捕了x条鱼
def minFish():
    # 计数
    count = 0
    total = []
    while True:
        count += 1
        if count >= 2:
            x = count
            # A先醒来，把鱼分成5分，每份a条，多余一条
            # x = 5 * a + 1
            if x > 1:
                a = (x - 1) / 5
            else:
                continue
            # B第二个醒来，把鱼分成5分，每份b条，多余一条
            # x = 5 * b + 1
            if x - a > 2:
                b = (x - a - 2) / 5
            else:
                continue
            # C第三个醒来，把鱼分成5份，每份c条，多余一条
            # x = 5 * c + 1
            if x - a - b > 3:
                c = (x - a - b - 3) / 5
            else:
                continue
            # D第三个醒来，把鱼分成5份，每份d条，多余一条
            # x = 5 * d + 1
            if x - a - b - c > 4:
                d = (x - a - b - c - 4) / 5
            else:
                continue
            # E第三个醒来，把鱼分成5份，每份e条，多余一条
            # x = 5 * e + 1
            if x - a - b - c - d > 5:
                e = (x - a - b - c - d - 5) / 5
            else:
                continue
            if int(str(a).split('.')[1]) == 0 and int(str(b).split('.')[1]) == 0 and int(
                    str(c).split('.')[1]) == 0 and int(str(d).split('.')[1]) == 0 and int(str(e).split('.')[1]) == 0:
                total.append(x)
        if len(total) == 10:
            return total


if __name__ == '__main__':
    total = minFish()
    print(total)
    # [3121, 6246, 9371, 12496, 15621, 18746, 21871, 24996, 28121, 31246]
    # [3121, 6246, 9371, 12496, 15621, 18746, 21871, 24996, 28121, 31246]
