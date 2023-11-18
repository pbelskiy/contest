class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        best = 0
        left = 0

        for right in range(len(nums)):
            d = nums[left] - nums[right]
            k -= d

            while k < 0 and left < right:
                k += (nums[left] - nums[left + 1]) * (right - left)
                left += 1

            best = max(best, right - left + 1)

        return best
