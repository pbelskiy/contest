class Solution:
    def totalMoney(self, n: int) -> int:
        t, i = 0, 1

        for _ in range(n // 7):
            t += sum(list(range(i, i + 7)))
            i += 1

        return t + sum(list(range(i, i + (n % 7))))
