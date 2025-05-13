class Solution:
    def maxFreqSum(self, s: str) -> int:
        f1, f2 = Counter(), Counter()

        for ch in s:
            if ch in ('a', 'e', 'i', 'o', 'u'):
                f1[ch] += 1
            else:
                f2[ch] += 1

        t = 0

        if f1:
            t += f1.most_common(1)[0][1]

        if f2:    
            t += f2.most_common(1)[0][1]

        return t

