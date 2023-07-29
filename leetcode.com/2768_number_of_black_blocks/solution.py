class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        yaxis, xaxis = defaultdict(set), defaultdict(set)

        # pre calculte
        for y, x in coordinates:
            yaxis[y].add(x)
            xaxis[x].add(y)

        visited = set()

        def get_black_count(y, x):
            count = 0

            if x in yaxis[y]:
                count += 1
            if x + 1 in yaxis[y]:
                count += 1
            if y + 1 in xaxis[x]:
                count += 1
            if x + 1 in yaxis[y + 1]:
                count += 1

            return count

        answer = [(m - 1)*(n - 1), 0, 0, 0, 0]

        for y, x in coordinates:
            # check 9 blocks around
            dirs = (
                (y - 1, x - 1), (y - 1, x), (y - 1, x + 1),
                (y - 0, x - 1), (y - 0, x), (y - 0, x + 1),
                (y + 1, x - 1), (y + 1, x), (y + 1, x + 1),
            )

            for dy, dx in dirs:
                if dy >= m - 1 or dx >= n - 1:
                    continue

                if dy < 0 or dx < 0:
                    continue

                if (dy, dx) in visited:
                    continue

                visited.add((dy, dx))
                count = get_black_count(dy, dx)

                if count > 0:
                    answer[0] -= 1
                    answer[count] += 1

        return answer
