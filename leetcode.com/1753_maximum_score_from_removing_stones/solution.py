class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        h = [-a, -b, -c]
        heapify(h)

        t = 0
        while True:
            x, y = heappop(h), heappop(h)
            if x == 0 or y == 0:
                break

            t += 1
            heappush(h, x + 1)
            heappush(h, y + 1)

        return t
