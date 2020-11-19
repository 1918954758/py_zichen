#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql

db = pymysql.connect("localhost", "root", "root")

pycursor = db.cursor()

if __name__ == '__main__':
    pycursor.execute("create database TESTDB")