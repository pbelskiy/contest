class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        for k, v in Counter(nums).items():
            if v > 2:
                return False
        return True
