class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        arr = []
        for i in range(len(nums)):
            if nums[i] != 0:
                arr.append(nums[i])

        return arr + [0]*(len(nums) - len(arr))
