"""
Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9
for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
"""

def multiplication_table(size):
    table = []

    for i in range(1, size + 1):
        row = [i]

        for _ in range(size - 1):
            row.append(i + row[-1])

        table.append(row)

    return table

if __name__ == '__main__':
    print(multiplication_table(3), [[1,2,3],[2,4,6],[3,6,9]])
    print(multiplication_table(15))

