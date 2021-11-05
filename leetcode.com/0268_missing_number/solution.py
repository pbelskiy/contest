class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        should = len(nums)
        have = 0

        for i in range(len(nums)):
            should += i
            have += nums[i]

        return should - have
