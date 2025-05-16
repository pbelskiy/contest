"""
Use dyamic programming, recursion with cache.

TC: O(N^2)
SC: O(N^2)
"""
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        @cache
        def dfs(curr, prev):
            if curr == len(words):
                return []

            # skip
            longest = dfs(curr + 1, prev)

            # take
            if prev is None or (len(words[curr]) == len(words[prev]) and groups[curr] != groups[prev] and sum(a != b for a, b in zip(words[curr], words[prev])) == 1):
                longest = max(longest, [words[curr]] + dfs(curr + 1, curr), key=len)

            return longest

        return dfs(0, None)

