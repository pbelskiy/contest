"""
Greedy solution, just do what asked for.

TC: O(N)
SC: O(1)
"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                continue

            if i + 2 >= len(nums):
                return -1

            nums[i + 0] ^= 1
            nums[i + 1] ^= 1
            nums[i + 2] ^= 1

            total += 1

        return total
