"""
Simulate process, use deque to boost performance of left and right append.

It's obvious when we take maximum element, it will be there all the time
and will be the winner.

TC: O(N) -- process the whole array unitl get max
SC: O(N) -- for deque
"""
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        q, m = deque(arr), max(arr)
        w, t = None, 0

        while t < k:
            a, b = q.popleft(), q.popleft()

            # it's already maximum
            if a == m or b == m:
                return m

            if a > b:
                q.appendleft(a)
                q.append(b)
            else:
                q.appendleft(b)
                q.append(a)

            if max(a, b) == w:
                t += 1
            else:
                w = max(a, b)
                t = 1

        return w
