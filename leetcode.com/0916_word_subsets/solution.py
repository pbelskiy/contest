class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        r = []
        c2 = collections.defaultdict(lambda: 0)

        # merge rules
        for w in words2:
            for k, v in collections.Counter(w).items():
                if k in c2:
                    c2[k] = max(c2[k], v)
                    continue

                c2[k] = v

        # check words
        for i, c1 in enumerate([collections.Counter(w) for w in words1]):
            for k2, v2 in c2.items():
                if k2 not in c1:
                    found = False
                    break

                if c1[k2] < v2:
                    found = False
                    break
            else:
                r.append(words1[i])

        return r
