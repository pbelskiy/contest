class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total = 0

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                continue

            d = nums[i] - nums[i + 1] + 1
            nums[i + 1] += d
            total += d

        return total
