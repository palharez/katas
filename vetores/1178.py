x = int(input())

n = []
n.append(x)

print("N [%.4f] = %.4f" % (0, n[0]))
for i in range(1, 100):
    n.append((n[i-1]) / 2)
    print("N [%d] = %.4f" % (i, n[i]))
