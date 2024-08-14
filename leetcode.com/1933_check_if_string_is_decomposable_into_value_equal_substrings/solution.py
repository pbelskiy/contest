class Solution:
    def isDecomposable(self, s: str) -> bool:
        s += 'X'  # dummy char to simplify logic
        j = 0

        count = Counter()
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                continue

            count[i - j] += 1
            j = i

        t = 0
        for k in count:
            if k == 1:
                return False

            if k > 3 and k % 3 != 0:
                t += 1
            elif k == 2:
                t += 1

        return t == 1
