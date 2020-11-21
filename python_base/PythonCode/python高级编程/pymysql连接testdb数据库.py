#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql

db = pymysql.connect('localhost', 'root', 'root', 'testdb')
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
if __name__ == '__main__':
    print(data)

db.close()
