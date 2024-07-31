class Solution:
    def minHeightShelves(self, books: List[List[int]], width: int) -> int:

        @cache
        def dp(i):
            if i == len(books):
                return 0

            m = float("inf")
            h = 0
            w = 0

            for j in range(i, len(books)):

                # could we put on current shelve?
                if w + books[j][0] <= width:
                    h = max(h, books[j][1])
                    w += books[j][0]
                else:
                    return min(m, dp(j) + h)

                # go next shelve
                if h > 0:
                    m = min(m, dp(j + 1) + h)

            return m

        return dp(0)
