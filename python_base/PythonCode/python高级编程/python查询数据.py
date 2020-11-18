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
# mycursor.execute("select * from sites")
mycursor.execute("select name, url, id from sites")
# myresult = mycursor.fetchall()  # 获取所有记录
if __name__ == '__main__':
    # for x in myresult:
    #     print(x)

    print('=============')
    print(mycursor.fetchone())
