#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql

db = pymysql.connect('localhost', 'root', 'root', 'testdb')
cursor = db.cursor()
cursor.execute('drop table if exists employee')
sql = """create table employee (first_name varchar(20) not null, last_name varchar(20), age int, sex varchar(1), income float)"""

if __name__ == '__main__':
    cursor.execute(sql)
    cursor.execute("show tables")
    for table in cursor:
        print(table)
    db.close()
