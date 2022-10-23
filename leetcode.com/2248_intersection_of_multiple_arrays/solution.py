class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        s = set(nums[0])

        for a in nums:
            s &= set(a)

        return sorted(s)
