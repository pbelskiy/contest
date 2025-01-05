class Solution:
    def maxLength(self, nums: List[int]) -> int:
        best = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                arr = nums[i:j+1]

                if prod(arr) == lcm(*arr) * gcd(*arr):
                    best = max(best, len(arr))

        return best
