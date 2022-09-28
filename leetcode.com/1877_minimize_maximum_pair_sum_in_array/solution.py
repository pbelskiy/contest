class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        r, i, j = 0, 0, len(nums) - 1

        while i < j:
            r = max(r, nums[i] + nums[j])
            i += 1
            j -= 1

        return r
