class Solution:
    def minOperations(self, s: str) -> int:
        """
        Comare with two possible vaild variants
        0101...
        1010...
        """
        t1, t2 = 0, 0
        p1, p2 = '0', '1'

        for i in range(len(s)):
            if s[i] != p1:
                t1 += 1
            if s[i] != p2:
                t2 += 1

            p1 = '1' if p1 == '0' else '0'
            p2 = '1' if p2 == '0' else '0'

        return min(t1, t2)
