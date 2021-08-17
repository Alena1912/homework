#!/usr/bin/env python

# В. Пупкин развозит пиццу. Ему сообщают адрес доствки в виде
# <улица> <номер дома>-<номер квартиры>
#
# Приезжая по указанному адресу, Вася видит f-этажное здание.
# Для простоты будем считать, что на каждом этаже в подъезде находятся 4 квартиры.
#
# Помогите Васе посчитать, в каком подъезде и на каком этаже находится нужная квартира n.
#
# Для решения понадобится использовать деление по модулю %
# или целочисленное деление //.


def find_entrance(f, n):
    """
    f - число этажей в доме
    n - номер квартиры
    """
    if n <= f * 4:
        entrance = 1
    elif n > f * 4 and n % (f * 4) == 0:
        entrance = n // (f * 4)
    else:
        entrance = n // (f * 4) + 1

    return entrance


def find_floor(f, n):

    p = f * 4
    if n > p:

        b = n - (n // p) * p
        if b <= 4 and b > 0:
            floor = 1
        elif b == 0:
            floor = f
        elif b % 4 == 0:
            floor = b // 4
        else:
            floor = (b // 4) + 1

    else:
        if n % 4 == 0:
            floor = n // 4
        else:
            floor = n // 4 + 1

    return floor


if __name__ == "__main__":
    floors = int(input("Число этажей: "))
    flat_num = int(input("Номер квартиры: "))

    entrance = find_entrance(floors, flat_num)
    floor = find_floor(floors, flat_num)
    print('Entrance: ', entrance)
    print('Floor: ', floor)


