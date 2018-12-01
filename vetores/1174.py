x = []
for i in range(100):
    n = float(input())
    x.append(n)

for i in range(len(x)):
    if x[i] <= 10:
        print("A[%d] = %.1f" % (i, x[i]))
