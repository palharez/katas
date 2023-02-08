def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    counter = {}

    for n in nums:
        if not counter.get(n):
            counter[n] = 0

        counter[n] += 1

    sorted_v = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    return [n[0] for n in sorted_v[:k]]
