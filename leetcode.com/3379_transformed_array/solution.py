class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)

        for i, n in enumerate(nums):
            j = (i + nums[i]) % len(nums)
            result[i] = nums[j]

        return result
