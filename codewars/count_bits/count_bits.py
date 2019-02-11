def count_bits(n):
    return sum([1 if int(k) == 1 else 0 for k in "{0:b}".format(n)])


if __name__ == "__main__":
    print(count_bits(9))
