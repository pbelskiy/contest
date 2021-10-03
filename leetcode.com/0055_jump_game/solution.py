class Solution:
    def canJump(self, nums: List[int]) -> bool:
        p = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= p:
                p = i

        return p == 0
