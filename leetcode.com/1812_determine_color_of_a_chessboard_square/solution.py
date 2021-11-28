class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        row = ord(coordinates[0]) - ord('a') + 1
        col = int(coordinates[1])

        return row % 2 != col % 2
