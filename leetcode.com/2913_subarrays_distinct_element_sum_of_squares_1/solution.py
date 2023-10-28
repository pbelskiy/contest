class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        t = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                t += len(set(nums[i:j+1]))**2

        return t
