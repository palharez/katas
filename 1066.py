pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(0, 5):
    val = int(input())
    if val % 2 == 0:
        pares += 1
    if val % 2 != 0:
        impares += 1
    if val > 0:
        positivos += 1
    if val < 0:
        negativos += 1

print('%i valor(es) par(es)' % pares)
print('%i valor(es) impar(es)' % impares)
print('%i valor(es) positivo(s)' % positivos)
print('%i valor(es) negativo(s)' % negativos)