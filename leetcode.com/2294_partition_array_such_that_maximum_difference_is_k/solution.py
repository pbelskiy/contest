class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        t = 0
        left = 0
        right = 0

        while right < len(nums):
            while right < len(nums) and nums[right] - nums[left] <= k:
                right += 1

            left = right
            t += 1

        return t
