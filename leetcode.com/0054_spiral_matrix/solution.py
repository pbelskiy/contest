class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        numbers = []

        n, m = len(matrix), len(matrix[0])
        y, x = 0, 0

        while len(visited) != n * m:
            # left -> right
            while (y, x) not in visited and x < m:
                numbers.append(matrix[y][x])
                visited.add((y, x))
                x += 1

            x -= 1
            y += 1

            # top -> down
            while (y, x) not in visited and y < n:
                numbers.append(matrix[y][x])
                visited.add((y, x))
                y += 1

            y -= 1
            x -= 1

            # right -> left
            while (y, x) not in visited and x >= 0:
                numbers.append(matrix[y][x])
                visited.add((y, x))
                x -= 1

            y -= 1
            x += 1

            # down -> up
            while (y, x) not in visited and y >= 0:
                numbers.append(matrix[y][x])
                visited.add((y, x))
                y -= 1

            y += 1
            x += 1

        return numbers
