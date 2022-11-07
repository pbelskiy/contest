class Solution:
    def averageValue(self, nums: List[int]) -> int:
        values = list(filter(lambda n: n % 2 == n % 3 == 0, nums))
        return sum(values) // len(values) if len(values) > 0 else 0
