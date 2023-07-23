class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        i = len(nums) - 1

        while i > 0:
            if nums[i] >= nums[i - 1]:
                nums[i] += nums[i - 1]
                nums.pop(i - 1)

            i -= 1

        return max(nums)
