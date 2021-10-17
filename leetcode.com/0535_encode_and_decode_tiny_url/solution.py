class Codec:

    def __init__(self):
        self.d = {}

    def encode(self, longUrl: str) -> str:
        v = str(hash(longUrl))
        self.d[v] = longUrl
        return v

    def decode(self, shortUrl: str) -> str:
        return self.d[shortUrl]
