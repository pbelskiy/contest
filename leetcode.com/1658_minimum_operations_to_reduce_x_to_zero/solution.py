class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        best = float('inf')
        total = 0
        left = 0

        if target < 0:
            return -1

        if target == 0:
            return len(nums)

        for right in range(len(nums)):
            total += nums[right]

            while left < right and total > target:
                total -= nums[left]
                left += 1

            if total == target:
                best = min(best, len(nums) - (right - left + 1))

        if best == float('inf'):
            return -1

        return best
