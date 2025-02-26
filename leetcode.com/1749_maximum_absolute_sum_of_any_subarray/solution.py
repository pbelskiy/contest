"""
Use Kadane alghorithm twice.

TC: O(N)
SC: O(1)
"""
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Kadan's max sum
        t, m = 0, 0
        for n in nums:
            t += n
            m = max(m, t)
            if t < 0:
                t = 0

        max_sum = m

        # Kadan's min sum
        t, m = 0, 0
        for n in nums:
            t += n
            m = min(m, t)
            if t > 0:
                t = 0

        min_sum = m

        return max(abs(min_sum), abs(max_sum))
