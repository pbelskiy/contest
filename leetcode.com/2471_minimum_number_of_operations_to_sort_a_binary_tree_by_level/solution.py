class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        levels = defaultdict(list)

        while q:
            node, level = q.popleft()
            levels[level].append(node.val)

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        operations = 0

        for a in levels.values():
            s = sorted(a)
            d = {c: i for i, c in enumerate(a)}

            for i in range(len(a)):
                if a[i] == s[i]:
                    continue

                j = d[s[i]]
                d[a[i]], d[a[j]] = j, i
                a[i], a[j] = a[j], a[i]
                operations += 1

        return operations
