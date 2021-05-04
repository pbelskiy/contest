class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0

        for i in range(len(nums)):
            if nums[i] == val:
                continue

            nums[p] = nums[i]
            p += 1

        return p
