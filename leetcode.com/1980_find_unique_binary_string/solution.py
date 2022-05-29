class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        a = {int(n, 2) for n in nums}

        for i in range(2**len(nums)):
            if i not in a:
                return bin(i)[2:].zfill(len(nums[0]))
