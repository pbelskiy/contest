class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        r = 0
        j = len(piles)

        for i in range(len(piles) // 3):
            r += piles[j - 2]
            j -= 2

        return r
