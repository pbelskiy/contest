class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        # get path from Bob to root
        q = deque([(bob, [bob])])
        v = set()
        while q:
            a, p = q.popleft()
            if a == 0:
                bob_path = p
                break

            for b in g[a]:
                if b not in v:
                    v.add(b)
                    q.append((b, p + [b]))

        # consume initial Bob state
        i = 1
        amount[bob] = 0

        best = float('-inf')

        # get path for Alice
        q = deque([(0, amount[0])])
        v = set([0])
        while q:
            # make Bob move
            if i < len(bob_path):
                bob = bob_path[i]
                i += 1
            else:
                bob = -1

            # make Alice moves around
            qq = deque()
            while q:
                leaf = True
                a, t = q.popleft()

                for b in g[a]:
                    if b in v:
                        continue

                    # at same node with Bob
                    if b == bob:
                        qq.append((b, t + amount[b] // 2))
                    else:
                        qq.append((b, t + amount[b]))

                    v.add(b)
                    leaf = False

                if leaf:
                    best = max(best, t)

            q = qq

            # erase after Bob move
            if bob != -1:
                amount[bob] = 0

        return best
