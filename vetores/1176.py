y = 60
fib1 = 0
fib2 = 1
vetFib = []
vetFib.append(fib1)
vetFib.append(fib2)
for i in range(y - 1):
    n = fib2 + fib1
    fib1 = fib2
    fib2 = n
    vetFib.append(n)

T = int(input())
for i in range(T):
    n = int(input())
    print("Fib(%d) = %d" % (n, vetFib[n]))
