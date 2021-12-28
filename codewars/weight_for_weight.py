def order_weight(strng):
    weights = strng.split()
    sorted_weigths = sorted(weights, key=lambda weight: (sum(int(w) for w in weight), weight))
    joined_weights = ' '.join(sorted_weigths)
    return joined_weights


if __name__ == '__main__':
    assert order_weight("103 123 4444 99 2000") == "2000 103 123 4444 99"
    assert order_weight("2000 10003 1234000 44444444 9999 11 11 22 123") == "11 11 2000 10003 22 123 1234000 44444444 9999"
    assert order_weight("") == ""