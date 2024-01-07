def two_sum(numbers, target):
  pointer_a = 0
  pointer_b = len(numbers) - 1

  while pointer_a < pointer_b:
      summed = numbers[pointer_a] + numbers[pointer_b]

      if summed == target:
          return [pointer_a + 1, pointer_b + 1]
      elif summed < target:
          pointer_a += 1
      else:
          pointer_b -= 1

  return False

if __name__ == '__main__':
  print(two_sum(numbers = [2,7,11,15], target = 9), [1,2])
  print(two_sum(numbers = [2,3,4], target = 6), [1,3])
  print(two_sum(numbers = [-1,0], target = -1), [1,2])
