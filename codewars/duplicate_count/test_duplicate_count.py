from duplicate_count import duplicate_count


def test_1():
    assert duplicate_count('abcde') == 0


def test_2():
    assert duplicate_count('abcdea') == 1


def test_3():
    assert duplicate_count('indivisibility') == 1
