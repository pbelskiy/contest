class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        values = sorted(set(nums), reverse=True)
        if len(values) < 3:
            return values[0]
        return values[2]
