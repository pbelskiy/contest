from collections import deque


class Solution:

    def get_distance(self, m, _y, _x):
        yl = len(m)
        xl = len(m[0])

        visited = set()

        queue = deque()
        queue.append((_y, _x, 0))
        visited.add((_y, _x))
        distance = 10**6

        # BFS
        while len(queue) > 0:
            y, x, d = queue.popleft()

            if m[y][x] == 0:
                return d

            for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                ny = y + dy
                nx = x + dx

                if ny >= yl or ny < 0 or nx >= xl or nx < 0:
                    continue

                if (ny, nx) in visited:
                    continue

                visited.add((ny, nx))
                queue.append((ny, nx, d + 1))

        return distance

    def updateMatrix(self, m):
        for y in range(len(m)):
            for x in range(len(m[0])):
                if m[y][x] != 0:
                    m[y][x] = self.get_distance(m, y, x)

        return m


matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]

nm = Solution().updateMatrix(matrix)

for r in nm:
    print(r)
