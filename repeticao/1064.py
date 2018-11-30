numTotal = 0.0
numInteiros = 0
for i in range(0, 6):
    num = float(input())
    if num > 0:
        numTotal += num
        numInteiros += 1

numTotal /= numInteiros
print('%i valores positivos' % numInteiros)
print('%.1f' % numTotal)