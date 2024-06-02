class Solution:
    def minimumChairs(self, s: str) -> int:
        b = 0
        m = 0
        for ch in s:
            if ch == 'E':
                b += 1
            else:
                b -= 1

            m = max(m, b)

        return m
