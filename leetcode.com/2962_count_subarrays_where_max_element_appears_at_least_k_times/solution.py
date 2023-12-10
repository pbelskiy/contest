"""
Sliding window approach.

TC: O(N)
SC: O(1)
"""
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        total = 0
        freq = 0

        left = 0
        for right in range(len(nums)):
            if nums[right] == target:
                freq += 1

            while freq >= k:
                total += len(nums) - right  # current subarray + following
                if nums[left] == target:
                    freq -= 1
                left += 1

        return total
