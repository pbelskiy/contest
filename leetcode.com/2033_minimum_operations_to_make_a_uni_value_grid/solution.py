class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sorted([n for row in grid for n in row])
        target = nums[len(nums) // 2]

        ops = 0
        for n in nums:
            d, m = divmod(abs(n - target), x)
            if m != 0:
                return -1
            ops += d

        return ops
