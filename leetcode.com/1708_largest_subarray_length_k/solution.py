class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        m = max(nums[:len(nums) - k + 1])  # find max element
        i = nums.index(m)                  # find start index of max element
        return nums[i:i+k]                 # return that subarray
