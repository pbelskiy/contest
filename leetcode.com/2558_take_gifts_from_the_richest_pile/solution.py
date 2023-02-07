"""
Time: 7 minutes

Obvious idea to use here priority queue.
TC: O(k*lgN)
SC: O(N)
"""

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        t = sum(gifts)
        h = [-g for g in gifts]
        heapify(h)

        for _ in range(k):
            v = abs(heappop(h))
            s = int(math.sqrt(v))
            t -= v - s
            heappush(h, -s)

        return t
