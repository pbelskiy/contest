class Solution:
    def passwordStrength(self, password: str) -> int:
        t = 0

        for ch in set(password):
            if 'a' <= ch <= 'z':
                t += 1
            elif 'A' <= ch <= 'Z':
                t += 2
            elif '0' <= ch <= '9':
                t += 3
            elif ch in "!@#$":
                t += 5

        return t
