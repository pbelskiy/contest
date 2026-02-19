"""
Use set

TC: O(N)
SC: O(N)
"""
class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        count = Counter(nums)
        freq = Counter(count.values())

        for n in nums:
            if freq[count[n]] == 1:
                return n

        return -1

