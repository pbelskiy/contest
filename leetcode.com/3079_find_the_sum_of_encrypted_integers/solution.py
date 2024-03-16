class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        t = 0
        for n in nums:
            t += int(max(str(n))*len(str(n)))
        return t
