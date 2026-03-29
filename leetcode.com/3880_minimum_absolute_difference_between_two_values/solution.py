class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        m = float('inf')

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == 1 and nums[j] == 2 or nums[j] == 1 and nums[i] == 2:
                    m = min(m, j - i)

        if m == float('inf'):
            return -1

        return m

