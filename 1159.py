X = int(input())
while X != 0:
    n = 0
    soma = 0
    while n < 5:
        if X % 2 == 0:
            soma += X
            n += 1
        X += 1
    print(soma)
    X = int(input())
