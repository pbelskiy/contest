"""
Due to we can visit nodes in arbitary way, we can use AND of all nodes
in each graph component to reduce cost.

1) Find all graph components and there summary bitwise AND
2) For each query calculate result

TC: O(N)
SC: O(N)
"""
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        def bfs(a, cid):
            m = -1
            q = deque([(a, -1)])
            v = set()

            while q:
                a, w = q.popleft()
                m &= w
                d[a] = cid

                for b, w in g[a]:
                    if (b, w) not in v:
                        v.add((b, w))
                        q.append((b, w))

            return {a: cid for a in v}, m

        g = defaultdict(list)
        for a, b, w in edges:
            g[a].append((b, w))
            g[b].append((a, w))

        # find all graph components and weight
        d, w = {}, {}
        for a, cid in enumerate(range(n)):
            if a not in d:
                dd, ww = bfs(a, cid)
                w[cid] = ww
                d.update(dd)

        # calculate result
        answer = []
        for a, b in query:
            if d[a] == d[b]:
                answer.append(w[d[a]])
            else:
                answer.append(-1)

        return answer

