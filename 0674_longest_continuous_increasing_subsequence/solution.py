class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        curr = prev = 1

        nums.append(nums[-1])
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                prev = max(prev, curr)
                curr = 1
            else:
                curr += 1

        return prev
