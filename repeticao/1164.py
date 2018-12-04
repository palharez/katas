N = int(input())

for i in range(N):
    x = int(input())
    perfeito = 0
    for i in range(1, x):        
        if x % i == 0:
            perfeito += i
    if perfeito == x:
        print("%d eh perfeito" % x)
    else: 
        print("%d nao eh perfeito" % x)