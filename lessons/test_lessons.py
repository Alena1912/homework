from lessons import end_of_lesson


def test_1():
    assert end_of_lesson(1) == (8, 45)


def test_2():
    assert end_of_lesson(2) == (9, 35)


def test_3():
    assert end_of_lesson(3) == (10, 35)


def test_4():
    assert end_of_lesson(4) == (11, 25)


def test_5():
    assert end_of_lesson(5) == (12, 25)


def test_6():
    assert end_of_lesson(6) == (13, 15)


def test_7():
    assert end_of_lesson(7) == (14, 15)


def test_8():
    assert end_of_lesson(8) == (15, 5)


def test_9():
    assert end_of_lesson(9) == (16, 5)


def test_10():
    assert end_of_lesson(10) == (16, 55)
