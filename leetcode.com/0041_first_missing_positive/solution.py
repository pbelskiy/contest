class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)  # O(N)
        m = 1
        while m in s:  # O(N)
            m += 1
        return m       # O(2N) = O(N)
