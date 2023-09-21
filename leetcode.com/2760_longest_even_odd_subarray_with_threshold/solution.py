class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        best = 0

        for i in range(len(nums)):
            if nums[i] > threshold or nums[i] % 2 == 1:
                continue

            best = max(best, 1)
            for j in range(i + 1, len(nums)):
                if nums[j] > threshold or nums[j] % 2 == nums[j - 1] % 2:
                    break

                best = max(best, j - i + 1)

        return best
