class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        g1 = defaultdict(list)
        for a, b in edges1:
            g1[a].append(b)
            g1[b].append(a)

        g2 = defaultdict(list)
        for a, b in edges2:
            g2[a].append(b)
            g2[b].append(a)

        # precompute tree2 nodes
        m = 0

        if k - 1 >= 0:
            for i, a in enumerate(range(len(g2))):
                q = deque([(a, k - 1)])
                v = set([a])

                while q:
                    a, r = q.popleft()
                    if r == 0:
                        continue

                    for b in g2[a]:
                        if b not in v:
                            q.append((b, r - 1))
                            v.add(b)

                m = max(m, len(v))

        # traverse all tree1 nodes
        answer = []

        for a in range(len(g1)):
            q = deque([(a, k)])
            v = set([a])

            while q:
                a, r = q.popleft()
                if r == 0:
                    continue

                for b in g1[a]:
                    if b not in v:
                        q.append((b, r - 1))
                        v.add(b)

            answer.append(len(v) + m)

        return answer

