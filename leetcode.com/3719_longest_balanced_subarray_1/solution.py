class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        m = 0

        for i in range(len(nums)):
            even, odd = set(), set()
            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])

                if len(even) == len(odd):
                    m = max(m, j - i + 1)
        
        return m

