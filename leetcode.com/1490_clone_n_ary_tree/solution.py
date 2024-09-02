class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        return copy.deepcopy(root)
