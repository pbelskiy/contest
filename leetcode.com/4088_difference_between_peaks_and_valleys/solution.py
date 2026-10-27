class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        a, b = 0, 0

        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                a += nums[i]
            if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                b += nums[i]
        
        return a - b

