from tribonacci import tribonacci


def test_1():
    assert tribonacci([1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]


def test_2():
    assert tribonacci([0, 0, 1], 10) == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]


def test_3():
    assert tribonacci([0, 1, 1], 10) == [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
