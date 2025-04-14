"""
TC: O(N)
SC: O(N)
"""
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        f = Counter(s)
        r1 = ''

        # odd must be in center
        for k in f:
            if f[k] % 2 == 1:
                r1 = k*f[k]
                f[k] = 0
                break

        # append to left and right chars
        for k in sorted(f, reverse=True):
            if f[k] == 0:
                continue

            n = f[k] // 2
            r1 =  k*n + r1 + k*n

        ##################################

        f = Counter(s)
        r2 = ''

        # odd must be in center
        for k in f:
            if f[k] % 2 == 1:
                r2 = k
                f[k] -= 1
                break

        # append to left and right chars
        for k in sorted(f, reverse=True):
            if f[k] == 0:
                continue

            n = f[k] // 2
            r2 =  k*n + r2 + k*n

        return min(r1, r2)

