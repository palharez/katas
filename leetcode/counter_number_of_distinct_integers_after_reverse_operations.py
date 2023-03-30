class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        counter = {}

        for n in nums:
            counter[n] = True
            reverse = int(f'{n}'[::-1])
            counter[reverse] = True

        return len(counter.keys())
