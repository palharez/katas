N = int(input())
for i in range(N):
    x, y = input().split()
    x = int(x)
    y = int(y)
    n = 0
    soma = 0
    while n < y:
        if x % 2 != 0:
            soma += x
            n += 1
        x += 1
    print(soma)
