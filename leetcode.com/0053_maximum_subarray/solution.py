class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        val = nums[0]
        target = val

        for i in range(1, n):
            val = max(val + nums[i], nums[i])
            target = max(target, val)

        return target
