def twoSum(nums, target):
    dicto = {nums[i]: i for i in range(len(nums))}
    for i in range(len(nums)):
        value = target - nums[i]
        if dicto.get(value):
            if dicto[value] == i:
                continue
            return [i, dicto[value]]


if __name__ == "__main__":
    print(twoSum([1, 2, 3], 4))  # [0, 2]
