class Solution:
    def maximumSwap(self, num: int) -> int:
        a, m = list(str(num)), num

        for i, j in permutations(range(len(a)), 2):
            a[i], a[j] = a[j], a[i]
            m = max(m, int(''.join(a)))
            a[i], a[j] = a[j], a[i]

        return m
