class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        m = float('inf')

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        m = min(m, nums[i] + nums[j] + nums[k])

        return m if m != float('inf') else -1
