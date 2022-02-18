def createTargetArray(nums, index):
    result = []

    for i in range(len(nums)):
        result.insert(index[i], nums[i])

    return result

if __name__ == '__main__':
    print(createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1])) # [0,4,1,3,2]

    print(createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,3,0])) # [0,1,2,3,4]
