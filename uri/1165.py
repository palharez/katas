n = int(input())
for i in range(n):
    x = int(input())
    impar = 0
    for i in range(1, x + 1):
        if x % i == 0:
            impar += 1
    
    if impar <= 2:
        print('%d eh primo' % x)
    else:
        print('%d nao eh primo' % x)