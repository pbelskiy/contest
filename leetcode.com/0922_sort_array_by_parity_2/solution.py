class Solution:
    def sortArrayByParityII(self, nums):
        n, even, odd = len(nums) - 1, 0, 0

        while even < n and odd < n:

            while (even % 2 == 1 or nums[even] % 2 == 0) and even < n:
                even += 1

            while (odd % 2 == 0 or nums[odd] % 2 == 1) and odd < n:
                odd += 1

            nums[even], nums[odd] = nums[odd], nums[even]

            even += 1
            odd += 1

        return nums
