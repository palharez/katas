def impar(n1, n2):
    impares = 0
    n2 += 1
    while n2 < n1:
        if n2 % 2 != 0:            
            impares += n2
        n2 += 1
    return impares

n1 = int(input())
n2 = int(input())

if n1 > n2:
    print(impar(n1, n2))
elif n2 > n1:
    print(impar(n2, n1))
else:
    print(0)

