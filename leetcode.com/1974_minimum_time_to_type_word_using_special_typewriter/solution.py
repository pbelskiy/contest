class Solution:
    def minTimeToType(self, word: str) -> int:
        cost = 0
        prev = 'a'

        for ch in word:
            v = abs(ord(ch) - ord(prev))
            cost += min(v, 26 - v)
            prev = ch

        return cost + len(word)
