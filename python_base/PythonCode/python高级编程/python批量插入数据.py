#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="runoob_db"
)
mycursor = mydb.cursor()
sql = "insert into sites (name, url) values (%s, %s)"
val = [('Google', 'https://www.google.com'), ('Github', 'https://www.github.com'), ('Taobao', 'https://www.taobao.com'),
       ('stackoverflow', 'https://www.stackoverflow.com/')]
if __name__ == '__main__':
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "记录插入成功。")
