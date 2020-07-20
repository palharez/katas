def remove_duplicates(nums):
    solution = {}

    for n in nums:
        solution[n] = 0

    return [*solution]


if __name__ == "__main__":
    print(remove_duplicates([1, 1, 2]))
    print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
