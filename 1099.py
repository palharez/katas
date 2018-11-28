def impares(v1, v2):
    v2 += 1
    impares = 0
    for i in range(v2, v1, 1):
        if i % 2 != 0:
            impares += i
    return impares

n = int(input())
somaImpares = 0

for i in range(n):
    v1, v2 = input().split(" ")
    v1 = int(v1)
    v2 = int(v2)
    if v1 > v2:
        print(impares(v1, v2))
    else:
        print(impares(v2, v1))

