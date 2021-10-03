class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]

        for n in encoded:
            first = n ^ first
            arr.append(first)

        return arr
