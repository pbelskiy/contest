class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        s = []

        for i, n in enumerate(nums):
            while len(s) + len(nums) - i > k and s and s[-1] > n:
                s.pop()
            s.append(n)

        return s[:k]
