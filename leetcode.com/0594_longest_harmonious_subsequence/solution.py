class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count, longest = sorted(Counter(nums).items()), 0

        for i in range(len(count) - 1):
            if count[i + 1][0] - count[i][0] == 1:
                longest = max(longest, count[i + 1][1] + count[i][1])

        return longest
