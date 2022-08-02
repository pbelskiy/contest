class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        total = sum(nums)
        nums.sort()

        while total > 0:

            for j in range(len(nums)):
                if nums[j] > 0:
                    break

            n = nums[j]

            for i in range(j, len(nums)):
                if nums[i] > 0:
                    nums[i] -= n
                    total -= n

            operations += 1

        return operations
