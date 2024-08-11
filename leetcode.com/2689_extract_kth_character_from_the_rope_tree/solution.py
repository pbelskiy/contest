"""
2689. Extract Kth Character From The Rope Tree (Easy)

You are given the root of a binary tree and an integer k.
Besides the left and right children, every node of this tree has
two other properties, a string node.val containing only lowercase
English letters (possibly empty) and a non-negative integer node.len.

There are two types of nodes in this tree:
- Leaf: These nodes have no children, node.len = 0, and node.val is
some non-empty string.
- Internal: These nodes have at least one child (also at most two
children), node.len > 0, and node.val is an empty string.

The tree described above is called a Rope binary tree.
Now we define S[node] recursively as follows:

If node is some leaf node, S[node] = node.val,
Otherwise if node is some internal node, S[node] =
concat(S[node.left], S[node.right]) and S[node].length = node.len.

Return k-th character of the string S[root].

Note: If s and p are two strings, concat(s, p) is a string obtained by
concatenating p to s. For example, concat("ab", "zz") = "abzz".
"""
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:

        def dfs(node):
            if not node:
                return
            self.s += node.val
            dfs(node.left)
            dfs(node.right)

        self.s = ''
        dfs(root)
        return self.s[k - 1]
