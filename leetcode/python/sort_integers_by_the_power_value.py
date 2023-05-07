class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def get_the_power_level(n, memo):
            if memo.get(n):
                return memo[n]
            
            if n == 1:
                return 0
            
            if n % 2 == 0:
                even = n / 2
                memo[n] = 1 + get_the_power_level(even, memo)
                return memo[n]

            else:
                odd = 3 * n  + 1
                memo[n] = 1 + get_the_power_level(odd, memo)
                return memo[n]

        memo = {}
        resp = []

        for i in range(lo, hi + 1):
            resp.append((get_the_power_level(i, memo), i))
        
        resp.sort()
        
        print(resp)
        
        return resp[k - 1][1]

