def printer(v1, v2):
    sum = 0
    for i in range(v2, v1 + 1, 1):
        sum += i
        print(i, end=" ")
    print("Sum=%i" % sum)
    return

i = 1
while i != 0:
    a, b = input().split()
    a = int(a)
    b = int(b)

    if a <= 0 or b <= 0:
        break
    
    if a > b:
        printer(a, b)
    else:
        printer(b, a)
    

