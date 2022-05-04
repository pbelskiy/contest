class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a, b = zip(*paths)
        return list((set(b) - set(a)))[0]
