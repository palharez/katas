from sum_two_smallest_numbers import sum_two_smallest_numbers

def test_1():
    assert sum_two_smallest_numbers([5, 8, 12, 18, 22]) == 13

def test_2():
    assert sum_two_smallest_numbers([7, 15, 12, 18, 22]) == 19

def test_3():
    assert sum_two_smallest_numbers([25, 42, 12, 18, 22]) == 30