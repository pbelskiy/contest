class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        orig = list(range(n))

        op = 0

        while True:
            arr = perm[:]

            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else:
                    arr[i] = perm[n // 2 + (i - 1) // 2]

            if arr == orig:
                return op + 1

            perm = arr
            op += 1
