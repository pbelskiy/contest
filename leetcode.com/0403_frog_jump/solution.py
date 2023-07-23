class Solution:
    def canCross(self, stones: List[int]) -> bool:

        @cache
        def dp(i, k):
            if i == len(stones) - 1:
                return True

            for j in range(i + 1, len(stones)):
                d = abs(stones[i] - stones[j])

                if d in (k - 1, k, k + 1) and dp(j, d):
                    return True

            return False

        return dp(0, 0)
