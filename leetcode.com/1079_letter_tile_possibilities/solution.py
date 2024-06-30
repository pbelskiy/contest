class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        s = set()

        for r in range(len(tiles)):
            for a in permutations(tiles, r + 1):
                s.add(''.join(a))

        return len(s)
