#!/usr/bin/env python

"""
Напишите функцию, которая проверяет "силу" пароля.

Надёжный пароль:
    - не менее 10 символов
    - содержит буквы разного регистра
    - минимум одну цифру
    - минимум один знак пунктуации
"""
import string

def is_strong_password(pwd: str) -> bool:
    BB='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    MB='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    count = 0

    UP=string.ascii_uppercase+BB
    LWD=string.ascii_lowercase+MB

    if len(pwd)>=10:
        count+=1
    else:
        return False

    for i in pwd:
        if i in UP: #string.ascii_uppercase or BB:
            count+=1
            break

    for i in pwd:
        if i in LWD: #string.ascii_lowercase or MB:
            count+=1
            break

    for i in pwd:
        if i in string.digits:
            count+=1
            break

    for i in pwd:
        if i in string.punctuation:
            count+=1
            break

    if count==5:
        return True
    else:
        return False
