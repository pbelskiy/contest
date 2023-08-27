class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        s, i, arr = 0, 0, set()

        while len(arr) != n:
            i += 1
            if target - i in arr:
                continue

            arr.add(i)
            s += i

        return s
