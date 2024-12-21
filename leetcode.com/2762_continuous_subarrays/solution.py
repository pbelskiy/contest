"""
It's simple sliding window, except that we need to know
each step min and max value of our current window.

The trick here is that counter cannot be larger than
3 elements because of requirements (|x - y| <= 2).

TC: O(N)
SC: O(1)
"""
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        total = 0
        count = Counter()

        left = 0
        for right in range(len(nums)):
            count[nums[right]] += 1

            while max(count) - min(count) > 2:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1

            total += right - left + 1

        return total
