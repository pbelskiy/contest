class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        pos = [n for n in nums if n > 0]
        neg = [n for n in nums if n < 0]

        # get maximum even numbers
        neg = sorted(neg)[:len(neg) - len(neg) % 2]

        if not pos and not neg:
            return max(nums)

        return math.prod(pos) * math.prod(neg)
