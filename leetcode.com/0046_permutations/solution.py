class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def trace(n):
            if n == len(nums):
                permutations.append(nums[:])
                return

            for i in range(n, len(nums)):
                nums[n], nums[i] = nums[i], nums[n]
                trace(n + 1)
                nums[n], nums[i] = nums[i], nums[n]

        permutations = []
        trace(0)
        return permutations
