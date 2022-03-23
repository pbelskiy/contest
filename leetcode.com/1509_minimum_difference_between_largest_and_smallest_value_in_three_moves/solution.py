class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()

        a1 = nums[3:]
        a2 = nums[:-3]
        a3 = nums[1:-2]
        a4 = nums[2:-1]

        d1 = max(a1) - min(a1)
        d2 = max(a2) - min(a2)
        d3 = max(a3) - min(a3)
        d4 = max(a4) - min(a4)

        return min(d1, d2, d3, d4)
