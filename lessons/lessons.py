#!/usr/bin/env python

"""
В школе, в которой учится В. Пупкин, занятия начинаются в 8 утра.
Урок длится 45 минут.
После каждого нечётного урока (1-го, 3-го, 5-го ...) перемена 5 минут,
а после каждого чётного (2-го, 4-го, 6-го ...) - 15.

Помогите непоседе Васе посчитать, когда заканчивается n-ый урок.
"""


def end_of_lesson(n: int) -> (int, int):
    hours = 8

    chtn = 0  # счетчик перемен после четных уроков
    nech = 0
    i = 1
    while i > 0 and i <= n:
        if i % 2 == 0:
            chtn += 1
        else:
            nech += 1
        i += 1

    if n % 2 == 0:
        minutes = 45 * n + nech * 5 + (chtn - 1) * 15
    else:
        minutes = 45 * n + (nech - 1) * 5 + chtn * 15

    hours = hours + minutes // 60
    minutes = minutes % 60

    return hours, minutes


if __name__ == "__main__":
    n = int(input("Номер урока: "))
    while n < 0:
        print('Количество уроков не может быть отрицательным! ')

    hours, minutes = end_of_lesson(n)

    print(f"{n}-ый урок заканчивается в {hours}:{minutes:02}")
