class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        s = 0
        for i in range(len(nums)):
            s += sum(nums[max(0, i - nums[i]):i+1])
        return s
