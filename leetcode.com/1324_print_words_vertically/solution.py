class Solution:
    def printVertically(self, s: str) -> List[str]:
        return [''.join(ch).rstrip() for ch in itertools.zip_longest(*s.split(' '), fillvalue=' ')]
