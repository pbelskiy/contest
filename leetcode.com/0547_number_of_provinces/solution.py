class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        d = collections.defaultdict(set)

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]:
                    d[i].add(j)

        groups = []
        for _, v in d.items():
            add = False

            for g in groups:
                if g & v:
                    g |= v
                    add = True

            if not add:
                groups.append(v)

        found = True
        while found:
            found = False
            for i in range(len(groups)):
                for j in range(i + 1, len(groups)):
                    if groups[i] & groups[j]:
                        found = True
                        groups[i] |= groups[j]
                        groups[j].clear()

        return len(list(filter(lambda g: len(g) > 0, groups)))
