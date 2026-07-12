class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        t = 0

        for n in sorted(nums, reverse=True)[:k]:
            if mul > 0:
                t += n*mul
                mul -= 1
            else:
                t += n

        return t

