class Solution:
    def tribonacci(self, n: int) -> int:
        def T(n, memo={}):
            if memo.get(n): return memo[n]

            if n == 0: return 0

            if n <= 2: return 1

            memo[n] = T(n - 1, memo) + T(n - 2, memo) + T(n - 3, memo)

            return memo[n]

        return T(n)
