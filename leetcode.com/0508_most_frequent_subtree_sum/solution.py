class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node):
            if not node:
                return 0

            v = node.val + dfs(node.left) + dfs(node.right)
            cnt[v] += 1
            return v

        cnt = collections.Counter()
        dfs(root)

        values = []
        last = None

        for k, v in cnt.most_common():
            if not (last is None or last == v):
                break
            values.append(k)
            last = v

        return values
