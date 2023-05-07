class Solution:
    def divisorGame(self, n: int) -> bool:
        alice = False

        while n > 1:
            alice = True if not alice else False

            n -= 1

        return alice
