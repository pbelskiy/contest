class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        right = 0
        while right + 1 < len(nums) and nums[right] + 1 == nums[right + 1]:
            right += 1

        t = sum(nums[:right+1])
        s = set(nums)
        while t in s:
            t += 1

        return t
