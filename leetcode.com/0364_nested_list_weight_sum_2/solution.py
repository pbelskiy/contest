class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:

        def get_max(nl):
            if not nl:
                return 0

            m = 0
            for el in nl:
                m = max(m, get_max(el.getList()) + 1)

            return m

        def dfs(nl, d):
            t = 0

            for el in nl:
                if el.isInteger():
                    t += el.getInteger()*d
                else:
                    t += dfs(el.getList(), d - 1)

            return t

        m = get_max(nestedList)
        return dfs(nestedList, m)
