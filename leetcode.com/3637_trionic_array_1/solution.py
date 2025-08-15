class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 4:
            return False

        # greedily increase left part
        left = 0
        while left + 1 < len(nums) - 1 and nums[left + 1] > nums[left]:
            left += 1

        # size must be > 1
        if left == 0:
            return False

        # greedily increase right part
        right = len(nums) - 1
        while right > left + 1 and nums[right - 1] < nums[right]:
            right -= 1

        # size must be > 1
        if right == len(nums) - 1:
            return False

        arr = nums[left:right+1]
        return len(arr) == len(set(arr)) and arr == sorted(arr, reverse=True)

