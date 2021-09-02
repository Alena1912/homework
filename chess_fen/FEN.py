#!/usr/bin/env python

"""
Напишите программу, которая использует шахматную нотацию Форсайта-Эдвардса (FEN - Forsyth–Edwards Notation)
для подсчёта баланса материала между белыми и чёрными.

- https://en.wikipedia.org/wiki/Forsyth–Edwards_Notation
- https://ru.wikipedia.org/wiki/Нотация_Форсайта_—_Эдвардса
- https://www.chessprogramming.org/Forsyth-Edwards_Notation

FEN задаёт полное расположение фигур на доске.
Относительная ценность фигур задана константами.
"""

PAWN_VAL = 1  # пешка
KNIGHT_VAL = BISHOP_VAL = 3  # конь и слон
ROOK_VAL = 5  # ладья
QUEEN_VAL = 9  # ферзь


def calc_chess_balance(fen: str) -> int:
    fen1 = fen.partition('w')
    fen=fen1[0]
    count=0
    for i in fen:
        if i=='p':
            count-=1
        elif i=='P':
            count+=1
        elif i=='n' or i=='b':
            count-=3
        elif i=='N' or i=='B':
            count+=3
        elif i=='r':
            count-=5
        elif i=='R':
            count+=5
        elif i=='q':
            count-=9
        elif i=='Q':
            count+=9
        else:
            count+=0

    return count

