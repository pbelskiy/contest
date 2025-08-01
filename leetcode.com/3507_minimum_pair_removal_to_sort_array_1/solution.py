class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        t = 0

        while True:
            if nums == sorted(nums):
                break
            
            p = float('inf')
            j = 0
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < p:
                    p = nums[i] + nums[i + 1]
                    j = i

            nums[j] += nums[j + 1]
            nums.pop(j + 1)
            t += 1

        return t

