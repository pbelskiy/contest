class Solution:
    def maxSum(self, nums: List[int]) -> int:
        best = -1

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if max(str(nums[i])) != max(str(nums[j])):
                    continue

                best = max(best, nums[i] + nums[j])

        return best
