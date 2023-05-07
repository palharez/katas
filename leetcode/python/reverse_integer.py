def reverse_integer(x):
    x_string = str(x)[::-1]
    MAX_BIT = 2147483648

    if len(x_string) == 1:
        return x

    minus = '-'
    asw = []
    insert_minus = False

    for n in x_string:
        if n == minus:
            insert_minus = True
            continue
        if n == '0' and len(asw) == 0:
            continue
        else:
            asw.append(n)

    if insert_minus:
        asw.insert(0, minus)

    asw_int = int(''.join(asw))

    return asw_int if abs(asw_int) <= MAX_BIT else 0


if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(10))
    print(reverse_integer(-10))
    print(reverse_integer(0))
    print(reverse_integer(100))
    print(reverse_integer(1534236469))


