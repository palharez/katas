class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        result = 0
        for num in range(n + 1):
            if num % m == 0:
                result -= num
            if num % m != 0:
                result += num
        return result
