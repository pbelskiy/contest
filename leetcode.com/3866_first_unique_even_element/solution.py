class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        count = Counter(nums)
        for n in nums:
            if n & 1 == 0 and count[n] == 1:
                return n
        return -1

