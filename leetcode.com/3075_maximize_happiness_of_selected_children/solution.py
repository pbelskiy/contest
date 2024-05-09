class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        t = 0
        w = 0

        for v in sorted(happiness, reverse=True)[:k]:
            if v - w <= 0:
                w += 1
                continue

            t += v - w
            w += 1

        return t
