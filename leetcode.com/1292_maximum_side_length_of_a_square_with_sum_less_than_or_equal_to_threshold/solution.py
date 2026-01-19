class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:

        def is_possible(sy, sx, s):
            t = 0

            for y in range(sy, sy + s):
                t += ps[y][sx + s] - ps[y][sx]
                if t > threshold:
                    return False

            return t <= threshold

        h, w = len(mat), len(mat[0])

        # calculate prefix sum
        ps = []
        for row in mat:
            t = [0]
            for v in row:
                t.append(t[-1] + v)
            ps.append(t)
 
        # check all sides
        for s in range(min(h, w), 0, -1):
            for y in range(h - s + 1):
                for x in range(w - s + 1):
                    if is_possible(y, x, s):
                        return s

        return 0

