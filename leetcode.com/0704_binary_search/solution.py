class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect.bisect(nums, target) - 1
        return i if nums[i] == target else -1
