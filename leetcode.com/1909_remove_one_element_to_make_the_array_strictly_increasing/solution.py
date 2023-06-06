class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(-1, len(nums)):

            p = 0
            for j in range(len(nums)):
                if j == i:
                    continue

                if nums[j] <= p:
                    break

                p = nums[j]
            else:
                return True

        return False
