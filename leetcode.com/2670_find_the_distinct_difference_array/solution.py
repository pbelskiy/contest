class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        diff = []

        for i in range(1, len(nums) + 1):
            diff.append(len(set(nums[:i])) - len(set(nums[i:])))

        return diff
