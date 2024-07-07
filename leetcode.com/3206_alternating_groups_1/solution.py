class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        colors += colors  # to simplify index bounds

        t = 0
        for i in range(len(colors) // 2):
            if colors[i] != colors[i + 1] and colors[i - 1] == colors[i + 1]:
                t += 1

        return t
