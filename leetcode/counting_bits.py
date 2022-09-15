class Solution:
    def countBits(self, n: int) -> List[int]:
        resp = []

        for n in range(n + 1):
            resp.append((str(bin(n)).count('1')))

        return resp
