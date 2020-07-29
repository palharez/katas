def runningSum(nums):
    total = 0
    result = []

    for n in nums:
        total += n
        result.append(total)

    return result
