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
if __name__ == '__main__':
    mycursor.execute("create table sites (name varchar(255), url varchar(255))")
