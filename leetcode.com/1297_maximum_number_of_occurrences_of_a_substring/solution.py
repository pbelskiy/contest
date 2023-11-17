class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        r = Counter()

        for i in range(len(s)):
            u = set()
            for j in range(i, min(len(s), i + maxSize)):
                u.add(s[j])
                if j - i + 1 >= minSize and len(u) <= maxLetters:
                    r[s[i:j+1]] += 1

        if not r:
            return 0

        return r.most_common(1)[0][1]
