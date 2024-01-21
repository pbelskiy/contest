class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        done = False
        while not done:
            done = True
            swap = False

            for i in range(len(nums) - 1):
                if nums[i] <= nums[i + 1]:
                    continue

                done = False

                # need to swap
                if nums[i].bit_count() == nums[i + 1].bit_count():
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swap = True

            if done is False and swap is False:
                break

        return nums == sorted(nums)
