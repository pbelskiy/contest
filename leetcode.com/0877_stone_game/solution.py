class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        @functools.cache
        def trace(left, right, p1, p2):
            if p1 > sum(piles[left:right + 1]):
                return True

            if left >= right:
                return p1 > p2

            return any([
                trace(left + 1, right, p1 + piles[left], p2),
                trace(left + 1, right, p1, p2 + piles[left]),
                trace(left, right - 1, p1 + piles[right], p2),
                trace(left, right - 1, p1, p2 + piles[right]),
            ])

        return True
        return trace(0, len(piles) - 1, 0, 0)
