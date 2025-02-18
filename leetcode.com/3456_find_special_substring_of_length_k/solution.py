class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for i in range(len(s) - k + 1):
            ss = s[i:i+k]

            if len(set(ss)) != 1:
                continue

            if i > 0 and s[i - 1] == ss[0]:
                continue

            if i + k < len(s) and s[i + k] == ss[0]:
                continue

            return True

        return False
