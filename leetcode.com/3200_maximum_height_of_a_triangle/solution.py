class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:

        def dfs(red, blue, curr_red, h):
            if curr_red:
                if red >= h:
                    h = max(h, dfs(red - h, blue, not curr_red, h + 1))
            else:
                if blue >= h:
                    h = max(h, dfs(red, blue - h, not curr_red, h + 1))

            return h

        return max(dfs(red, blue, True, 1), dfs(red, blue, False, 1))  - 1
