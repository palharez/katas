x = []
for i in range(20):
    n = int(input())
    x.append(n)

n = len(x) - 1
for i in range(len(x) // 2):
    x[i], x[n] = x[n], x[i]
    n -= 1

for i in range(len(x)):
    print("N[%d] = %d" % (i, x[i]))
