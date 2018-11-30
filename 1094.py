n = int(input())
coelhos = 0
ratos = 0
sapos = 0
total = 0

for i in range(n):
    qnt, cob = input().split(" ")
    qnt = int(qnt)
    if cob == 'C':
        coelhos += qnt
    elif cob == 'R':
        ratos += qnt
    elif cob == 'S':
        sapos += qnt
    total += qnt

percol = (coelhos * 100) / total
perrat = (ratos * 100) / total
persap = (sapos * 100) / total

print('Total: %i cobaias' % total)
print('Total de coelhos: %i' % coelhos)
print('Total de ratos: %i' % ratos)
print('Total de sapos: %i' % sapos)
print('Percentual de coelhos: %.2f ' % percol + '%')
print('Percentual de ratos: %.2f ' % perrat + '%')
print('Percentual de sapos: %.2f ' % persap + '%')
