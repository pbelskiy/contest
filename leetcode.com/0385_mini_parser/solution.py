class Solution:
    def deserialize(self, s: str) -> NestedInteger:

        def dfs(obj):
            if isinstance(obj, int):
                return NestedInteger(obj)

            ni = NestedInteger()
            for el in obj:
                if isinstance(el, list):
                    ni.add(dfs(el))
                else:
                    ni.add(NestedInteger(el))

            return ni

        return dfs(eval(s))
