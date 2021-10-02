class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []

        array = []
        row = []

        for v in original:
            if len(row) != n:
                row.append(v)
                continue

            array.append(row)
            row = []
            row.append(v)

        if row:
            array.append(row)

        return array
