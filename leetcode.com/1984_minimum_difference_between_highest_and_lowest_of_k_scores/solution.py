class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        left, right, minimum = 0, k - 1, float('inf')

        while right < len(nums):
            minimum = min(minimum, nums[right] - nums[left])
            left += 1
            right += 1

        return minimum
