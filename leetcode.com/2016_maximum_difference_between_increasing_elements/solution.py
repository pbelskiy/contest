class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        d = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                d = max(d, nums[j] - nums[i])

        if d == 0:
            return -1

        return d
