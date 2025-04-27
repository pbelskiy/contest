"""
Brute force, try to find all matches per cells,
then overlapped cells are the solutions count,
use z function for fast pattern matching.

TC: O(N*M)
SC: O(N*M)
"""
def z_func(s):
    z = [0]*len(s)

    l, r = 0, 0

    for i in range(1, len(s)):
        # use previous info to optimize search
        if i <= r:
            z[i] = min(
                z[i - l],  # previous prefix
                r - i + 1  # remain characters in range
            )

        # increase step by step
        while i + z[i] < len(s) and s[i + z[i]] == s[z[i]]:
            z[i] += 1

        # increase r
        if z[i] > 0 and i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1

    return z


def find_substring(s, p):
    z = z_func(p + '#' + s)
    result = []
    for i in range(len(p) + 1, len(z)):
        if z[i] == len(p):
            result.append(i - len(p) - 1)

    return result


class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        h, w = len(grid), len(grid[0])

        f = Counter()

        # process horizontal
        hs, hd = '', {}
        for y in range(h):
            for x in range(w):
                hd[len(hs)] = (y, x)
                hs += grid[y][x]

        a = find_substring(hs, pattern)
        for i in range(len(a)):
            k = a[i + 1] - a[i] if i + 1 < len(a) else 10**9

            for j in range(min(len(pattern), k)):
                f[hd[a[i] + j]] = 1

        # process vertical
        vs, vd = '', {}
        for x in range(w):
            for y in range(h):
                vd[len(vs)] = (y, x)
                vs += grid[y][x]

        # find cell intersections
        t = 0
        a = find_substring(vs, pattern)
        for i in range(len(a)):
            k = a[i + 1] - a[i] if i + 1 < len(a) else 10**9

            for j in range(min(len(pattern), k)):
                if f[vd[a[i] + j]]:
                    t += 1

        return t

