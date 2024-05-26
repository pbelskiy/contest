class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        r = 0
        v = set()

        for n in nums:
            if n in v:
                r ^= n
            v.add(n)

        return r
