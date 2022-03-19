class Solution:
    def halveArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        have, need = 0, sum(nums) / 2
        operations = 0

        i = 0

        while have < need:
            have += nums[i] / 2
            nums[i] /= 2

            while i + 1 < len(nums) and nums[i] < nums[i + 1]:
                i += 1

            if nums[0] > nums[i]:
                nums.sort(reverse=True)
                i = 0

            operations += 1

        return operations
