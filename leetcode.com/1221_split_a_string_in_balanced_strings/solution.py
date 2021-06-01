class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total = rc = lc = 0

        for ch in s:
            if ch == 'R':
                rc += 1
            else:
                lc += 1

            if rc == lc:
                total += 1
                rc = 0
                lc = 0

        return total
