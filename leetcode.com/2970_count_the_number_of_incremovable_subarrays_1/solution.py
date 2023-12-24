class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:

        def is_valid(left, right):
            arr = nums[:left] + nums[right+1:]

            for i in range(1, len(arr)):
                if arr[i] <= arr[i - 1]:
                    return False

            return True

        t = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if is_valid(i, j):
                    t += 1

        return t
