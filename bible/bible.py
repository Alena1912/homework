#!/usr/bin/env python

"""
Напишите функцию, которая находит n наиболее употребляемых слов из Библии.
Слова в возвращаемом списке идут по убыванию их частоты использования.
"""

import re
import string

from pathlib import Path

f = Path(__file__).parent.absolute() / "king_james_bible.txt"
BIBLE = f.read_text()


def most_freq_bible_words(n: int) -> list:
    d = {}
    list_word = []
    list = []

    bible = BIBLE.lower()
    word_count = re.findall(r'[a-z]{1,15}\b', bible)

    for word in word_count:
        count = d.get(word, 0)
        d[word] = count + 1

    sorted_values = sorted(d.values())
    sorted_d = {}

    for i in sorted_values:
        for k in d.keys():
            if d[k] == i:
                sorted_d[k] = d[k]
                break

    for key in sorted_d:
        list_word.append(key)

    list_word = list_word[::-1]
    list = list_word[0:n]

    return list


if __name__ == "__main__":
    print(*most_freq_bible_words(10), sep="\n")
