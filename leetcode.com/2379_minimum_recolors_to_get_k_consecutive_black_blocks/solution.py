class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minimum = float('inf')

        for i in range(len(blocks)):
            w = b = 0
            for j in range(i, len(blocks)):
                if blocks[j] == 'W':
                    w += 1
                else:
                    b += 1

                if w + b == k:
                    minimum = min(minimum, w)

        return minimum
