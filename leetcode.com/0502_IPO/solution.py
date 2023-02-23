"""
Here is idea that our capital only grows up.
- Sort ways by their cheap
- Add to heap all possible profits which we can with current capital
- Get largest profit from heap
- Increase our capital
"""

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]):
        ways = sorted(zip(capital, profits), key=lambda t: (t[0], -t[1]))
        heap, idx = [], 0

        while k > 0:
            while idx < len(ways):
                cap, prof = ways[idx]
                if cap > w:
                    break
                heappush(heap, -prof)
                idx += 1

            if not heap:
                break

            w += -heappop(heap)
            k -= 1

        return w
