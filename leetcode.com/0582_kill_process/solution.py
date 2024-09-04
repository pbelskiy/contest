class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        d = defaultdict(list)

        for a, b in zip(pid, ppid):
            d[b].append(a)

        if kill not in d:
            return [kill]

        q = deque([kill])
        v = []
        while q:
            a = q.popleft()
            v.append(a)
            for b in d[a]:
                q.append(b)

        return v
