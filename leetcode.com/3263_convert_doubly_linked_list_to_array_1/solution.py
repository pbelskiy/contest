class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        vals = []

        while root:
            vals.append(root.val)
            root = root.next

        return vals
