class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return map(int, ''.join(map(str, nums)))
