#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import datetime

if __name__ == "__main__":
    # 获得当前时间时间戳
    now = int(time.time())
    # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)

if __name__ == "__main__":
    # 获得当前时间
    now = datetime.datetime.now()
    # 转换为指定的格式
    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    print(otherStyleTime)
