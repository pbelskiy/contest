"""
Use Sliding Windows technique.

TC: O(N)
SC: O(1)
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        longest = 0

        for right in range(len(nums)):
            # decrease count of flips
            if nums[right] == 0:
                k -= 1

            # update longest
            if k >= 0:
                longest = max(longest, right - left + 1)
                continue

            # move left pointer and restore flip balance
            while k != 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        return longest
