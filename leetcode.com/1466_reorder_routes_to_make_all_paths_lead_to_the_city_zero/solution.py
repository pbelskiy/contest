class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        fw = defaultdict(list)
        bw = defaultdict(list)

        for a, b in connections:
            fw[a].append(b)
            bw[b].append(a)

        t = 0
        q = deque([0])
        v = set([0])
        while q:
            a = q.popleft()

            for b in fw[a]:
                if b not in v:
                    q.append(b)
                    v.add(b)
                    t += 1

            for b in bw[a]:
                if b not in v:
                    q.append(b)
                    v.add(b)

        return t
