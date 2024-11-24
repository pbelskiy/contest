class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False

        a = False
        n -= 10
        s = 9

        while True:
            if n < s:
                return not a

            n -= s
            s -= 1
            a = not a
