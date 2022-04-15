import pickle
import base64


class Codec:

    def serialize(self, root):
        return base64.b64encode(pickle.dumps(root)).decode('utf-8')

    def deserialize(self, data):
        return pickle.loads(base64.b64decode(data.encode('utf-8')))
