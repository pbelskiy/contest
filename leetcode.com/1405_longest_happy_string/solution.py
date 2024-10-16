"""
Greedy approach, use heapq for convenience.

TC: O(a+b+c)
SC: O(a+b+c)
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = ''

        q = []
        h = []

        for cnt, ch in ((a, 'a'), (b, 'b'), (c, 'c')):
            heappush(h, (-cnt, ch))

        while h:
            cnt, ch = heappop(h)            # get largest char

            if cnt != 0 and s[-2:] != ch*2: # add to s if possible
                s += ch
                heappush(h, (cnt + 1, ch))  # put back to heap

                for cnt, ch in q:
                    heappush(h, q.pop())    # put back to heap from queue
            else:
                q.append((cnt, ch))         # add to queue

        return s
