from divisors import divisors


def test_1():
    assert divisors(15) == [3, 5]


def test_2():
    assert divisors(12) == [2, 3, 4, 6]


def test_3():
    assert divisors(13) == "13 is prime"
