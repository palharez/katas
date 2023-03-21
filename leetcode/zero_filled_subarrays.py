class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        def add_one(temp, n):
            aux = 0

            for i in range(n, 0, -1):
                temp[aux] += i
                aux += 1

            return temp

        resp = [0] * len(nums)
        temp = []

        for n in nums:
            if n == 0:
                temp.append(0)
            else:
                resp = add_one(resp, len(temp))
                temp = []

        if temp:
            resp = add_one(resp, len(temp))

        return sum(resp)
