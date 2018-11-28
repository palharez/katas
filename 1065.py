positivos = 0
for i in range(0, 5):
    val = int(input())
    if val % 2 == 0:
        positivos += 1

print('%i valores pares' % positivos)