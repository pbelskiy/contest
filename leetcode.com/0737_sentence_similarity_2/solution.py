class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        if len(sentence1) != len(sentence2):
            return False

        d = defaultdict(set)
        for a, b in similarPairs:
            d[a].add(b)
            d[b].add(a)

        def bfs(a):
            q = deque([a])
            v = set()

            while q:
                a = q.popleft()

                for b in d[a]:
                    if b not in v:
                        v.add(b)
                        q.append(b)

            return v

        t = {w: bfs(w) for w in d}

        for a, b in zip(sentence1, sentence2):
            if a == b:
                continue

            if a in t.get(b, {}) or b in t.get(a, {}):
                continue

            return False

        return True
