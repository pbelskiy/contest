import pickle
import base64


class Codec:

    def serialize(self, root: TreeNode) -> str:
        return base64.b64encode(pickle.dumps(root)).decode('utf-8')

    def deserialize(self, data: str) -> TreeNode:
        return pickle.loads(base64.b64decode(data.encode('utf-8')))
