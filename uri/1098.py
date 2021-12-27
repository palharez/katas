n = 0
tot = 0
for i in range(11):
    for j in range(1, 4, 1):
        tot = j + n
        if not i == 10 and not i == 0 and not i == 5:
            print('I=%.1f J=%.1f' % (n, tot))
        else:
            print('I=%.0f J=%.0f' % (n, tot))
    n += 0.2