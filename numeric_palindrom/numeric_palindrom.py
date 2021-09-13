#!/usr/bin/env python

"""
Напишите функцию, которая проверяет, является ли целое положительное число палиндромом.

Можно работать только с числами, конвертировать в строку нельзя :)
"""


def is_palindrom(n: int) -> bool:
    if n <= 0:
        raise ValueError("Number must be a positive integer")

    m = n
    res = 0

    while n != 0:
        dr_ch = n % 10
        res = res * 10 + dr_ch
        n = int(n / 10)

    if (res == m):
        return True
    else:
        return False
