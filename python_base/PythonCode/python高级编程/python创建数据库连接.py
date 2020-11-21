#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

if __name__ == '__main__':
    print(mydb)
    mydbcursor = mydb.cursor()
    # 创建数据库
    # mydbcursor.execute("create database runoob_db")
    # 查看数据库
    mydbcursor.execute("show databases")
    for mydbc in mydbcursor:
        print(mydbc)
