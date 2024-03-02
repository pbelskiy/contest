class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0

        for n in sorted(nums):
            if n >= k:
                break
            count += 1

        return count
