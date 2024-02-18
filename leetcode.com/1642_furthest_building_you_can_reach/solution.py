"""
Initially it was hard proble for me, I've tried recursion with memoization
which gave me TLE.

But acaully problem is quite simple, just use bricks every time we need,
and only when there is no enought bricks now, try to replace previously
largest bricks pile to one ladder.

TC: O(NlgN)
SC: O(N)
"""
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        h = []
        for i in range(len(heights) - 1):
            if (d := heights[i + 1] - heights[i]) <= 0:
                continue

            if bricks >= d:
                bricks -= d
                heappush(h, -d)
                continue

            if ladders == 0:
                break

            if len(h) == 0:
                ladders -= 1
                continue

            # get previously used largest bricks pile
            p = -heappop(h)
            if p < d:
                heappush(h, -p)
                ladders -= 1
                continue

            # get back bricks and use there ladder instead
            bricks += p
            ladders -= 1
            bricks -= d
            heappush(h, -d)
        else:
            return len(heights) - 1

        return i
