def missing_number(nums):
    res = len(nums)

    for i in range(len(nums)):
        res += i - nums[i]

    return res

if __name__ == "__main__":
    print(missing_number([9,6,4,2,3,5,7,0,1]))
    print(missing_number([0,1]))
    print(missing_number([0,1,2,3,5]))
