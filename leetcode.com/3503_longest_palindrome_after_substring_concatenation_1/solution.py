"""
Since limits are small brute force is okay here.

TC: O(N^4)
SC: O(N+M)
"""
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        m = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                ss = s[i:j+1]

                if ss == ss[::-1]:
                    m = max(m, len(ss))

                for i2 in range(len(t)):
                    for j2 in range(i2, len(t)):
                        ss2 = t[i2:j2+1]

                        if ss2 == ss2[::-1]:
                            m = max(m, len(ss2))

                        x = ss + ss2
                        if x == x[::-1]:
                            m = max(m, len(x))

        return m

