#!/usr/bin/env python

"""
Напишите *генератор* пар соседних чисел Фибоначчи (в функции вместо `result` будет `yield`):

(1, 1), (1, 2), (2, 3), (3, 5), (5, 8) ...

https://en.wikipedia.org/wiki/Fibonacci_number

С помощью генератора найдите 2 таких числа Фибоначчи,
через которые можно будет вычислить золотое сечение c заданной точностью.

https://en.wikipedia.org/wiki/Golden_ratio#Relationship_to_Fibonacci_sequence
"""

# Golden Ratio
GOLDEN = (1 + 5 ** 0.5) / 2  # (a+b)/a or b/a
import math


def fib_pair_gen():
    """
    Generator to produce Fibonacci numbers indefinitely.
    """
    a = b = 1

    while 1:
        yield a, b
        a, b = b, a + b


def fib_phi_calc(precision: float) -> (int, int):
    """
    Returns 2 consecutive Fibonacci numbers to calculate Golden Ratio with a given precision.
    """
    for a, b in fib_pair_gen():  # pary iz generatora
        pogr = abs(GOLDEN - b / a)  # pogreshnost'
        if precision >= pogr:
            return a, b
