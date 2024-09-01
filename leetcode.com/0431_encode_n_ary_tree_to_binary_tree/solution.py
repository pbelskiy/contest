import pickle

class Codec:
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        return pickle.dumps(root)

    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        return pickle.loads(data)
