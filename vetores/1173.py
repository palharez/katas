x = []
n = int(input())

for i in range(10):
    x.append(n)
    n = n * 2

for i in range(len(x)):
    print("N[%d] = %d" % (i, x[i]))
