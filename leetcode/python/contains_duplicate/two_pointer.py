def contains_duplicate(nums):
  for i in range(len(nums)):
    for k in range(i + 1, len(nums)):
      if nums[i] == nums[k]:
        return True

  return False

if __name__ == '__main__':
  print(contains_duplicate(nums=[1,2,3,1]), True)
  print(contains_duplicate(nums=[1,2,3,4]), False)
  print(contains_duplicate(nums=[1,1,1,3,3,4,3,2,4,2]), True)
