def twoSum_dp(nums, target):
    """
        Nos iteramos pelo array e verificamos se o valor que procuramos existe no array
        A cada iteração nós preenchemos o array com I

        We iterate over the array to verify if the needed value already exists in our
        hash map.
        In the end of each iteration we put I on hash map.

        O(n)
    """
    hm = {}
    for i, n in enumerate(nums):
        diff = target - n

        if diff in hm:
            return [hm.get(diff), i]

        hm[n] = i


def twoSum_brute(nums, target) :
    """
    Time: O(n^2)
    """
    for i in range(len(nums)):
        for n in range(i + 1, len(nums)):
            if nums[i] + nums[n] == target:
                return [i, n]


if __name__ == "__main__":
    assert twoSum_brute([1,2,3], 4) == [0, 2]
    assert twoSum_dp([1,2,3], 4) == [0, 2]

