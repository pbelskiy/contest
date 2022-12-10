class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return abs(stones[0] - stones[1])

        # to simplify logic below
        if len(stones) % 2 == 0:
            stones.append(stones[-1] + 1)

        j = 0

        # -> go forward
        for i in range(0, len(stones) - 2, 2):
            j = max(j, abs(stones[i] - stones[i+2]))

        # <- go backward
        for i in range(1, len(stones) - 2, 2):
            j = max(j, abs(stones[i] - stones[i+2]))

        return j
