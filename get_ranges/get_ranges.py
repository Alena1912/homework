#!/usr/bin/env python

"""
Реализовать функцию `get_ranges` которая “сворачивает” список неповторяющихся целых чисел, отсортированных по возрастанию:

- [0, 1, 2, 3, 4, 7, 8, 10] -> "0-4, 7-8, 10"
- [4, 7, 10] -> "4, 7, 10"
- [2, 3, 8, 9]) -> "2-3, 8-9"
"""

def get_ranges(l: list) -> str:
    m = []
    for i in l:
        if not m:
            m.append([i])
        elif int(i) - pred_i == 1:
            m[-1].append(i)
        else:
            m.append([i])
        pred_i = int(i)

    final_ranges = ''

    for range_ in m:
        if len(range_) == 1:
            str_range = str(range_[0])
        elif len(range_) >= 2:
            str_range = f"{range_[0]}-{range_[-1]}"

        if final_ranges=='':
            final_ranges=str_range
        else:
            final_ranges = final_ranges + ', ' + str_range

    return final_ranges
