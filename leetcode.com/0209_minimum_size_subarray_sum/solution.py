class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = float('inf')
        left = 0
        total = 0

        for right in range(len(nums)):
            total += nums[right]
            if total < target:
                continue

            while total >= target:
                best = min(best, right - left + 1)
                total -= nums[left]
                left += 1

        return best if best != float('inf') else 0
