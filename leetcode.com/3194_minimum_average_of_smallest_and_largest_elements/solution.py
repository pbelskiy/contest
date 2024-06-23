class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        a = []

        for _ in range(len(nums) // 2):
            lo, hi = min(nums), max(nums)
            nums.remove(lo)
            nums.remove(hi)
            a.append((lo + hi) / 2)

        return min(a)
