"""
Traverse the graph to collect all suspicious methods,
then check if non suspicious connected to suspicious
or not, and return result, to boost performance use
set here.

TC: O(N+M)
SC: O(N+M)
"""
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # build graph
        g = defaultdict(set)
        for a, b in invocations:
            g[a].add(b)

        # collect all suspicious methods
        q = deque([k])
        v = set()
        while q:
            a = q.popleft()
            v.add(a)

            for b in g[a]:
                if b not in v:
                    q.append(b)

        # check if we can remove them
        all_nodes = set(range(n))
        not_suspicious = all_nodes - v

        for a in not_suspicious:
            if v & g[a]:
                return all_nodes

        return not_suspicious
