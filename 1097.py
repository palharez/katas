m = 7
for i in range(1, 10, 2):
    n = m
    for j in range(3):        
        print('I=%i J=%i' % (i, n))
        n -= 1
    m += 2