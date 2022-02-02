class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indexes = []

        n = len(p)

        p_count = collections.Counter(p)
        i_count = collections.Counter(s[:n])

        for i in range(n, len(s) + 1):
            if i_count == p_count:
                indexes.append(i - n)

            i_count[s[i - n]] -= 1

            if i < len(s):
                i_count[s[i]] += 1

            if i_count[s[i - n]] == 0:
                del i_count[s[i - n]]

        return indexes
