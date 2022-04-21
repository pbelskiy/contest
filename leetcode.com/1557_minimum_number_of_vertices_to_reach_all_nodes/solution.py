class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        s = set()
        for _, b in edges:
            s.add(b)
        return set(range(n)) - s
