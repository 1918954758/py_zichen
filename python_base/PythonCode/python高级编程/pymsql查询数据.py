#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

db = pymysql.connect('localhost', 'root', 'root', 'testdb')
cursor = db.cursor()
sql = """select * from employee where income > %s"""
na = (1000,)

if __name__ == '__main__':
    try:
        cursor.execute(sql, na)
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            print("fname=%s, lname=%s, age=%s, sex=%s, income=%s" % (fname, lname, age, sex, income))
    except:
        print('Error: unable to fetch data')
    db.close()
