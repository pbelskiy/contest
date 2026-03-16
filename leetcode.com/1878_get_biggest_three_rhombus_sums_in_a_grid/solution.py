class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        
        def get(y, x):
            d = 1
            s = grid[y][x]
            r = [s]

            left_y, left_x = y, x
            right_y, right_x = y, x

            while True:
                # increase lines
                left_y, left_x = left_y + 1, left_x - 1
                right_y, right_x = right_y + 1, right_x + 1

                if left_y >= h or right_y > h or left_x < 0 or right_x >= w:
                    break

                s += grid[left_y][left_x]
                s += grid[right_y][right_x]

                # finish
                ss = s

                # down, right
                dy, dx = left_y, left_x
                for _ in range(d):
                    dy += 1
                    dx += 1
                    if dy >= h or dx >= w:
                        return r
                    ss += grid[dy][dx]

                # down, left
                dy, dx = right_y, right_x
                for _ in range(d - 1):
                    dy += 1
                    dx -= 1
                    ss += grid[dy][dx]

                r.append(ss)
                d += 1

            return r

        h, w = len(grid), len(grid[0])

        r = []
        for y in range(h):
            for x in range(w):
                r += get(y, x)

        return sorted(set(r), reverse=True)[:3]

