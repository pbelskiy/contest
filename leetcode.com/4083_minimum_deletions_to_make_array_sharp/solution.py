class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        t = 0

        for i in range(len(nums) - 1):
            if nums[i] ^ nums[i + 1] == 0:
                t += 1
        
        return t

