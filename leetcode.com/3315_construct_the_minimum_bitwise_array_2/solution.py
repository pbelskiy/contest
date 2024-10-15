class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:
            for i in range(n.bit_length(), -1, -1):
                x = n & ~(1 << i)
                if x | (x + 1) == n:
                    ans.append(x)
                    break
            else:
                ans.append(-1)

        return ans
