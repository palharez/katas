class Solution:
    def fib(self, n: int) -> int:
        def F(n, memo={}):
            if memo.get(n): return memo[n]

            if n == 0: return 0

            if n == 1: return 1

            memo[n] = F(n - 1, memo) + F(n - 2, memo)

            return memo[n]

        return F(n)
