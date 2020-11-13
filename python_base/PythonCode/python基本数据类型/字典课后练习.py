#!/usr/bin/python
# -*- coding: UTF-8 -*-

country_counter = {}


def addone(country):
    if country in country_counter:
        country_counter[country] += 1
    else:
        country_counter[country] = 1


if __name__ == '__main__':
    addone('China')
    addone('Japan')
    addone('china')
    print(country_counter)
    print(len(country_counter))
