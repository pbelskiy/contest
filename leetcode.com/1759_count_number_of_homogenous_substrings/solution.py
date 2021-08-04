class Solution:
    def countHomogenous(self, s: str) -> int:
        n = len(s)
        total = n
        x = 1
        last = None

        for ch in s:
            if ch == last:
                total += x
                x += 1
            else:
                last = ch
                x = 1

        return total % (10**9 + 7)
