class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, arr1) & reduce(lambda a, b: a ^ b, arr2)
