class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        q = deque()
        v = set()
        s = [set(r) for r in routes]

        for i in range(len(s)):
            if source in s[i]:
                q.append((1, i))
                v.add(i)

        if q and source == target:
            return 0

        while q:
            d, i = q.popleft()
            if target in s[i]:
                return d

            for j in range(len(s)):
                if j not in v and s[i] & s[j]:
                    q.append((d + 1, j))
                    v.add(j)

        return -1
