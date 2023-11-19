"""
Sort it, then count layer by layer number of changes.

Example:
    [1,1,3,3,5,5]
             3,3   (+2)
         1,1,1,1   (+4)

Result: 6

TC: O(NlgN)
SC: O(n)
"""
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        t = 0
        p = nums[0]

        for i in range(len(nums)):
            if nums[i] == p:
                continue

            t += len(nums) - i
            p = nums[i]

        return t
