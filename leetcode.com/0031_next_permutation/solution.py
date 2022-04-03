class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # find increasing suffix
        i = len(nums) - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1

        # pivot value
        j = i - 1

        # find rightmost successor and swap them, then sort rest
        i = len(nums) - 1
        while i > j:
            if nums[i] > nums[j]:
                break
            i -= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[j+1:] = sorted(nums[j+1:])
