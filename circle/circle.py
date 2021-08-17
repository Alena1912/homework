#!/usr/bin/env python

# Бабушка Зина любит печь блины своему любимому внуку Васе.
# А внук Вася любит математику и знает, что периметр и площадь блина можно найти по диаметру сковородки.
# Напишите программу, которая поможет Васе проверить его вычисления.




from math import pi



def perimeter(diameter):
    p=diameter*pi
    return p


def square(diameter):
    s=pi*(diameter/2)**2
    return s



if __name__ == "__main__":
    d = int(input("Диаметр сковородки = "))

    print('Длина блина ', format(perimeter(d),'.2f'))
    print('Площаль блина', format(square(d),'.2f'))

