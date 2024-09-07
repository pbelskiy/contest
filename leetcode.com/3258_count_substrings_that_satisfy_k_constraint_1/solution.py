class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        t = 0

        for i in range(len(s)):
            count = Counter()
            for j in range(i, len(s)):
                count[s[j]] += 1

                if count['0'] <= k:
                    t += 1

                elif count['1'] <= k:
                    t += 1

        return t
