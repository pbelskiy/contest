class Solution:
    def validPalindrome(self, s: str) -> bool:
        errors = 0
        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:

            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
                continue

            if errors > 1:
                return False
            elif errors == 1:
                p1 = s1
                p2 = s2
                errors += 1
                continue

            if p2 - 1 >= 0 and s[p1] == s[p2 - 1]:
                s1 = p1 + 1
                s2 = p2
                p2 -= 1
            elif p1 + 1 < len(s) and s[p1+1] == s[p2]:
                s1 = p1
                s2 = p2 - 1
                p1 += 1
            else:
                return False

            errors += 1

        return True
