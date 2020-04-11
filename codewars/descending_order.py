def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))


if __name__ == "__main__":
    print(descending_order(0), 0)
    print(descending_order(15), 51)
    print(descending_order(1234567809), 9876543210)
