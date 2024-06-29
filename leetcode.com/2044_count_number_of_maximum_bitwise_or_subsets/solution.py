class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        t = reduce(operator.or_, nums)
        s = 0

        for r in range(1, len(nums) + 1):
            for a in combinations(nums, r):
                if reduce(operator.or_, a) == t:
                    s += 1

        return s
