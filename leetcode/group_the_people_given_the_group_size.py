def groupThePeople(groupSizes):
    groups = {}

    for i in range(len(groupSizes)):

        size = groupSizes[i]

        if not groups.get(size):
            groups[size] = [[]]

        if len(groups[size][-1]) == size:
            groups[size].append([])

        k = 0

        while k < len(groups[size]):
            if len(groups[size][k]) == size:
                pass

            else:
                groups[size][k].append(i)

            k += 1

    resp = []

    for _, group in groups.items():
        resp.extend(group)

    return resp


if __name__ == "__main__":
    print(groupThePeople([3, 3, 3, 3, 3, 1, 3]))
    print(groupThePeople([2, 1, 3, 3, 3, 2]))
