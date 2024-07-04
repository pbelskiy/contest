class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        r = []

        for i in range(1, n):
            for j in range(i, n + 1):
                if i == j:
                    continue

                for k in range(2, j):
                    if i % k == 0 and j % k == 0:
                        break
                else:
                    r.append(f'{i}/{j}')

        return r
