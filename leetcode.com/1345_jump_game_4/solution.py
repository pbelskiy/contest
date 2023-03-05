class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = defaultdict(list)
        for i, n in enumerate(arr):
            d[n].append(i)

        v = set()
        q = deque([(0, 0)])
        while q:
            i, m = q.popleft()
            if i == len(arr) - 1:
                return m

            if i - 1 >= 0:
                if i - 1 not in v:
                    q.append((i - 1, m + 1))
                    v.add(i - 1)

            if i + 1 < len(arr):
                if i + 1 not in v:
                    q.append((i + 1, m + 1))
                    v.add(i + 1)

            for j in d[arr[i]]:
                if j not in v:
                    q.append((j, m + 1))
                    v.add(j)

            # clear because we already add it to queue in loop above
            d[arr[i]].clear()
