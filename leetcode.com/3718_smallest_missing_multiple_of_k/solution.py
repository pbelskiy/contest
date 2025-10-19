class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        n = k
        while True:
            if n not in s:
                return n
            n += k

