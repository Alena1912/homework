#!/usr/bin/env python

"""
Напишите функцию, которая выводят n-ое число Фибоначчи.
Разрешается использовать временные переменные, циклы и условные операторы.

https://en.wikipedia.org/wiki/Fibonacci_number
"""


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Index must be >= 0")

    i = 0
    f0 = 0
    f1 = 1

    if n == 0:
        return f0

    if n == 1:
        return f1

    if n > 1:
        while i <= n - 2:
            count = f0 + f1
            f0 = f1
            f1 = count
            i = i + 1

    return f1
