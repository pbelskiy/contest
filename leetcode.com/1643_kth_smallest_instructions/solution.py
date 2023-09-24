class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:

        def ncr(r, c):
            if r < 0 or c < 0:
                return 0
            return math.comb(r + c, r)

        h, w, p = *destination, ''

        while True:
            ways_right = ncr(h - 1, w)
            ways_down = ncr(h, w - 1)

            # then, we should go down, it's there!
            if k > ways_down:
                p += 'V'
                h -= 1
                if k >= ways_down:
                    k -= ways_down
            else:
                p += 'H'
                w -= 1

            # we are in the destination
            if w == 0 and h == 0:
                break

        return p
