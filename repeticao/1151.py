y = int(input())
fib1 = 0
fib2 = 1
print(fib1, end=" ")
print(fib2, end=" ")
for i in range(y - 2):
    n = fib2 + fib1
    fib1 = fib2
    fib2 = n
    if (i == (y - 3)):
        print(n)
    else:
        print(n, end=" ")
