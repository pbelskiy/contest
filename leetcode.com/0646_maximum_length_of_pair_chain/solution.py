class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        @cache
        def solve(i):
            m = 0

            for j in range(len(pairs)):
                if pairs[j][0] > pairs[i][1]:
                    m = max(m, solve(j) + 1)

            return m

        return max(solve(i) + 1 for i in range(len(pairs)))
