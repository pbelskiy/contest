class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        t = m = sum(cardPoints[:k])

        for i in range(k):
            v = cardPoints[len(cardPoints) - 1 - i]
            t += v - cardPoints[k - 1 - i]
            m = max(m, t)

        return m
