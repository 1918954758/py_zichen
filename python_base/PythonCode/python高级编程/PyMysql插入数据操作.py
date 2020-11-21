#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

db = pymysql.connect('localhost', 'root', 'root', 'testdb')

cursor = db.cursor()

sql = """insert into employee (first_name, last_name, age, sex, income) values ('Mac', 'Mohan', 20, 'M', 2000)"""

if __name__ == '__main__':
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()
