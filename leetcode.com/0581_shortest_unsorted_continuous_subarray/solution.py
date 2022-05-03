class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sn = sorted(nums)

        i = 0
        while i < len(nums) and nums[i] == sn[i]:
            i += 1

        j = len(nums) - 1
        while j > i and nums[j] == sn[j]:
            j -= 1

        return j - i + 1
