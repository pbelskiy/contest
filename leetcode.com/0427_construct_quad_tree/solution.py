class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def get_value(y1, x1, y2, x2):
            value = grid[y1][x1]

            for y in range(y1, y2):
                for x in range(x1, x2):
                    if grid[y][x] != value:
                        return None

            return value

        def build(root, y1, x1, y2, x2):
            # top left
            args = [y1, x1, y1 + (y2 - y1) // 2, x1 + (x2 - x1) // 2]
            if not (args[0] == args[2] or args[1] == args[3]):
                val = get_value(*args)
                node = Node(val, 1, None, None, None, None)
                if val is None:
                    build(node, *args)
                root.topLeft = node
                root.isLeaf = 0

            # top right
            args = [y1, x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2, x2]
            if not (args[0] == args[2] or args[1] == args[3]):
                val = get_value(*args)
                node = Node(val, 1, None, None, None, None)
                if val is None:
                    build(node, *args)
                root.topRight = node
                root.isLeaf = 0

            # bottom left
            args = [y1 + (y2 - y1) // 2, x1, y2, x1 + (x2 - x1) // 2]
            if not (args[0] == args[2] or args[1] == args[3]):
                val = get_value(*args)
                node = Node(val, 1, None, None, None, None)
                if val is None:
                    build(node, *args)
                root.bottomLeft = node
                root.isLeaf = 0

            # bottom right
            args = [y1 + (y2 - y1) // 2, x1 + (x2 - x1) // 2, y2, x2]
            if not (args[0] == y1 or args[1] == x1):
                val = get_value(*args)
                node = Node(val, 1, None, None, None, None)
                if val is None:
                    build(node, *args)
                root.isLeaf = 0
                root.bottomRight = node

        args = [0, 0, len(grid), len(grid)]
        val = get_value(*args)
        root = Node(val, 1, None, None, None, None)
        if val is None:
            build(root, *args)

        return root
