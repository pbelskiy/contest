class Solution:
    def sortColors(self, nums: List[int]) -> None:
        done = False

        while not done:
            done = True

            for i in range(len(nums)):
                for j in range(i, len(nums)):
                    if nums[i] > nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
                        done = False
                        continue
