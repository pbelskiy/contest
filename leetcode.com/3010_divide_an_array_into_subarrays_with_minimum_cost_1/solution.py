class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        m = float('inf')

        for i in range(1, n):
            for j in range(i + 1, n):
                m = min(m, nums[0] + nums[i] + nums[j])

        return m
