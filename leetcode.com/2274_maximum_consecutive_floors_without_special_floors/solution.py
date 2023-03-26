class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()

        m = max(special[0] - bottom, top - special[-1])

        for i in range(len(special) - 1):
            m = max(m, special[i + 1] - special[i] - 1)

        return m
