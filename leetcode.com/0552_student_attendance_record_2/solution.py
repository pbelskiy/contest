@cache
def dp(a, l, t):
    if t == 0:
        return 1

    r = dp(a, 0, t - 1)  # present
    if a < 1:
        r += dp(a + 1, 0, t - 1)  # absent
    if l < 2:
        r += dp(a, l + 1, t - 1)  # late

    return r % (10**9 + 7)


class Solution:
    def checkRecord(self, n: int) -> int:
        return dp(0, 0, n) % (10**9 + 7)
