class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        m = -1
        s = 0
        for i in range(len(nums)):
            if i >= 2 and nums[i] < s:
                m = max(m, s + nums[i])
            s += nums[i]

        return m
