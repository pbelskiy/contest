class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.cmb = itertools.combinations(characters, combinationLength)
        self.last = next(self.cmb)

    def next(self) -> str:
        ret = ''.join(self.last)
        try:
            self.last = next(self.cmb)
        except StopIteration:
            self.last = None

        return ret

    def hasNext(self) -> bool:
        return self.last
