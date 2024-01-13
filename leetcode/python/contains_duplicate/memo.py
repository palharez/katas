def contains_duplicate(nums):
  memo = {}

  for num in nums:
    if memo.get(num):
      return True

    memo[num] = True

  return False

if __name__ == '__main__':
  print(contains_duplicate(nums=[1,2,3,1]), True)
  print(contains_duplicate(nums=[1,2,3,4]), False)
  print(contains_duplicate(nums=[1,1,1,3,3,4,3,2,4,2]), True)
