def valores(X, Y):
    soma = 0
    for i in range(X, Y+1):
        if i % 13 == 0:
            continue
        soma += i
    return soma

X = int(input())
Y = int(input())

if(X > Y):
    print(valores(Y, X))
else:
    print(valores(X, Y))
