class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        d = {}
        r = []
        cnt = Counter()

        for i, j in queries:
            if i not in d:
                cnt[j] += 1
            elif d[i] != j:
                cnt[j] += 1
                cnt[d[i]] -= 1
                if cnt[d[i]] == 0:
                    del cnt[d[i]]

            d[i] = j
            r.append(len(cnt))

        return r
