class Solution(object):
    def minStartValue(self, nums):
        m = nums[0]

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            m = min(m, nums[i])

        return abs(min(0, m)) + 1
