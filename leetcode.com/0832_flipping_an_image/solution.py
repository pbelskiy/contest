class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flipped = []

        for row in image:
            flipped.append([int(not v) for v in reversed(row)])

        return flipped
