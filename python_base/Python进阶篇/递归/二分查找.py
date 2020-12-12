#!/usr/bin/python
# -*- coding:UTF-8 -*-

def search(sequence, number, lower, upper):
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (upper - lower) // 2
        if number > sequence[middle] // 2:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)
