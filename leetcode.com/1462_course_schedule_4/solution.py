class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]]
    ) -> List[bool]:

        @cache
        def dfs(a, t):
            if a == t:
                return True

            for b in g[a]:
                if dfs(b, t):
                    return True

            return False

        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)

        answer = []
        for a, b in queries:
            answer.append(dfs(a, b))

        return answer
