#!/usr/bin/env python

"""
Напишите функцию, которая возвращает для чисел:

- кратных 3 - Fizz
- кратных 5 - Buzz
- одновременно кратных и 3 и 5 - FizzBuzz
- строковое представление этих чисел (т.е. "1" для 1)

https://en.wikipedia.org/wiki/Fizz_buzz
"""


def fizzbuzz(n: int) -> str:
    if (n % 3 == 0 and n % 5 == 0):
        a = 'FizzBuzz'
        return a
    elif n % 3 == 0:
        a = 'Fizz'
        return a
    elif n % 5 == 0:
        a = 'Buzz'
        return a
    else:
        num = str(n)
        return num
