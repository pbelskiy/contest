"""
Sliding window

TC: O(N)
SC: O(1)
"""
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        score = 0
        total = 0
        left = 0

        for right in range(len(nums)):
            score += nums[right]

            while score*(right - left + 1) >= k:
                score -= nums[left]
                left += 1

            total += right - left + 1

        return total

