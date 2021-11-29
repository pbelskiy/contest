class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        def union_find(lis):
            lis = map(set, lis)
            unions = []
            for item in lis:
                temp = []
                for s in unions:
                    if not s.isdisjoint(item):
                        item = s.union(item)
                    else:
                        temp.append(s)
                temp.append(item)
                unions = temp
            return unions


        d = dict()

        for acc in accounts:
            name, *emails = acc
            emails = set(emails)
            found = False

            for k, v in d.items():
                for i, s in enumerate(v):
                    if s & emails:
                        d[k][i] = s | emails
                        found = True
                        d[k] = union_find(d[k])
                        break
                if found:
                    break
            else:
                if name in d:
                    d[name].append(emails)
                else:
                    d[name] = [emails]

        r = []
        for k, v in d.items():
            for s in v:
                r.append([k, *list(sorted(s))])

        return r
