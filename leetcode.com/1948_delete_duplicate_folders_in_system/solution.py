
"""
Build tree, and calc hash of each node, then trim.

TC: O(sort)
SC: O(sort)
"""
class Node:
    def __init__(self, v, p):
        self.v = v
        self.d = {}
        self.h = 0
        self.p = p


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:

        def get_hash(s):
            h = 0
            for c in s:
                h = (h * 31 + ord(c)) % (10**9 + 7)
            return h

        def calc_nodes_hash(node):
            if not node.d:
                return 0

            hashes = [get_hash(''.join(node.d.keys()))]
            for k in node.d:
                hashes.append(calc_nodes_hash(node.d[k]))

            node.h = get_hash(''.join([str(v) for v in hashes]))
            hash_to_nodes[node.h].append(node)
            return node.h

        def dfs(node, path):
            if not node:
                return
            if path:
                folders.append(path)
            for k in node.d:
                dfs(node.d[k], path[:] + [k])

        # build tree
        paths.sort()

        root = Node('/', None)
        for path in paths:
            curr_node = root
            for part in path:
                if part not in curr_node.d:
                    curr_node.d[part] = Node(part, curr_node)
                curr_node = curr_node.d[part]

        hash_to_nodes = defaultdict(list)
        calc_nodes_hash(root)

        # trim
        for nodes in hash_to_nodes.values():
            if len(nodes) > 1:
                for node in nodes:
                    del node.p.d[node.v]

        # deserialize
        folders = []
        dfs(root, [])
        return folders

