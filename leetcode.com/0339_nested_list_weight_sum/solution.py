class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def dfs(nl, d):
            t = 0

            for el in nl:
                if el.isInteger():
                    t += el.getInteger()*d
                else:
                    t += dfs(el.getList(), d + 1)

            return t

        return dfs(nestedList, 1)
