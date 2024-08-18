class StringIterator:

    def __init__(self, compressedString: str):
        self.s = ''
        self.i = 0

        for chunk in re.findall('(\w\d+)', compressedString):
            p, d = chunk[0], chunk[1:]
            self.s += p*int(d)

    def next(self) -> str:
        if not self.hasNext():
            return ' '

        self.i += 1
        return self.s[self.i - 1]

    def hasNext(self) -> bool:
        return self.i < len(self.s)
