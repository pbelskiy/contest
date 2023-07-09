"""
It's also could add performance booster, by using x, y axes of
obstacles and binary search on them.

TC: O(9*commands)
SC: O(obstacles)
"""
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        y, x, f, d, o = 0, 0, 0, 0, {tuple(p) for p in obstacles}

        for k in commands:
            if k == -2:    # turn left 90 degrees
                f = (f - 1) % 4
            elif k == -1:  # turn right 90 degrees
                f = (f + 1) % 4
            elif f == 0:   # north
                while k > 0 and (x, y + 1) not in o:
                    y += 1; k -= 1
            elif f == 1:   # east
                while k > 0 and (x + 1, y) not in o:
                    x += 1; k -= 1
            elif f == 2:   # south
                while k > 0 and (x, y - 1) not in o:
                    y -= 1; k -= 1
            elif f == 3:   # west
                while k > 0 and (x - 1, y) not in o:
                    x -= 1; k -= 1

            d = max(d, x**2 + y**2)

        return d
