class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.values = []
        self.i = 0

        def dfs(l):
            for v in l:
                if v.isInteger():
                    self.values.append(v.getInteger())
                else:
                    dfs(v.getList())

        dfs(nestedList)

    def next(self) -> int:
        self.i += 1
        return self.values[self.i - 1]

    def hasNext(self) -> bool:
        return self.i < len(self.values)
