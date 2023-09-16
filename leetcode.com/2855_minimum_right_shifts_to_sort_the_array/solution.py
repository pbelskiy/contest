class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        target = sorted(nums)

        for i in range(len(nums)):
            if nums == target:
                return i

            nums.insert(0, nums.pop())

        return -1
