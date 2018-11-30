def main():
    y = int(input())
    x = int(input())
    if (y > x):
        resto(x, y)
    resto(y, x)


def resto(y, x):
    while y <= x:
        y += 1
        if y % 5 == 2 or y % 5 == 3 and y != x:
            print(y)


main()
