class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = sum(rolls) + n
        count = len(rolls) + n

        # it's imposible mean
        if total / count > mean:
            return []

        x = count * mean
        rest = x - total

        a = [1]*n

        for i in range(n):
            v = min(rest, 5)
            a[i] += v
            rest -= v

            if rest == 0:
                break

        if (sum(rolls) + sum(a)) // count != mean:
            return []

        return a
