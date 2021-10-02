class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        total, n = 0, len(nums)

        for i in range(n):
            for j in range(n):
                if i != j and nums[i] + nums[j] == target:
                    total += 1

        return total
