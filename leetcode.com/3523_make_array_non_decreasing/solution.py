class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        t = len(nums)
        m = nums[0]

        for i in range(1, len(nums)):
            m = max(m, nums[i])

            if nums[i] < m:
                t -= 1

        return t

