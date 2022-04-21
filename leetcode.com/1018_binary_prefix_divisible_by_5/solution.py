class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = int(''.join(map(str, nums)), 2)
        v = []

        while len(v) != len(nums):
            v.append(n % 5 == 0)
            n >>= 1

        return reversed(v)
