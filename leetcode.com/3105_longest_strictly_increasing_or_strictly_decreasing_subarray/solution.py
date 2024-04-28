class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        m = 1

        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):
                if nums[j] <= nums[j - 1]:
                    break
                m = max(m, j - i + 1)

            for j in range(i + 1, len(nums)):
                if nums[j] >= nums[j - 1]:
                    break
                m = max(m, j - i + 1)

        return m
