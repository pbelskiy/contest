"""
Sort and try to use the highest possible value.

TC: O(NlgN)
SC: O(N)
"""
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        t = 0
        m = float('inf')
        v = set()

        for n in sorted(maximumHeight, reverse=True):
            if n in v:
                n = m - 1

            if n < 1:
                return -1

            t += n
            v.add(n)
            m = min(m, n)

        return t
