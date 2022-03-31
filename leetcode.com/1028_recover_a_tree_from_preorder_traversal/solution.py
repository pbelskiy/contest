class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        def get_positions():
            values = []
            depth = 0

            i = 0
            while i < len(traversal):
                if traversal[i] == '-':
                    depth += 1
                    i += 1
                    continue

                j = i
                while j < len(traversal) and traversal[j] != '-':
                    j += 1

                values.append((depth, int(traversal[i:j]), i))

                depth = 0
                i = j

            return values

        def get_indexes(left, right, depth):
            p = []

            for i in range(left, right):
                if positions[i][0] == depth:
                    p.append((positions[i][1], i))

            if len(p) == 0:
                return None, None, None, None

            if len(p) == 1:
                p.append((None, None))

            return *p[0], *p[1]

        def build(parent, left, right, depth):
            lv, lp, rv, rp = get_indexes(left, right, depth + 1)

            if lv:
                parent.left = TreeNode(lv)
                build(parent.left, left, rp or right, depth + 1)

            if rv:
                parent.right = TreeNode(rv)
                build(parent.right, rp or right, right, depth + 1)

            return parent

        positions = get_positions()
        return build(TreeNode(positions[0][1]), 0, len(positions), 0)
