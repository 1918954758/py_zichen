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
mycursor.execute("show tables")
if __name__ == '__main__':
    for table in mycursor:
        print(table)
