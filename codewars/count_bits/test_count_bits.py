from count_bits import count_bits


def test_1():
    assert count_bits(0) == 0


def test_2():
    assert count_bits(4) == 1


def test_3():
    assert count_bits(7) == 3


def test_4():
    assert count_bits(9) == 2


def test_5():
    assert count_bits(10) == 2
