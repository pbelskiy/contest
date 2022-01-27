class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        m, t = nums[0], nums[0]

        for i in range(len(nums)):
            if i > 0 and nums[i] > nums[i - 1]:
                t += nums[i]
            else:
                m = max(m, t)
                t = nums[i]

        return max(m, t)
