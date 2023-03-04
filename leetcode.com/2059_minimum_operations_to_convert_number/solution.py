class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = deque([(start, 0)])
        v = set()

        while q:
            x, m = q.popleft()
            if x == goal:
                return m

            if not (0 <= x <= 1000):
                continue

            for n in nums:
                for y in ((x + n), (x - n), (x ^ n)):
                    if y in v:
                        continue
                    q.append((y, m + 1))
                    v.add(y)

        return -1
