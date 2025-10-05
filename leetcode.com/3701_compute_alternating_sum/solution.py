class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        s = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                s += nums[i]
            else:
                s -= nums[i]

        return s

