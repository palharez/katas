n = int(input())
inn = 0
out = 0

for i in range(n):
    x = int(input())
    if x >= 10 and x <= 20:
        inn += 1
    else:
        out += 1

print('%i in' % inn)
print('%i out' % out)