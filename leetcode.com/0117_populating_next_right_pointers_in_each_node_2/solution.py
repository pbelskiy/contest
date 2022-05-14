class Solution:
    def connect(self, root: 'Node') -> 'Node':

        def dfs(node, level):
            if not node:
                return
            levels[level].append(node)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        levels = collections.defaultdict(list)
        dfs(root, 0)

        for level in levels.values():
            for n1, n2 in zip(level, level[1:]):
                n1.next = n2

        return root
