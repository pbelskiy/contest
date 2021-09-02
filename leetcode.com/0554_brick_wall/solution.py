class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        h = collections.defaultdict(int)

        for row in wall:
            p = 0
            for brick in row:
                h[p] += 1
                p += brick

        h.pop(0, None)

        if len(h) == 0:
            return len(wall)

        # print(len(wall), h)
        return len(wall) - max(h.values())
