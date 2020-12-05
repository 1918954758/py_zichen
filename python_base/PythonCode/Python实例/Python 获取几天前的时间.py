#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import datetime

if __name__ == '__main__':
    # 先获得时间数组格式的日期
    threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=3))
    # 转换为时间戳
    timeStamp = int(time.mktime(threeDayAgo.timetuple()))
    # 转换为其他字符串格式
    otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
    print(otherStyleTime)
'''
if __name__ == '__main__':
    import time
    import datetime

    # 给定时间戳
    timeStamp = 1557502800
    dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
    threeDayAgo = dateArray - datetime.timedelta(days=3)
    print(threeDayAgo)
'''