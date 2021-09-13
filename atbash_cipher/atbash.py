#!/usr/bin/env python

"""
Напишите программу, которая кодирует и декодирует текст шифром Атбаш.
В этом шифре каждая i-ая буква алфавита заменяется i-ой буквой с его конца, например, для латинского алфавита: a - z, b - y и т.д.

- заглавные буквы переводятся в строчные
- пробельные символы и знаки препинания опускаются
- шифр идёт блоками по 5 символов, между ними пробел

Пример:

`Bambarbia, Kirgudu` -> `yznyz iyrzp ritfw f`
"""

import string

BLOCK_SIZE = 5
LIT = 'abcdefghijklmnopqrstuvwxyz'
TIL = LIT[::-1]


def atbash_encode(text: str) -> str:
    line = ''

    text = text.lower()

    text = ''.join(i for i in text if i.isalnum())

    for i in text:
        if i in LIT:
            ind = LIT.find(i)
            line = line + TIL[ind]
        else:
            line = line + i

    line = [line[i:i + 5] for i in range(0, len(line), 5)]

    cipher = " ".join(str(elem) for elem in line)

    return cipher


def atbash_decode(cipher: str) -> str:
    line = ''
    cipher = ''.join(i for i in cipher if i.isalnum())

    for i in cipher:
        if i in LIT:
            ind = LIT.find(i)
            line = line + TIL[ind]
        else:
            line = line + i

    return line
