n = int(input())
resultado = 0

for i in range (1, n+1):
    if i % 2 == 0:
        resultado = i ** 2
        print(str(i) + "^2 = " + str(resultado))