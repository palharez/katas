
def countKDifference(nums, k):
    result = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                result += 1

    return result

if __name__ == "__main__":
    # print(countKDifference(nums = [1,2,2,1], k = 1)) # 4
    # print(countKDifference(nums = [1,3], k = 3)) # 0
    print(countKDifference(nums = [3,2,1,5,4], k = 2)) # 3
