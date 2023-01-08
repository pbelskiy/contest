class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        a, b = 0, 0

        for n in nums:
            if n > 0:
                a += 1
            elif n < 0:
                b += 1

        return max(a, b)
