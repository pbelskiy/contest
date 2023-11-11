class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        t = 0

        for i in range(n+1):
            if i > limit:
                continue
            for j in range(n+1):
                if j > limit:
                    continue
                for k in range(n+1):
                    if k > limit:
                        continue

                    if i + j + k == n:
                        t += 1

        return t
