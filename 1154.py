n = int(input())
idades = 0
qntIdade = 0
while n > 0:
    idades += n
    qntIdade += 1
    n = int(input())

print('%.2f' % (idades/qntIdade))
