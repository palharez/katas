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

# Chat Solution
def count_subarrays(nums):
    """
        We define two pointers: left and right. The left pointer starts at the beginning of the array, and the right pointer starts at the same position as the left pointer.
        We move the right pointer until we find a zero in the array. Once we find a zero at index i, we know that any subarray containing this zero will be a combination of subarrays on the left and right side of the zero.
        We can count the number of subarrays with this zero by taking the product of the number of zeros on the left side of the
        zero and the number of zeros on the right side of the zero. We can do this because any subarray containing this zero will be a combination of subarrays on the left and right side of the zero.
        We move the left pointer to the next index after the zero and repeat steps 2-3 until the end of the array is reached.
        Finally, we sum up the counts obtained in step 3 to get the total number of subarrays filled with 0.
        Here's a Python implementation of the sliding window technique:
    """
    left, right = 0, 0
    count = 0
    while right < len(nums):
        if nums[right] == 0:
            # calculate number of subarrays with this zero
            count += (right - left + 1) * (nums[left:right+1].count(0))
            # move left pointer to next index
            left = right + 1
        right += 1
    return count
