"""
Use prefix sum here.

TC: O(N)
SC: O(N)
"""
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = list(accumulate(nums))
        arr = []

        for i in range(len(nums)):
            # sum of left part
            if i == 0:
                left = 0
            else:
                left = nums[i]*i - prefix[i - 1]

            # sum of right part
            right = (prefix[-1] - prefix[i]) - nums[i]*(len(nums) - i - 1)

            arr.append(left + right)

        return arr
