class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        sy, sx = source
        ty, tx = target

        # black and white
        if (sy + sx) % 2 != (ty + tx) % 2:
            return -1

        # same diagonal
        if abs(sy - ty) == abs(sx - tx):
            return 1

        # it can be reached in two steps anyway
        return 2

