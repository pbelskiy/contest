class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s, t = set(), set(range(1, k + 1))
        ops = 0

        while s & t != t:
            s.add(nums.pop())
            ops += 1

        return ops
