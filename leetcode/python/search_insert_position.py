def searchInsert(nums, target):
    return binary_search(nums, 0, len(nums) -1, target)

def binary_search(arr, low, high, x):
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return low

if __name__ == '__main__':
    # print(searchInsert(nums = [1,3,5,6], target = 2))
    print(searchInsert(nums = [1,3,5,6], target = 7))

