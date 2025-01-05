class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        left, right = p.split('*')

        i = -1
        while True:
            i = s.find(left, i + 1)
            if i == -1:
                break

            if s.find(right, i + len(left)) != -1:
                return True

        return False
