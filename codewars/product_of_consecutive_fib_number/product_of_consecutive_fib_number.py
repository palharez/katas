def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def productFib(prod):
    index = 0
    while True:
        n1, n2 = fib(index), fib(index + 1)
        if n1 * n2 > prod:
            return [n1, n2, False]
        elif n1 * n2 == prod:
            return [n1, n2, True]
        index += 1


if __name__ == "__main__":
    print(productFib(4895) == [55, 89, True])
    print(productFib(714))
    print(productFib(800))
    print(productFib(0))
    print(fib(11))