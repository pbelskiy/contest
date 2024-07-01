
class Solution:
    def numWays(self, words: List[str], target: str) -> int:

        @cache
        def dfs(i, j):
            if i == len(target):    # target formed +1
                return 1
            if j == len(words[0]):  # out of bounds
                return 0

            return (
                dfs(i, j + 1) +                          # we don't have this char on this column
                dfs(i + 1, j + 1) * count[j][target[i]]  # count ways in current column (i)
            ) % (10**9 + 7)

        # frequency of char for each column
        count = []
        for i in range(len(words[0])):
            count.append(Counter(w[i] for w in words))

        return dfs(0, 0)
