class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == sum(map(int, str(nums[i]))):
                return i
 
        return -1

