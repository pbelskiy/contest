class Solution:
    def findValidPair(self, s: str) -> str:
        freq = Counter(s)

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                continue
            if freq[s[i]] != int(s[i]):
                continue
            if freq[s[i + 1]] != int(s[i +1]):
                continue

            return s[i] + s[i+1]

        return ''
