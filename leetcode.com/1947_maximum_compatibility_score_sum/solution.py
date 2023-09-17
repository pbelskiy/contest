class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:

        @cache
        def score(i, j):
            t = 0
            for k in range(len(students[i])):
                if students[i][k] == mentors[j][k]:
                    t += 1
            return t

        @cache
        def dfs(s, m):
            best = 0

            for i in s:
                for j in m:
                    new_s = tuple(set(s) - set([i]))
                    new_m = tuple(set(m) - set([j]))
                    best = max(best, dfs(new_s, new_m) + score(i, j))

            return best

        return dfs(tuple(range(len(students))), tuple(range(len(mentors))))
