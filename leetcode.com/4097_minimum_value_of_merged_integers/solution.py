class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        m = float('inf')

        for i in range(1, len(nums), 2):
            m = min(m, int(str(nums[i - 1]) + str(nums[i])))

        return m

