class Solution:
    def secondHighest(self, s: str) -> int:
        nums = sorted(set(filter(lambda v: v.isdigit(), s)))
        if len(nums) < 2:
            return -1
        return nums[-2]
