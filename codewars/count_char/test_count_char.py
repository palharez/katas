from count_char import count


def test_1():
    assert count('aba') == {'a': 2, 'b': 1}


def test_2():
    assert count('') == {}