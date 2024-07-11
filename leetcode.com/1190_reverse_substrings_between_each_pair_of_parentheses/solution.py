"""
Simple DFS with simple logic

TC: O(N)
SC: O(N)
"""
class Solution:
    def reverseParentheses(self, s: str) -> str:

        def dfs(i):
            if i >= len(s):
                return i, ""

            p = ""
            j = i
            while j < len(s):
                if s[j] == "(":
                    j, chunk = dfs(j + 1)
                    p += chunk[::-1]
                elif s[j] == ")":
                    return j, p
                else:
                    p += s[j]

                j += 1

            return j, p

        return dfs(0)[1]
