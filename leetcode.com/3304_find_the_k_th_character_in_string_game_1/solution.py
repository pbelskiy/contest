class Solution:
    def kthCharacter(self, k: int) -> str:
        s = 'a'

        while len(s) < k:
            ss = s
            for ch in s:
                ss += chr((ord(ch) + 1) % ord('z'))

            s = ss

        return s[k - 1]
