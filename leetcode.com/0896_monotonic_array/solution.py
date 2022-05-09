class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        dec = inc = False

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                dec = True
            if nums[i] < nums[i + 1]:
                inc = True

        return not (inc and dec)
