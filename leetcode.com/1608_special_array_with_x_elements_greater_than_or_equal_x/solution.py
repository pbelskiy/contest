class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        for x in range(1, len(nums) + 1):
            if len(list(filter(lambda n: n >= x, nums))) == x:
                return x

        return -1
