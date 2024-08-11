class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        for k, v in sorted(Counter(nums).items(), key=lambda t: (-t[0], t[1])):
            if v == 1:
                return k

        return -1
